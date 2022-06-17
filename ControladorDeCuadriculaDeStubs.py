# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""
from PyQt5.QtGui import QIntValidator

import os.path
import csv
from PyQt5.QtWidgets import QFileDialog,QLabel,QLineEdit,QSlider
from PyQt5.QtCore import Qt

from functools import partial
from Advertencia import adv

from PyQt5.QtCore import QThread
from cmath import tanh as complextanh
from Funciones import vectordistancias

import traceback

SS_slider="""
            QSlider::groove:horizontal {
                border: 2px solid black;
            	border-radius: 0px;
                height: 7px; 
            }
            
            QSlider::handle:horizontal {
                background: rgb(85,170,255);
                border: 2px solid black;
                width: 5px;
                margin: -2px 0;
                border-radius: 3px;
            }
            
            QSlider::add-page:horizontal {
                background:rgb(85,170,255);
            }
            
            QSlider::sub-page:horizontal {
                background: rgb(85,170,255);
            }
            
            """

SS_slider_opaco="""
                QSlider::groove:horizontal {
                    border: 2px solid black;
                	border-radius: 0px;
                    height: 7px; 
                }
                
                QSlider::handle:horizontal {
                    background: rgb(79, 93, 108);
                    border: 2px solid black;
                    width: 5px;
                    margin: -2px 0;
                    border-radius: 3px;
                }
                
                QSlider::add-page:horizontal {
                    background:rgb(79, 93, 108);
                }
                
                QSlider::sub-page:horizontal {
                    background: rgb(79, 93, 108);
                }
                
                """

class BorrarStubs(QThread):

    def __init__(self,layout,stub_i,stub_f):
        QThread.__init__(self)
        self.layout=layout
        self.stub_i=stub_i
        self.stub_f=stub_f
        
    def run(self):
        for n in range(self.stub_i,self.stub_f+1):
            try:
                self.layout.itemAtPosition(2*n-2,0).widget().deleteLater() #Label Stub
                self.layout.itemAtPosition(2*n-2,1).widget().deleteLater() #Label d
                self.layout.itemAtPosition(2*n-2,2).widget().deleteLater() #LineEdit d
                self.layout.itemAtPosition(2*n-2,3).widget().deleteLater() #ScrollBar d
                self.layout.itemAtPosition(2*n-1,1).widget().deleteLater() #Label l
                self.layout.itemAtPosition(2*n-1,2).widget().deleteLater() #LineEdit l
                self.layout.itemAtPosition(2*n-1,3).widget().deleteLater() #ScrollBar l
                
            except:
                pass
                                        
    def salir(self):
        self.exit()           

class ControladorDeCuadriculaDeStubs:
    def __init__(self,ventana_secundaria):

        self.cvs=ventana_secundaria
        
        #Inicializar
        self.cvs.pbtn_cargarstubs.show()
        self.cvs.pbtn_guardarstubs.show()
        self.cvs.pbtn_reiniciarstubs.show()
        self.cvs.spnbx_parametrosstubs.show()

        self.Zins=dict()
        
        self.N_anterior=1
        self.W=dict() #Widgets de los stubs
        self.ignorar_senhales=False
        
        
        self.W['lbl_stub1']=self.cvs.lbl_stub1
        self.W['lbl_d1']=self.cvs.lbl_d1
        self.W['linedit_d1']=self.cvs.linedit_d1
        self.W['slider_d1']=self.cvs.slider_d1
        self.W['lbl_l1']=self.cvs.lbl_l1
        self.W['linedit_l1']=self.cvs.linedit_l1
        self.W['slider_l1']=self.cvs.slider_l1
        self.cvs.slider_d1.setEnabled(False)
        self.cvs.slider_l1.setEnabled(False)
        
        self.W['lbl_d1'].setFixedWidth(69)
        self.W['lbl_d1'].setAlignment(Qt.AlignRight)
        self.W['lbl_l1'].setFixedWidth(69)
        self.W['lbl_l1'].setAlignment(Qt.AlignRight)
        self.W['linedit_d1'].setValidator(QIntValidator())
        self.W['linedit_l1'].setValidator(QIntValidator())
        
        #Conexiones
        self.W['linedit_d1'].editingFinished.connect(partial(self.editing_finished,self.W['linedit_d1'],1,0))
        self.W['linedit_l1'].editingFinished.connect(partial(self.editing_finished,self.W['linedit_l1'],1,1))
        self.W['linedit_d1'].textChanged.connect(partial(self.text_changed,self.W['linedit_d1'],1,0))
        self.W['linedit_l1'].textChanged.connect(partial(self.text_changed,self.W['linedit_l1'],1,1))
        
        self.W['slider_d1'].valueChanged.connect(partial(self.slider_value_changed,self.W['slider_d1'],1,0))
        self.W['slider_l1'].valueChanged.connect(partial(self.slider_value_changed,self.W['slider_l1'],1,1))
        self.W['slider_d1'].sliderReleased.connect(self.slider_released)
        self.W['slider_l1'].sliderReleased.connect(self.slider_released)
        
        self.datos=self.plantilla_datos()
        if self.cvs.bandera=='buscar':
            for nombre in self.cvs.cvp.no_fallidos:
                algoritmoX=self.cvs.cvp.Buscadores[nombre]
                break
            self.intervalo=round(algoritmoX.dmax-algoritmoX.dmin)   
        elif self.cvs.bandera=='graficar':
            self.ps=50 #porcentaje para el minimo y el máximo de los sliders

        #Conexiones
        self.cvs.spnbx_parametrosstubs.valueChanged.connect(self.accion_spnbx)
        self.cvs.pbtn_cargarstubs.clicked.connect(self.cargar)
        self.cvs.pbtn_guardarstubs.clicked.connect(self.guardar)
        self.cvs.pbtn_reiniciarstubs.clicked.connect(self.clicked_reiniciar)
        self.cvs.cbx_cargastubs.currentTextChanged.connect(self.accion_cbx_cargastubs)
        
    ### Lógica de Interfaz Gráfica
        
    def bloquear(self): 
        self.cvs.gpbx_stubs.setEnabled(False)
        
    def desbloquear(self):
        self.cvs.gpbx_stubs.setEnabled(True)
        
    def plantilla_datos(self,disposicion='Paralelo',carga='Corto circuito',Nstubs=1): 
        # disposicion,carga,Nstubs
        # d1,l1
        # d2,l2
        # ...
        # dN,lN
        
        datos=[[disposicion,carga,Nstubs]]
        for i in range(Nstubs): datos.append(['',''])
            
        return datos
    
    def cargar(self): 
        try:
            carpeta='./Datos/MSMN'
            ruta = QFileDialog.getOpenFileName(self.cvs, 'Cargar archivo',carpeta,"*.msmn")[0]
            if os.path.exists(ruta):
                datos=[]
                with open(ruta) as archivo:
                    lector = csv.reader(archivo, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    for fila in lector: datos.append(fila) 
                
                if self.formato_correcto(datos): pass
                else: raise Exception
                
                self.datos=datos
                if self.cvs.bandera=='buscar': self.cvs.cvp.Buscadores[self.cvs.cbx_algoritmos.currentText()].datos=self.datos
                self.determinar_posicion_entrada_adaptador()
                    
                self.ignorar_senhales=True
                self.datosAventana()
                self.ignorar_senhales=False
                
                self.graficar()
                           
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos de la MSMN.')
            ad.exec_()
            self.ignorar_senhales=False
            self.reiniciar_por_codigo()
            
    def cargar_datos(self,datos,avisar=True): 
        try: 
            if self.formato_correcto(datos): pass
            else: raise Exception
            
            self.datos=datos
                
            self.ignorar_senhales=True
            self.datosAventana()
            self.ignorar_senhales=False
                           
        except:
            if avisar:
                ad=adv('Formato incompatible.\nNo se pudo cargar los datos de la MSMN.')
                ad.exec_()
            self.ignorar_senhales=False
            self.reiniciar_por_codigo()
        
    def formatear_datos(self,datos): 
        # disposicion,carga,Nstubs
        # d1,l1
        # d2,l2
        # ...
        # dN,lN
        
        datos[0][2]=int(float(datos[0][2])) #Nstubs
        for i in range(1,datos[0][2]+1):
            datos[i][0]=int(float(datos[i][0])) #d
            datos[i][1]=int(float(datos[i][1])) #l
        
        return datos
        
    def guardar(self): 
        carpeta='./Datos/MSMN'
        ruta = QFileDialog.getSaveFileName(self.cvs,'Guardar archivo',carpeta,'*.msmn')[0]
        if ruta!='':
            if ruta[-5:] != '.msmn': ruta=ruta+'.msmn'
            with open(ruta,'w',newline='') as archivo:
                escritor = csv.writer(archivo)
                for fila in self.datos:
                    escritor.writerow(fila)
                    
    def reiniciar_por_codigo(self): 
        self.N_anterior=int(float(self.datos[0][2]))
        self.datos=self.plantilla_datos('Paralelo','Corto circuito',1)
        
        self.ignorar_senhales=True
        
        self.cvs.spnbx_parametrosstubs.blockSignals(True)
        self.cvs.spnbx_parametrosstubs.setValue(1)
        self.BorrarStubsLayout(self.cvs.spnbx_parametrosstubs.value()+1,self.N_anterior)
        self.N_anterior=self.cvs.spnbx_parametrosstubs.value()
        self.cvs.spnbx_parametrosstubs.blockSignals(False)
        
        self.cvs.cbx_dispostubs.setCurrentText('Paralelo')
        self.cvs.cbx_cargastubs.setCurrentText('Corto circuito')
        
        self.W['slider_d1'].blockSignals(True)
        self.W['linedit_d1'].blockSignals(True)
        self.W['slider_l1'].blockSignals(True)
        self.W['linedit_l1'].blockSignals(True)
        
        self.W['slider_d1'].setMinimum(0)
        self.W['slider_d1'].setMaximum(2)
        self.W['slider_d1'].setValue(1)
        self.W['slider_d1'].setStyleSheet(SS_slider_opaco)
        self.W['slider_d1'].setEnabled(False)
        self.W['linedit_d1'].setText('')
        
        self.W['slider_l1'].setMinimum(0)
        self.W['slider_l1'].setMaximum(2)
        self.W['slider_l1'].setValue(1)
        self.W['slider_l1'].setStyleSheet(SS_slider_opaco)
        self.W['slider_l1'].setEnabled(False)
        self.W['linedit_l1'].setText('')
        
        self.W['slider_d1'].blockSignals(False)
        self.W['linedit_d1'].blockSignals(False)
        self.W['slider_l1'].blockSignals(False)
        self.W['linedit_l1'].blockSignals(False)
        
        self.ignorar_senhales=False
        
    def clicked_reiniciar(self): 
        self.datos=self.plantilla_datos('Paralelo','Corto circuito',1)
        if self.cvs.bandera=='buscar': self.cvs.cvp.Buscadores[self.cvs.cbx_algoritmos.currentText()].datos=self.datos
        self.cvs.spnbx_parametrosstubs.setValue(1)
        self.cvs.cbx_dispostubs.setCurrentText('Paralelo')
        self.cvs.cbx_cargastubs.setCurrentText('Corto circuito')
        
        self.W['slider_d1'].setMinimum(0)
        self.W['slider_d1'].setMaximum(2)
        self.W['slider_d1'].setValue(1)
        self.W['slider_d1'].setStyleSheet(SS_slider_opaco)
        self.W['slider_d1'].setEnabled(False)
        self.W['linedit_d1'].setText('')
        
        self.W['slider_l1'].setMinimum(0)
        self.W['slider_l1'].setMaximum(2)
        self.W['slider_l1'].setValue(1)
        self.W['slider_l1'].setStyleSheet(SS_slider_opaco)
        self.W['slider_l1'].setEnabled(False)
        self.W['linedit_l1'].setText('')
        
    
    def BorrarStubsLayout(self,stub_i,stub_f): 
        if stub_f < stub_i : return
        
        hilo_borrar=BorrarStubs(self.cvs.layout_parametrosstubs,stub_i,stub_f)
        hilo_borrar.start()
        while not hilo_borrar.isFinished(): pass
        hilo_borrar.salir()
        hilo_borrar.deleteLater()
        
    def CrearWidgets(self,stub_i,stub_f): 
        for i in range(stub_i,stub_f+1):
            self.W['lbl_stub'+str(i)]=QLabel('Stub '+str(i)+':',alignment=Qt.AlignVCenter)
            self.W['lbl_stub'+str(i)].setFixedWidth(69)
            self.W['lbl_stub'+str(i)].setStyleSheet("""
                                                     color:rgb(238, 238, 238);
                                                     font: 75 10pt "MS Shell Dlg 2";
                                                    
                                                     border: 2px solid;
                                                     border-color:rgb(85,170,255);
                                                     border-radius: 10px;
                                                     padding-left: 5px;
                                                     padding-right: 5px;
                                                     """)
            self.W['lbl_d'+str(i)]=QLabel(' D'+str(i)+' (mm):',alignment=Qt.AlignRight)
            self.W['lbl_d'+str(i)].setStyleSheet(self.cvs.SS_lbl)
            #self.W['lbl_d'+str(i)].setFixedWidth(50)
            self.W['linedit_d'+str(i)]=QLineEdit()
            self.W['linedit_d'+str(i)].setFixedWidth(60)
            self.W['linedit_d'+str(i)].setStyleSheet(self.cvs.SS_linedit)
            self.W['lbl_l'+str(i)]=QLabel('  L'+str(i)+' (mm):',alignment=Qt.AlignRight)
            self.W['lbl_l'+str(i)].setStyleSheet(self.cvs.SS_lbl)
            #self.W['lbl_l'+str(i)].setFixedWidth(50)
            self.W['linedit_l'+str(i)]=QLineEdit()
            self.W['linedit_l'+str(i)].setFixedWidth(60)
            self.W['linedit_l'+str(i)].setStyleSheet(self.cvs.SS_linedit)
            self.W['linedit_d'+str(i)].setValidator(QIntValidator())
            self.W['linedit_l'+str(i)].setValidator(QIntValidator())
            self.W['slider_d'+str(i)]=QSlider(Qt.Horizontal)
            self.W['slider_d'+str(i)].setStyleSheet(SS_slider_opaco)
            self.W['slider_d'+str(i)].setEnabled(False)
            self.W['slider_d'+str(i)].setFixedWidth(120)
            self.W['slider_d'+str(i)].setFixedHeight(20)
            self.W['slider_d'+str(i)].setValue(50)
            self.W['slider_l'+str(i)]=QSlider(Qt.Horizontal)
            self.W['slider_l'+str(i)].setStyleSheet(SS_slider_opaco)
            self.W['slider_l'+str(i)].setEnabled(False)
            self.W['slider_l'+str(i)].setFixedWidth(120)
            self.W['slider_l'+str(i)].setFixedHeight(20)
            self.W['slider_l'+str(i)].setValue(50)
            
            self.cvs.layout_parametrosstubs.addWidget(self.W['lbl_stub'+str(i)],2*i-2,0)
            self.cvs.layout_parametrosstubs.addWidget(self.W['lbl_d'+str(i)],2*i-2,1)
            self.cvs.layout_parametrosstubs.addWidget(self.W['linedit_d'+str(i)],2*i-2,2)
            self.cvs.layout_parametrosstubs.addWidget(self.W['slider_d'+str(i)],2*i-2,3)
            self.cvs.layout_parametrosstubs.addWidget(self.W['lbl_l'+str(i)],2*i-1,1)
            self.cvs.layout_parametrosstubs.addWidget(self.W['linedit_l'+str(i)],2*i-1,2)
            self.cvs.layout_parametrosstubs.addWidget(self.W['slider_l'+str(i)],2*i-1,3)
            
            #Conexiones
            self.W['linedit_d'+str(i)].editingFinished.connect(partial(self.editing_finished,self.W['linedit_d'+str(i)],i,0))
            self.W['linedit_l'+str(i)].editingFinished.connect(partial(self.editing_finished,self.W['linedit_l'+str(i)],i,1))
            self.W['linedit_d'+str(i)].textChanged.connect(partial(self.text_changed,self.W['linedit_d'+str(i)],i,0))
            self.W['linedit_l'+str(i)].textChanged.connect(partial(self.text_changed,self.W['linedit_l'+str(i)],i,1))
            
            self.W['slider_d'+str(i)].valueChanged.connect(partial(self.slider_value_changed,self.W['slider_d'+str(i)],i,0))
            self.W['slider_l'+str(i)].valueChanged.connect(partial(self.slider_value_changed,self.W['slider_l'+str(i)],i,1))
            self.W['slider_d'+str(i)].sliderReleased.connect(self.slider_released)
            self.W['slider_l'+str(i)].sliderReleased.connect(self.slider_released)
            
        
    def accion_cbx_cargastubs(self): 
        if self.ignorar_senhales: return
        self.datos[0][1]=self.cvs.cbx_cargastubs.currentText()
        self.graficar()
        
    def accion_spnbx(self): 
        if self.ignorar_senhales: return
        
        self.datos[0][2]=self.cvs.spnbx_parametrosstubs.value()
        
        if (self.cvs.spnbx_parametrosstubs.value() < self.N_anterior):#Borrar lo que sobra
            
            self.cvs.spnbx_parametrosstubs.setEnabled(False)
            self.BorrarStubsLayout(self.cvs.spnbx_parametrosstubs.value()+1,self.N_anterior)
            self.datos=self.datos[0:self.cvs.spnbx_parametrosstubs.value()+1]
            try:
                if self.cvs.bandera=='buscar': 
                    self.cvs.cvp.Buscadores[self.cvs.cbx_algoritmos.currentText()].datos=self.datos
            except:
                pass
            
            try: self.determinar_posicion_entrada_adaptador()
            except: pass
        
            self.graficar()
            
            self.cvs.spnbx_parametrosstubs.setEnabled(True)
            
            
        elif (self.cvs.spnbx_parametrosstubs.value()>self.N_anterior):
            #Solo agregar los que hacen falta
            
            self.CrearWidgets(self.N_anterior+1,self.cvs.spnbx_parametrosstubs.value())
            for i in range(self.cvs.spnbx_parametrosstubs.value()-self.N_anterior): self.datos.append(['',''])
            self.NoGrafica()
                
        self.N_anterior=self.cvs.spnbx_parametrosstubs.value()
        
    def text_changed(self,linedit,fila,columna): 
        if self.ignorar_senhales:
            self.datos[fila][columna]=linedit.text()
        else:
            self.ignorar_senhales=True
            self.datos[fila][columna]=linedit.text()
            self.ignorar_senhales=False
            
        if columna==0: key='d'+str(fila)
        elif columna==1: key='l'+str(fila)
        
        if linedit.text()=='':
            self.bloquear_slider(self.W['slider_'+key])
            self.NoGrafica()
            
    def editing_finished(self,linedit,fila,columna): 
        if self.ignorar_senhales: return
        linedit.setCursorPosition(0)
        
        if columna==0: key='d'+str(fila)
        elif columna==1: key='l'+str(fila)
        
        try: 
            self.datos[fila][columna]=int(float(linedit.text()))
        except: 
            self.datos[fila][columna]=''
            
            self.bloquear_slider(self.W['slider_'+key])
            self.NoGrafica()
            return
        
        if self.datos[fila][columna] > 0:
            if key[0]=='d': self.determinar_posicion_entrada_adaptador()
            dol_min,dol_max = self.determinar_dol_min_max(self.datos[fila][columna])
                
            self.configurar_slider(self.W['slider_'+key],dol_min,self.datos[fila][columna],dol_max)
            self.graficar()
            
        else:            
            self.bloquear_slider(self.W['slider_'+key])
            self.NoGrafica()
                    
    def NoGrafica(self): 
        self.cvs.Cgrafica.ocultar()
        self.cvs.Cbarra.ocultar()
        self.cvs.pbtn_figuras_merito.hide()
        self.cvs.lbl_revisar_parametros.show()
        
    def bloquear_slider(self,slider): 
        slider.blockSignals(True)
        slider.setStyleSheet(SS_slider_opaco)
        slider.setEnabled(False)
        slider.setMinimum(0)
        slider.setMaximum(2)
        slider.setValue(1)
        slider.blockSignals(False)
        
    def configurar_slider(self,slider,dol_min,dol,dol_max): 
        slider.blockSignals(True)
        slider.setStyleSheet(SS_slider)
        slider.setEnabled(True)
        slider.setMinimum(dol_min)
        slider.setMaximum(dol_max)
        slider.setValue(dol)
        slider.blockSignals(False)
        
    def slider_value_changed(self,slider,fila,columna): 
        if columna==0: key='d'+str(fila)
        elif columna==1: key='l'+str(fila)
        
        self.W['linedit_'+key].setText(str(self.W['slider_'+key].value()))
        self.W['linedit_'+key].setCursorPosition(0)
        if not self.W['slider_'+key].isSliderDown(): 
            if key[0]=='d': self.determinar_posicion_entrada_adaptador()
            self.graficar()
    
    def slider_released(self): 
        self.determinar_posicion_entrada_adaptador()
        self.graficar() 
    
    def datosAventana(self): 
        # disposicion,carga,Nstubs
        # d1,l1
        # d2,l2
        # ...
        # dN,lN
        
        #Establecer disposicion, carga y Nstubs
        self.cvs.cbx_dispostubs.setCurrentText('Paralelo')
        self.cvs.cbx_cargastubs.setCurrentText(self.datos[0][1])
        N=int(float(self.datos[0][2]))
        self.cvs.spnbx_parametrosstubs.setValue(N)
        
        # Eliminar Widgets previos y crear los nuevos
        self.BorrarStubsLayout(1,self.N_anterior)
        self.CrearWidgets(1,N)
        self.N_anterior=N
        
        # Cargar los Widgets con la información
        for n in range(1,N+1):
            self.W['linedit_d'+str(n)].blockSignals(True)
            self.W['linedit_l'+str(n)].blockSignals(True)
            
            if self.datos[n][0]=='': 
                d=self.datos[n][0]
                self.W['linedit_d'+str(n)].setText(str(d))
            else: 
                d=int(float(self.datos[n][0]))
                d_min,d_max = self.determinar_dol_min_max(d)     
                self.configurar_slider(self.W['slider_d'+str(n)],d_min,d,d_max)
                self.W['linedit_d'+str(n)].setText(str(d))          
            
            if self.datos[n][1]=='': 
                l=self.datos[n][1]
                self.W['linedit_l'+str(n)].setText(str(l))
            else: 
                l=int(float(self.datos[n][1]))
                l_min,l_max = self.determinar_dol_min_max(l)                
                self.configurar_slider(self.W['slider_l'+str(n)],l_min,l,l_max)
                self.W['linedit_l'+str(n)].setText(str(l))
            
            self.W['linedit_d'+str(n)].blockSignals(False)
            self.W['linedit_l'+str(n)].blockSignals(False)
            
    ### Lógica de Cómputo
            
    def determinar_dol_min_max(self,dol): 
        if self.cvs.bandera=='buscar':
            if dol >= int(1 + self.intervalo/2):
                dol_min=dol-int(self.intervalo/2)
                dol_max=dol+int(self.intervalo/2)
            else:
                dol_min=1 # en mm
                dol_max=dol_min+self.intervalo

            return dol_min,dol_max

        elif self.cvs.bandera=='graficar':
            dol_min=round(dol*(1-self.ps/100))
            if dol_min<=0: dol_min=1
            dol_max=round(dol*(1+self.ps/100))
            
            return dol_min,dol_max
        
    def datos_correcto(self, advertir=True): 
        # disposicion,carga,Nstubs
        # d1,l1
        # d2,l2
        # ...
        # dN,lN
        
        try:
            
            if int(float(self.datos[0][2])) <= 0: # Nstubs
                if advertir:
                    ad=adv('La cantidad de stubs debe ser positiva.')
                    ad.exec()
                return False
            
            for i in range(1,int(float(self.datos[0][2]))+1):
                if int(float(self.datos[i][0])) <= 0: #d
                    if advertir:
                        ad=adv('Los valores de las distancias entre los stubs\deben ser positivas.')
                        ad.exec()
                    return False
                
                if int(float(self.datos[i][1])) <= 0: #l
                    if advertir:
                        ad=adv('Los valores de las longitudes de los stubs\deben ser positivas.')
                        ad.exec()
                    return False
        except:
            
            if advertir:
                ad=adv('Ingrese correctamente los parámetros\nde la MSMN.')
                ad.exec()
            return False
        
        return True
    
    def formato_correcto(self,datos): 
        # disposicion,carga,Nstubs
        # d1,l1
        # d2,l2
        # ...
        # dN,lN
        
        if datos[0][0]=='Paralelo':pass
        else: return False
        
        if datos[0][1]=='Corto circuito' or datos[0][1]=='Circuito abierto':pass
        else: return False
        
        N=int(float(datos[0][2]))
        if len(datos)!=(N+1): return False
        
        for i in range(1,N+1):
            if len(datos[i]) != 2: return False
        
        return True
        
    
    def graficar(self):    
        try:
            self.datos=self.formatear_datos(self.datos)
            if self.cvs.bandera=='buscar': self.cvs.cvp.Buscadores[self.cvs.cbx_algoritmos.currentText()].datos=self.datos
            
            if self.cvs.bandera=='buscar':
                nombre=self.cvs.cbx_algoritmos.currentText()
                Pmax=float(self.cvs.Clinea.datos[1][1])
                DCA=int(float(self.cvs.Clinea.datos[3][0]))
                DGA=int(float(self.cvs.Clinea.datos[3][1]))
                
                self.cvs.cvp.Buscadores[nombre].datos=self.datos
                self.determinar_posicion_entrada_adaptador()
                self.cvs.cvp.Buscadores[nombre].posicion=self.cvs.cvp.Buscadores[nombre].posicion_entrada_adaptador
                self.cvs.cvp.Buscadores[nombre].vectorD=vectordistancias(self.cvs.cvp.Buscadores[nombre].datos,DCA,DGA)
                self.cvs.Cbarra.configurar(self.cvs.cvp.Buscadores[nombre].vectorD,self.cvs.cvp.Buscadores[nombre].posicion_entrada_adaptador) 
                self.cvs.cvp.Buscadores[nombre].Zins=self.calcularZins(self.cvs.Fvisual,self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc)
                
                self.cvs.cvp.Buscadores[nombre].crear_grafica(self.cvs.cbx_tipografica.currentText(),
                                                              self.cvs.cbx_presentaciongrafica.currentText(),
                                                              self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                                              self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                                              self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                              self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                              self.cvs.Cbarra.posicion)
                      
                self.cvs.Cgrafica.borrar()
                self.cvs.Cgrafica.graficar()
                if self.cvs.cbx_tipografica.currentText()=='Respuesta en frecuencia': self.cvs.Cbarra.ocultar()
                else: self.cvs.Cbarra.mostrar()
                self.cvs.pbtn_figuras_merito.show()
                
            elif self.cvs.bandera=='graficar':
                Pmax=float(self.cvs.Clinea.datos[1][1])
                DCA=int(float(self.cvs.Clinea.datos[3][0]))
                DGA=int(float(self.cvs.Clinea.datos[3][1]))
                
                self.determinar_posicion_entrada_adaptador()
                self.cvs.posicion=self.cvs.posicion_entrada_adaptador
                self.cvs.vectorD=vectordistancias(self.datos,DCA,DGA)
                self.cvs.Cbarra.configurar(self.cvs.vectorD,self.cvs.posicion_entrada_adaptador)
                self.Zins=self.calcularZins(self.cvs.Fvisual,self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc)
                
                self.cvs.crear_grafica(self.cvs.cbx_tipografica.currentText(),
                                       self.cvs.cbx_presentaciongrafica.currentText(),
                                       self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                       self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                       self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                       self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                       self.cvs.Cbarra.posicion)
                
                self.cvs.Cgrafica.borrar()
                self.cvs.Cgrafica.graficar()
                if self.cvs.cbx_tipografica.currentText()=='Respuesta en frecuencia': self.cvs.Cbarra.ocultar()
                else: self.cvs.Cbarra.mostrar()
                self.cvs.pbtn_figuras_merito.show()
            
            self.cvs.lbl_revisar_parametros.hide()
        except:
            # traceback.print_exc()
            self.NoGrafica()

        
    def calcularZins(self,F,Alfa,Beta,Zc): 
        j=complex(0+1j)
        Zins=dict()
        for i in range(1,self.cvs.spnbx_parametrosstubs.value()+1):
            Zins['stub'+str(i)]=[]
            for indf in range(0,len(F)):
                if self.cvs.cbx_cargastubs.currentText()=='Corto circuito':
                    Zins['stub'+str(i)].append(Zc[indf]*complextanh((Alfa[indf]+j*Beta[indf])*int(float(self.datos[i][1]))*10**(-3)))
                elif self.cvs.cbx_cargastubs.currentText()=='Circuito abierto':
                    Zins['stub'+str(i)].append(Zc[indf]/complextanh((Alfa[indf]+j*Beta[indf])*int(float(self.datos[i][1]))*10**(-3)))  
        return Zins
                    
    
    def determinar_posicion_entrada_adaptador(self):
        if not self.datos_correcto(advertir=False): return
        
        DCA=self.cvs.Clinea.datos[3][0]
        acum=int(float(DCA))
        for i in range(1,len(self.datos)):
            acum+=int(float(self.datos[i][0]))
            
        if self.cvs.bandera=='buscar':
            self.cvs.cvp.Buscadores[self.cvs.cbx_algoritmos.currentText()].posicion_entrada_adaptador=acum
        elif self.cvs.bandera=='graficar':
            self.cvs.posicion_entrada_adaptador=acum       
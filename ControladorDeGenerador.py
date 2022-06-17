# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

from PyQt5.QtGui import QDoubleValidator
import os.path
import csv
from PyQt5.QtWidgets import QFileDialog,QMainWindow,QLineEdit,QLabel,QComboBox
from Advertencia import adv       
from ventana_generador_ui import Ui_MainWindow as VentanaGenerador
from PyQt5.QtCore import Qt
from numpy import Infinity
from PyQt5.QtCore import QThread
from functools import partial
from PyQt5.QtGui import QPixmap
from Funciones import ZCARGA,FUENTE
from math import sqrt
from cmath import tanh as complextanh

class BorrarFilas(QThread):

    def __init__(self,layout,fi=None,ff=None):
        QThread.__init__(self)
        
        self.layout=layout
        
        if fi is None: self.fi=1
        else: self.fi=fi
        
        if ff is None: self.ff=self.layout.rowCount()
        else: self.ff=ff
        
    def run(self):
        for i in range(self.fi,self.ff+1):
            for j in range(self.layout.columnCount()): 
                try:
                    self.layout.itemAtPosition(i-1,j).widget().deleteLater()
                except:
                    pass
            
    def salir(self):
        self.exit()  
        
class EliminarDiccionarioDeWidgets(QThread):

    def __init__(self,dic):
        QThread.__init__(self)
        self.dic=dic
        
    def run(self):
        for nombre in self.dic: 
            try:
                self.dic[nombre].deleteLater()
            except:
                pass
        
    def salir(self):
        self.exit()
        

class ControladorDeGenerador(QMainWindow,VentanaGenerador):
    def __init__(self,ventana_principal):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setWindowTitle('Configurar generador')
        
        self.cvp=ventana_principal
        
        ### Fuente
        self.SS_cbx_fuente="""
                            QComboBox {
                                border:1px solid rgb(0, 0, 0);
                               	border-radius: 10px;
                            	color:rgb(238, 238, 238);
                            	font: 75 10pt "MS Shell Dlg 2";
                            	background-color: rgb(49, 58, 67);
                            
                                padding-left: 6px;
                               /* min-width: 6em;*/
                            }
                            QComboBox:hover{
                            	border: 1px solid rgb(85,170,255);
                            }
                            QComboBox:focus{
                            	border: 1px solid rgb(85,170,255);
                            }
                            
                            QComboBox::drop-down {    
                                border-left-width: 0px;
                                border-left-color: black;
                                border-left-style: solid; 
                            	width:0px;
                            }
                            
                            QComboBox QAbstractItemView {
                                selection-background-color: rgb(85,170,255);
                            	selection-color: black;
                            	color: rgb(238, 238, 238);
                            	background-color: rgb(79, 93, 108);
                            }
        
                            """
        
        self.layout_fuente.setAlignment(Qt.AlignTop)
        
        self.WF=dict() # diccionario de widgets de la fuente
        self.WF['lbl_s1']=self.lbl_s1
        self.WF['linedit_s1']=self.linedit_s1
        self.WF['cbx_s1']=self.cbx_s1
        self.WF['lbl_s2']=self.lbl_s2
        self.WF['linedit_s2']=self.linedit_s2
        self.WF['cbx_s2']=self.cbx_s2
        self.WF['lbl_f1']=self.lbl_f1
        self.WF['linedit_f1']=self.linedit_f1
        self.WF['cbx_f1']=self.cbx_f1
        self.WF['lbl_f2']=self.lbl_f2
        self.WF['linedit_f2']=self.linedit_f2
        self.WF['cbx_f2']=self.cbx_f2
        
        self.datos_fuente=self.plantilla_datos_fuente()
        self.Nanterior=2
        self.ignorar_senhales_fuente=False
        self.Voltaje=[]
        self.Voltaje_original=[]
        
        self.fmin_fuente=None
        self.fmax_fuente=None
        
        self.WF['linedit_s1'].setValidator(QDoubleValidator())
        self.WF['linedit_s2'].setValidator(QDoubleValidator())
        self.WF['linedit_f1'].setValidator(QDoubleValidator())
        self.WF['linedit_f2'].setValidator(QDoubleValidator())
        
        self.tltp_v='Amplitud del voltaje\nincidente a la entrada de la\nlínea de transmisión cuando\nesta se encuentra adaptada\ncon la impedancia del generador.'
        self.tltp_p='Potencia activa promedio\nincidente a la entrada de la\nlínea de transmisión cuando\nesta se encuentra adaptada\ncon la impedancia del generador.'
        
        ### Impedancia
        self.layout_impedancia.setAlignment(Qt.AlignTop)
        self.lbl_importado.hide()
        self.WI=dict() # diccionario de los widgets de impedancia
        self.WI['lbl_R']=self.lbl_R
        self.WI['linedit_R']=self.linedit_R
        self.WI['linedit_R'].setValidator(QDoubleValidator())
        self.WI['linedit_R'].setAlignment(Qt.AlignLeft)
        self.WI['lbl_R'].setAlignment(Qt.AlignRight)
        self.WI['cbx_R']=self.cbx_R
        self.WI['cbx_R'].setCurrentText('Ω')
        
        self.Impedancia=[]
        self.ImpedanciaPrima=[]
        self.Impedancia_original=[]
        self.fmin_impedancia=None
        self.fmax_impedancia=None
        self.datos_impedancia=self.plantilla_datos_impedancia()
        self.ignorar_senhales_impedancia=False

        ### Conexiones
        self.pbtn_ok.clicked.connect(self.salir)
        self.actionReiniciar.triggered.connect(self.reiniciar)
        
        ### Fuente
        self.WF['linedit_s1'].editingFinished.connect(partial(self.editing_finished_fuente,'s1',1,0))
        self.WF['cbx_s1'].currentTextChanged.connect(partial(self.accion_cbx_unidades_fuente,'s1',1,0))
        self.WF['linedit_f1'].editingFinished.connect(partial(self.editing_finished_fuente,'f1',1,1))
        self.WF['cbx_f1'].currentTextChanged.connect(partial(self.accion_cbx_unidades_fuente,'f1',1,1))
        self.WF['linedit_s2'].editingFinished.connect(partial(self.editing_finished_fuente,'s2',2,0))
        self.WF['cbx_s2'].currentTextChanged.connect(partial(self.accion_cbx_unidades_fuente,'s2',2,0))
        self.WF['linedit_f2'].editingFinished.connect(partial(self.editing_finished_fuente,'f2',2,1))
        self.WF['cbx_f2'].currentTextChanged.connect(partial(self.accion_cbx_unidades_fuente,'f2',2,1))
        self.cbx_fuente.currentTextChanged.connect(self.accion_cbx_fuente)
        self.spnbx_mediciones.valueChanged.connect(self.accion_spnbx_mediciones)
        self.actionCargarFuente.triggered.connect(self.cargar_fuente)
        self.actionGuardarFuente.triggered.connect(self.guardar_fuente)
        self.WF['linedit_s1'].textChanged.connect(partial(self.text_changed_fuente,self.WF['linedit_s1'],1,0))
        self.WF['linedit_f1'].textChanged.connect(partial(self.text_changed_fuente,self.WF['linedit_f1'],1,1))
        self.WF['linedit_s2'].textChanged.connect(partial(self.text_changed_fuente,self.WF['linedit_s2'],2,0))
        self.WF['linedit_f2'].textChanged.connect(partial(self.text_changed_fuente,self.WF['linedit_f2'],2,1))
        
        ### Impedancia
        self.linedit_R.editingFinished.connect(partial(self.editing_finished_impedancia,'R',2,0))
        self.linedit_R.textChanged.connect(partial(self.text_changed_impedancia,self.linedit_R,2,0))
        self.cbx_modelo.currentTextChanged.connect(self.accionmodelo_impedancia)
        self.actionCargarModelo.triggered.connect(self.cargar_modelo_impedancia)
        self.actionCargarArchivo_imp.triggered.connect(self.cargar_archivo_imp_impedancia)
        self.actionGuardarModelo.triggered.connect(self.guardar_modelo_impedancia)

       
    ### Lógica de Interfaz Grafica     
    def closeEvent(self, event): 
        self.salir()
        
    def salir(self): 
        self.hide()
        self.cvp.pbtn_configurar_generador.setEnabled(True)
        
    def bloquear(self):
        self.cvp.pbtn_configurar_generador.setEnabled(False)
        self.hide()
        
    def desbloquear(self):
        self.cvp.pbtn_configurar_generador.setEnabled(True)
        
    def reiniciar(self):
        self.reiniciar_fuente()
        self.reiniciar_impedancia()
            
    ### Fuente    
    def plantilla_datos_fuente(self,tipo='Voltaje',Nmed=2): 
        # Potencia/Voltaje,Nmed        
        # P1/V1,f1
        # P2/V2,f2
        # ...
        # PN/VN,fN
        # fmin,fmax
        
        datos=[[tipo,Nmed]]
        for i in range(Nmed): datos.append(['',''])
        datos.append([0,Infinity])
            
        return datos
    
    def cargar_fuente(self): 
        try:
            carpeta='./Datos/Generador'
            ruta = QFileDialog.getOpenFileName(self, 'Cargar archivo',carpeta,"*.source")[0]
            if os.path.exists(ruta):
                datos=[]
                with open(ruta) as archivo:
                    lector = csv.reader(archivo, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    for fila in lector: datos.append(fila) 
                
                if self.formato_correcto_fuente(datos): pass
                else: raise Exception
                
                self.datos_fuente=datos                
                self.determinar_fmin_fmax_datos_fuente()
                    
                self.ignorar_senhales_fuente=True
                self.datosAventana_fuente()
                self.ignorar_senhales_fuente=False
                           
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos.')
            ad.exec_()
            self.ignorar_senhales_fuente=False
            self.reiniciar_fuente()
            
    def cargar_datos_fuente(self,datos): 
        try: 
            if self.formato_correcto_fuente(datos): pass
            else: raise Exception
            
            self.datos_fuente=datos                
            self.determinar_fmin_fmax_datos_fuente()
                
            self.ignorar_senhales_fuente=True
            self.datosAventana_fuente()
            self.ignorar_senhales_fuente=False
                           
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos de\nla fuente.')
            ad.exec_()
            self.ignorar_senhales_fuente=False
            self.reiniciar_fuente()
        
    def formatear_datos_fuente(self,datos): 
        # Potencia/Voltaje,Nmed        
        # P1/V1,f1
        # P2/V2,f2
        # ...
        # PN/VN,fN
        # fmin,fmax
        
        datos[0][1]=int(float(datos[0][1])) #Nmed
        for i in range(1,datos[0][1]+1):
            datos[i][0]=float(datos[i][0]) #P/V
            datos[i][1]=float(datos[i][1]) #f
            
        datos[-1][0]=float(datos[-1][0]) #fmin
        datos[-1][1]=float(datos[-1][1]) #fmax
        
        return datos
        
    def guardar_fuente(self): 
        carpeta='./Datos/Generador'
        ruta = QFileDialog.getSaveFileName(self,'Guardar archivo',carpeta,'*.source')[0]
        if ruta!='':
            if ruta[-7:] != '.source': ruta=ruta+'.source'
            with open(ruta,'w',newline='') as archivo:
                escritor = csv.writer(archivo)
                for fila in self.datos_fuente:
                    escritor.writerow(fila)
                    
    def reiniciar_fuente(self): 
        self.spnbx_mediciones.setValue(2)
        self.datos_fuente=self.plantilla_datos_fuente()
        self.cbx_fuente.setCurrentText('Voltaje')
        self.WF['linedit_s1'].setText('')
        self.WF['cbx_s1'].setCurrentIndex(1)
        self.WF['linedit_s2'].setText('')
        self.WF['cbx_s2'].setCurrentIndex(1)
        self.WF['linedit_f1'].setText('')
        self.WF['cbx_f1'].setCurrentIndex(1)
        self.WF['linedit_f2'].setText('')
        self.WF['cbx_f2'].setCurrentIndex(1)
        
    def borrar_filas(self,fi=None,ff=None): 
        hilo_borrar=BorrarFilas(self.layout_fuente,fi,ff)
        hilo_borrar.start()
        while not hilo_borrar.isFinished(): pass
        hilo_borrar.salir()
        hilo_borrar.deleteLater()
        
    def CrearWidgets_fuente(self,fi,ff): 
        for i in range(fi,ff+1):
            if self.cbx_fuente.currentText()=='Potencia':
                self.WF['lbl_s'+str(i)]=QLabel('Pin:',alignment=Qt.AlignRight)
                self.WF['lbl_s'+str(i)].setMinimumWidth(26)
                self.WF['lbl_s'+str(i)].setStyleSheet(self.cvp.SS_lbl)
                self.WF['lbl_s'+str(i)].setToolTip(self.tltp_p)
                self.WF['linedit_s'+str(i)]=QLineEdit()
                self.WF['linedit_s'+str(i)].setMinimumWidth(65)
                self.WF['linedit_s'+str(i)].setMaximumWidth(65)
                self.WF['linedit_s'+str(i)].setValidator(QDoubleValidator())
                self.WF['linedit_s'+str(i)].setStyleSheet(self.cvp.SS_linedit)
                self.WF['cbx_s'+str(i)]=QComboBox()
                self.WF['cbx_s'+str(i)].setMinimumWidth(40)
                self.WF['cbx_s'+str(i)].addItem('kW')
                self.WF['cbx_s'+str(i)].addItem('W')
                self.WF['cbx_s'+str(i)].addItem('mW')
                self.WF['cbx_s'+str(i)].setCurrentIndex(1)
                self.WF['cbx_s'+str(i)].setStyleSheet(self.SS_cbx_fuente)
                
            elif self.cbx_fuente.currentText()=='Voltaje':
                self.WF['lbl_s'+str(i)]=QLabel('|Vin|:',alignment=Qt.AlignRight)
                self.WF['lbl_s'+str(i)].setStyleSheet(self.cvp.SS_lbl)
                self.WF['lbl_s'+str(i)].setToolTip(self.tltp_v)
                self.WF['linedit_s'+str(i)]=QLineEdit()
                self.WF['linedit_s'+str(i)].setMinimumWidth(65)
                self.WF['linedit_s'+str(i)].setMaximumWidth(65)
                self.WF['linedit_s'+str(i)].setValidator(QDoubleValidator())
                self.WF['linedit_s'+str(i)].setStyleSheet(self.cvp.SS_linedit)
                self.WF['cbx_s'+str(i)]=QComboBox()
                self.WF['cbx_s'+str(i)].setMinimumWidth(40)
                self.WF['cbx_s'+str(i)].addItem('kV')
                self.WF['cbx_s'+str(i)].addItem('V')
                self.WF['cbx_s'+str(i)].addItem('mV')
                self.WF['cbx_s'+str(i)].addItem('μV')
                self.WF['cbx_s'+str(i)].addItem('nV')
                self.WF['cbx_s'+str(i)].addItem('pV')
                self.WF['cbx_s'+str(i)].setCurrentIndex(1)
                self.WF['cbx_s'+str(i)].setStyleSheet(self.SS_cbx_fuente)
            
            self.WF['lbl_f'+str(i)]=QLabel('@f:',alignment=Qt.AlignRight)
            self.WF['lbl_f'+str(i)].setStyleSheet(self.cvp.SS_lbl)
            self.WF['linedit_f'+str(i)]=QLineEdit()
            self.WF['linedit_f'+str(i)].setMinimumWidth(65)
            self.WF['linedit_f'+str(i)].setMaximumWidth(65)
            self.WF['linedit_f'+str(i)].setValidator(QDoubleValidator())
            self.WF['linedit_f'+str(i)].setStyleSheet(self.cvp.SS_linedit)
            self.WF['cbx_f'+str(i)]=QComboBox()
            self.WF['cbx_f'+str(i)].setMinimumWidth(40)
            self.WF['cbx_f'+str(i)].addItem('GHz')
            self.WF['cbx_f'+str(i)].addItem('MHz')
            self.WF['cbx_f'+str(i)].addItem('kHz')
            self.WF['cbx_f'+str(i)].setCurrentIndex(1)
            self.WF['cbx_f'+str(i)].setStyleSheet(self.SS_cbx_fuente)
            
            self.WF['linedit_s'+str(i)].editingFinished.connect(partial(self.editing_finished_fuente,'s'+str(i),i,0))
            self.WF['linedit_f'+str(i)].editingFinished.connect(partial(self.editing_finished_fuente,'f'+str(i),i,1))
            self.WF['linedit_s'+str(i)].textChanged.connect(partial(self.text_changed_fuente,self.WF['linedit_s'+str(i)],i,0))
            self.WF['linedit_f'+str(i)].textChanged.connect(partial(self.text_changed_fuente,self.WF['linedit_f'+str(i)],i,1))
            self.WF['cbx_s'+str(i)].currentTextChanged.connect(partial(self.accion_cbx_unidades_fuente,'s'+str(i),i,0))
            self.WF['cbx_f'+str(i)].currentTextChanged.connect(partial(self.accion_cbx_unidades_fuente,'f'+str(i),i,1))
            
            self.layout_fuente.addWidget(self.WF['lbl_s'+str(i)],i-1,0)
            self.layout_fuente.addWidget(self.WF['linedit_s'+str(i)],i-1,1)
            self.layout_fuente.addWidget(self.WF['cbx_s'+str(i)],i-1,2)
            self.layout_fuente.addWidget(self.WF['lbl_f'+str(i)],i-1,3)
            self.layout_fuente.addWidget(self.WF['linedit_f'+str(i)],i-1,4)
            self.layout_fuente.addWidget(self.WF['cbx_f'+str(i)],i-1,5)
            
    def accion_cbx_fuente(self): 
        if self.ignorar_senhales_fuente: return
        
        self.datos_fuente[0][0]=self.cbx_fuente.currentText()
        
        if self.cbx_fuente.currentText()=='Potencia':
            for i in range(1,self.spnbx_mediciones.value()+1):
                self.WF['lbl_s'+str(i)].setText('Pin:')
                self.WF['lbl_s'+str(i)].setMinimumWidth(26)
                self.WF['lbl_s'+str(i)].setToolTip(self.tltp_p)
                self.WF['linedit_s'+str(i)].setText('')
                self.WF['cbx_s'+str(i)].clear()
                self.WF['cbx_s'+str(i)].addItem('kW')
                self.WF['cbx_s'+str(i)].addItem('W')
                self.WF['cbx_s'+str(i)].addItem('mW')
                self.WF['cbx_s'+str(i)].setCurrentIndex(1)
                self.datos_fuente[i][0]='' #P
                
        elif self.cbx_fuente.currentText()=='Voltaje':
            for i in range(1,self.spnbx_mediciones.value()+1):
                self.WF['lbl_s'+str(i)].setText('|Vin|:')
                self.WF['lbl_s'+str(i)].setToolTip(self.tltp_v)
                self.WF['linedit_s'+str(i)].setText('')
                self.WF['cbx_s'+str(i)].clear()
                self.WF['cbx_s'+str(i)].addItem('kV')
                self.WF['cbx_s'+str(i)].addItem('V')
                self.WF['cbx_s'+str(i)].addItem('mV')
                self.WF['cbx_s'+str(i)].addItem('μV')
                self.WF['cbx_s'+str(i)].addItem('nV')
                self.WF['cbx_s'+str(i)].addItem('pV')
                self.WF['cbx_s'+str(i)].setCurrentIndex(1)               
                self.datos_fuente[i][0]='' #V
        
    def accion_spnbx_mediciones(self): 
        if self.ignorar_senhales_fuente: return
        
        if (self.spnbx_mediciones.value() < self.Nanterior):
            #Borrar lo que sobra
            self.borrar_filas(self.spnbx_mediciones.value()+1,self.Nanterior)
            delta=self.Nanterior-self.spnbx_mediciones.value()
            for i in range(delta): del self.datos_fuente[-2]
            self.datos_fuente[0][1]=self.spnbx_mediciones.value()
                
        elif (self.spnbx_mediciones.value()>self.Nanterior):
            #Solo agregar los que hacen falta
            self.CrearWidgets_fuente(self.Nanterior+1,self.spnbx_mediciones.value())
            for i in range(self.Nanterior+1,self.spnbx_mediciones.value()+1): self.datos_fuente.insert(i,['',''])
            self.datos_fuente[0][1]=self.spnbx_mediciones.value()
            
        self.Nanterior=self.spnbx_mediciones.value()
        
    def accion_cbx_unidades_fuente(self,key,fila,columna): 
        if self.ignorar_senhales_fuente: return
        
        if key[0]=='s':
            if self.cbx_fuente.currentText()=='Potencia':
                if self.WF['cbx_'+key].currentText()=='kW': mult=1e3
                elif self.WF['cbx_'+key].currentText()=='W': mult=1
                elif self.WF['cbx_'+key].currentText()=='mW': mult=1e-3
                try: self.datos_fuente[fila][columna]=float(self.WF['linedit_'+key].text())*mult
                except: pass
            
            elif self.cbx_fuente.currentText()=='Voltaje':
                if self.WF['cbx_'+key].currentText()=='kV': mult=1e3
                elif self.WF['cbx_'+key].currentText()=='V': mult=1
                elif self.WF['cbx_'+key].currentText()=='mV': mult=1e-3
                elif self.WF['cbx_'+key].currentText()=='μV': mult=1e-6
                elif self.WF['cbx_'+key].currentText()=='nV': mult=1e-9
                elif self.WF['cbx_'+key].currentText()=='pV': mult=1e-12
                try: self.datos_fuente[fila][columna]=float(self.WF['linedit_'+key].text())*mult
                except: pass
            
        if key[0]=='f':
            if self.WF['cbx_'+key].currentText()=='GHz': mult=1e3
            elif self.WF['cbx_'+key].currentText()=='MHz': mult=1
            elif self.WF['cbx_'+key].currentText()=='kHz': mult=1e-3
            try: self.datos_fuente[fila][columna]=float(self.WF['linedit_'+key].text())*mult
            except: pass
        
    def text_changed_fuente(self,linedit,fila,columna):
        if self.ignorar_senhales_fuente:
            self.datos_fuente[fila][columna]=linedit.text()
        else:
            self.ignorar_senhales_fuente=True
            self.datos_fuente[fila][columna]=linedit.text()
            self.ignorar_senhales_fuente=False
        
    def editing_finished_fuente(self,key,fila,columna): 
        if self.ignorar_senhales_fuente: return
        self.WF['linedit_'+key].setCursorPosition(0)
        try: self.datos_fuente[fila][columna]=float(self.WF['linedit_'+key].text())*self.multiplicador_fuente(key)
        except: pass
        
    def multiplicador_fuente(self,key): 
        if key[0]=='s':
            if self.cbx_fuente.currentText()=='Potencia':
                if self.WF['cbx_'+key].currentText()=='kW': mult=1e3
                elif self.WF['cbx_'+key].currentText()=='W': mult=1
                elif self.WF['cbx_'+key].currentText()=='mW': mult=1e-3
            
            elif self.cbx_fuente.currentText()=='Voltaje':
                if self.WF['cbx_'+key].currentText()=='kV': mult=1e3
                elif self.WF['cbx_'+key].currentText()=='V': mult=1
                elif self.WF['cbx_'+key].currentText()=='mV': mult=1e-3
                elif self.WF['cbx_'+key].currentText()=='μV': mult=1e-6
                elif self.WF['cbx_'+key].currentText()=='nV': mult=1e-9
                elif self.WF['cbx_'+key].currentText()=='pV': mult=1e-12
            
        if key[0]=='f':
            if self.WF['cbx_'+key].currentText()=='GHz': mult=1e3
            elif self.WF['cbx_'+key].currentText()=='MHz': mult=1
            elif self.WF['cbx_'+key].currentText()=='kHz': mult=1e-3
            
        return mult
        
    def datosAventana_fuente(self):
        # Establecer el tipo y numero
        self.cbx_fuente.setCurrentText(self.datos_fuente[0][0])
        self.spnbx_mediciones.setValue(int(float(self.datos_fuente[0][1])))
        
        # Eliminar Widgets previos y crear los nuevos
        self.borrar_filas()
        self.CrearWidgets_fuente(1,int(float(self.datos_fuente[0][1])))
        self.Nanterior=int(float(self.datos_fuente[0][1]))
        
        # Cargar los Widgets con la información
        for i in range(1,int(float(self.datos_fuente[0][1]))+1):
            self.WF['linedit_s'+str(i)].setText(str(self.datos_fuente[i][0])) #P/V
            self.WF['linedit_f'+str(i)].setText(str(self.datos_fuente[i][1])) #f
            self.WF['linedit_s'+str(i)].setCursorPosition(0)
            self.WF['linedit_f'+str(i)].setCursorPosition(0)
        
        
    ### Impedancia
    def plantilla_datos_impedancia(self,tipo='Modelo',n=None,modelo='R'): 
        
        if tipo=='Modelo':
            if (modelo=='R')or(modelo=='L')or(modelo=='C'):
                # tipo:modelo,n
                # modelo:R
                # R
                # fmin,fmax
                
                n=3
                datos=[[tipo,n]]
                datos.append([modelo])
                datos.append([''])
                datos.append([0,Infinity])
                
            elif (modelo=='R-s-L')or(modelo=='R-p-L')or(
                    modelo=='R-s-C')or(modelo=='R-p-C')or(
                        modelo=='L-s-C')or(modelo=='L-p-C'):
                            # tipo:modelo,n
                            # modelo:R-s-L
                            # R
                            # L
                            # fmin,fmax
                            
                            n=4
                            datos=[[tipo,n]]
                            datos.append([modelo])
                            datos.append([''])
                            datos.append([''])
                            datos.append([0,Infinity])
    
            elif (modelo=='R-s-L-s-C')or(modelo=='R-p-L-p-C')or(
                    modelo=='R-s-(L-p-C)')or(modelo=='R-p-(L-s-C)')or(
                        modelo=='L-s-(R-p-C)')or(modelo=='L-p-(R-s-C)')or(
                            modelo=='C-s-(R-p-L)')or(modelo=='C-p-(R-s-L)'):
                                # tipo:modelo,n
                                # modelo:R-s-L-s-C
                                # R
                                # L
                                # C
                                # fmin,fmax
                                
                                n=5
                                datos=[[tipo,n]]
                                datos.append([modelo])
                                datos.append([''])
                                datos.append([''])
                                datos.append([''])
                                datos.append([0,Infinity])
            
            elif modelo=='Antena Microstrip':
                # tipo:modelo,n
                # modelo:Antena Microstrip
                # L1
                # C1
                # R
                # L
                # C
                # fmin,fmax
                
                n=7
                datos=[[tipo,n]]
                datos.append([modelo])
                datos.append([''])
                datos.append([''])
                datos.append([''])
                datos.append([''])
                datos.append([''])
                datos.append([0,Infinity])
                
        elif tipo=='Archivo':
            # tipo:Archivo,n
            # f1,r1,x1
            # f2,r2,x2
            # ...
            # fn,rn,xn
            # fmin,fmax
            
            datos=[[tipo,n]]
            for i in range(n): datos.append(['','',''])
            datos.append(['',''])
            
        return datos
                
    def cargar_modelo_impedancia(self): 
        try:
            carpeta='./Datos/Generador'
            ruta = QFileDialog.getOpenFileName(self, 'Cargar archivo',carpeta,"*.modelimp")[0]
            if os.path.exists(ruta):
                datos=[]
                with open(ruta) as archivo:
                    lector = csv.reader(archivo, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    for fila in lector: datos.append(fila) 
                
                if self.formato_correcto_impedancia(datos): pass
                else: raise Exception
                
                self.datos_impedancia=datos                
                self.determinar_fmin_fmax_datos_impedancia()
                    
                self.ignorar_senhales_impedancia=True
                self.datosAventana_impedancia()
                self.ignorar_senhales_impedancia=False
                           
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos.')
            ad.exec_()
            self.ignorar_senhales_impedancia=False
            self.reiniciar_impedancia()
            
    def cargar_archivo_imp_impedancia(self): 
        try:
            carpeta='./Datos/Generador'
            ruta = QFileDialog.getOpenFileName(self, 'Cargar archivo',carpeta,"*.imp")[0]
            if os.path.exists(ruta):
                archivo_imp=[]
                with open(ruta) as archivo:
                    lector = csv.reader(archivo, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    for fila in lector: archivo_imp.append(fila)

                if self.formato_correcto_impedancia(archivo_imp): pass
                else: raise Exception
                
                self.datos_impedancia=archivo_imp 
                self.determinar_fmin_fmax_datos_impedancia()
                            
                self.ignorar_senhales_impedancia=True
                self.datosAventana_impedancia()
                self.ignorar_senhales_impedancia=False
                
                self.WI['linedit_R'].setEnabled(False)
                self.WI['cbx_R'].setEnabled(False)
                           
        except:
            import traceback
            traceback.print_exc()
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos.')
            ad.exec_()
            self.ignorar_senhales_impedancia=False
            self.WI['linedit_R'].setEnabled(True)
            self.WI['cbx_R'].setEnabled(True)
            self.reiniciar_impedancia()
            
    def cargar_datos_impedancia(self,datos): 
        try:
            if self.formato_correcto_impedancia(datos): pass
            else: raise Exception
            
            self.datos_impedancia=datos                
            self.determinar_fmin_fmax_datos_impedancia()
                
            self.ignorar_senhales_impedancia=True
            self.datosAventana_impedancia()
            self.ignorar_senhales_impedancia=False
                           
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos de\nla impedancia del generador.')
            ad.exec_()
            self.ignorar_senhales_impedancia=False
            self.reiniciar_impedancia()
    
    def formatear_datos_impedancia(self,datos): 
        tipo=datos[0][0]
        n=int(float(datos[0][1]))
        datos[0][1]=n
        
        if tipo=='Modelo':
            modelo=datos[1][0]
            
            if (modelo=='R')or(modelo=='L')or(modelo=='C'):
                # tipo:modelo,n
                # modelo:R
                # R
                # fmin,fmax
                
                datos[2][0]=float(datos[2][0]) #R
                datos[3][0]=float(datos[3][0]) #fmin
                datos[3][1]=float(datos[3][1]) #fmax
                
            elif (modelo=='R-s-L')or(modelo=='R-p-L')or(
                    modelo=='R-s-C')or(modelo=='R-p-C')or(
                        modelo=='L-s-C')or(modelo=='L-p-C'):
                            # tipo:modelo,n
                            # modelo:R-s-L
                            # R
                            # L
                            # fmin,fmax
                            
                            datos[2][0]=float(datos[2][0]) #R
                            datos[3][0]=float(datos[3][0]) #L
                            datos[4][0]=float(datos[4][0]) #fmin
                            datos[4][1]=float(datos[4][1]) #fmax
    
            elif (modelo=='R-s-L-s-C')or(modelo=='R-p-L-p-C')or(
                    modelo=='R-s-(L-p-C)')or(modelo=='R-p-(L-s-C)')or(
                        modelo=='L-s-(R-p-C)')or(modelo=='L-p-(R-s-C)')or(
                            modelo=='C-s-(R-p-L)')or(modelo=='C-p-(R-s-L)'):
                                # tipo:modelo,n
                                # modelo:R-s-L-s-C
                                # R
                                # L
                                # C
                                # fmin,fmax
                                
                                datos[2][0]=float(datos[2][0]) #R
                                datos[3][0]=float(datos[3][0]) #L
                                datos[4][0]=float(datos[4][0]) #C
                                datos[5][0]=float(datos[5][0]) #fmin
                                datos[5][1]=float(datos[5][1]) #fmax
            
            elif modelo=='Antena Microstrip':
                # tipo:modelo,n
                # modelo:Antena Microstrip
                # L1
                # C1
                # R
                # L
                # C
                # fmin,fmax
                
                datos[2][0]=float(datos[2][0]) #L1
                datos[3][0]=float(datos[3][0]) #C1
                datos[4][0]=float(datos[4][0]) #R
                datos[5][0]=float(datos[5][0]) #L
                datos[6][0]=float(datos[6][0]) #C
                datos[7][0]=float(datos[7][0]) #fmin
                datos[7][1]=float(datos[7][1]) #fmax
                
        elif tipo=='Archivo':
            # tipo:Archivo,n
            # f1,r1,x1
            # f2,r2,x2
            # ...
            # fn,rn,xn
            # fmin,fmax

            for i in range(1,n+1):
                datos[i][0]=float(datos[i][0]) #fi
                datos[i][1]=float(datos[i][1]) #ri
                datos[i][2]=float(datos[i][2]) #xi
                
            datos[n+1][0]=float(datos[n+1][0]) #fmin
            datos[n+1][1]=float(datos[n+1][1]) #fmax
            
        return datos
    
    def guardar_modelo_impedancia(self): 
        # Tipo:Modelo,n
        # Modelo: R-s-L-s-C
        # R
        # L
        # C
        # fmin,fmax
        
        if self.datos_impedancia[0][0]=='Archivo': self.datos_impedancia=self.plantilla_datos_impedancia()
                    
        carpeta='./Datos/Generador'
        ruta = QFileDialog.getSaveFileName(self,'Guardar archivo',carpeta,'*.modelimp')[0]
        if ruta!='':
            if ruta[-9:] != '.modelimp': ruta=ruta+'.modelimp'
            with open(ruta,'w',newline='') as archivo:
                escritor = csv.writer(archivo)
                for fila in self.datos_impedancia:
                    escritor.writerow(fila)
                    
    def reiniciar_impedancia(self): 
        self.datos_impedancia=self.plantilla_datos_impedancia()
        self.cbx_modelo.setCurrentText('R')
        self.WI['linedit_R'].setText('')
        self.WI['linedit_R'].setEnabled(True)
        self.WI['cbx_R'].setCurrentText('Ω')
        self.WI['cbx_R'].setEnabled(True)
        self.lbl_importado.hide()
        
    def eliminar_diccionario_de_widgets(self): 
        hilo_borrar=EliminarDiccionarioDeWidgets(self.WI)
        hilo_borrar.start()
        while not hilo_borrar.isFinished(): pass
        hilo_borrar.salir()
        hilo_borrar.deleteLater()
        self.WI=dict()
        
    def CrearWidgets_impedancia(self): 
        if self.cbx_modelo.currentText()=='R':
            self.WI['lbl_R']=QLabel('R:',alignment=Qt.AlignRight)
            self.WI['lbl_R'].setStyleSheet(self.cvp.SS_lbl)
            self.WI['lbl_R'].setMinimumWidth(75)
            self.WI['lbl_R'].setFixedHeight(20)
            self.WI['linedit_R']=QLineEdit(alignment=Qt.AlignLeft)
            self.WI['linedit_R'].setStyleSheet(self.cvp.SS_linedit)
            self.WI['linedit_R'].setMinimumWidth(69)
            self.WI['linedit_R'].setMaximumWidth(69)
            self.WI['linedit_R'].setFixedHeight(20)
            self.WI['linedit_R'].setValidator(QDoubleValidator())
            self.WI['cbx_R']=QComboBox()
            self.WI['cbx_R'].addItem('kΩ')
            self.WI['cbx_R'].addItem('Ω')
            self.WI['cbx_R'].addItem('mΩ')   
            self.WI['cbx_R'].setCurrentText('Ω')
            self.WI['cbx_R'].setStyleSheet(self.cvp.SS_cbx_und)
            self.layout_impedancia.addWidget(self.WI['lbl_R'],0,0)
            self.layout_impedancia.addWidget(self.WI['linedit_R'],0,1)
            self.layout_impedancia.addWidget(self.WI['cbx_R'],0,2)
            self.WI['linedit_R'].editingFinished.connect(partial(self.editing_finished_impedancia,'R',2,0))
            self.WI['linedit_R'].textChanged.connect(partial(self.text_changed_impedancia,self.WI['linedit_R'],2,0))
            self.WI['cbx_R'].currentTextChanged.connect(partial(self.accion_cbx_unidades_impedancia,'R',2,0))
            
            pixmap = QPixmap('./imagenes_impedancias/impedancia_generador/R.png')
            self.lbl_modelo.setPixmap(pixmap)
                        
        elif (self.cbx_modelo.currentText()=='R-s-L')or(self.cbx_modelo.currentText()=='R-p-L'):
            self.WI['lbl_R']=QLabel('R:',alignment=Qt.AlignRight)
            self.WI['lbl_R'].setStyleSheet(self.cvp.SS_lbl)
            self.WI['lbl_R'].setMinimumWidth(75)
            self.WI['lbl_R'].setFixedHeight(20)
            self.WI['linedit_R']=QLineEdit(alignment=Qt.AlignLeft)
            self.WI['linedit_R'].setStyleSheet(self.cvp.SS_linedit)
            self.WI['linedit_R'].setMinimumWidth(69)
            self.WI['linedit_R'].setMaximumWidth(69)
            self.WI['linedit_R'].setFixedHeight(20)
            self.WI['linedit_R'].setValidator(QDoubleValidator())
            self.WI['cbx_R']=QComboBox()
            self.WI['cbx_R'].addItem('kΩ')
            self.WI['cbx_R'].addItem('Ω')
            self.WI['cbx_R'].addItem('mΩ')   
            self.WI['cbx_R'].setCurrentText('Ω')
            self.WI['cbx_R'].setStyleSheet(self.cvp.SS_cbx_und)
            self.layout_impedancia.addWidget(self.WI['lbl_R'],0,0)
            self.layout_impedancia.addWidget(self.WI['linedit_R'],0,1)
            self.layout_impedancia.addWidget(self.WI['cbx_R'],0,2)
            self.WI['linedit_R'].editingFinished.connect(partial(self.editing_finished_impedancia,'R',2,0))
            self.WI['linedit_R'].textChanged.connect(partial(self.text_changed_impedancia,self.WI['linedit_R'],2,0))
            self.WI['cbx_R'].currentTextChanged.connect(partial(self.accion_cbx_unidades_impedancia,'R',2,0))
            
            self.WI['lbl_L']=QLabel('L:',alignment=Qt.AlignRight)
            self.WI['lbl_L'].setStyleSheet(self.cvp.SS_lbl)
            self.WI['lbl_L'].setMinimumWidth(75)
            self.WI['lbl_L'].setFixedHeight(20)
            self.WI['linedit_L']=QLineEdit(alignment=Qt.AlignLeft)
            self.WI['linedit_L'].setStyleSheet(self.cvp.SS_linedit)
            self.WI['linedit_L'].setMinimumWidth(69)
            self.WI['linedit_L'].setMaximumWidth(69)
            self.WI['linedit_L'].setFixedHeight(20)
            self.WI['linedit_L'].setValidator(QDoubleValidator())
            self.WI['cbx_L']=QComboBox()
            self.WI['cbx_L'].addItem('H')
            self.WI['cbx_L'].addItem('mH')
            self.WI['cbx_L'].addItem('μH') 
            self.WI['cbx_L'].addItem('nH')
            self.WI['cbx_L'].addItem('pH')
            self.WI['cbx_L'].setCurrentText('nH')
            self.WI['cbx_L'].setStyleSheet(self.cvp.SS_cbx_und)
            self.layout_impedancia.addWidget(self.WI['lbl_L'],1,0)
            self.layout_impedancia.addWidget(self.WI['linedit_L'],1,1)
            self.layout_impedancia.addWidget(self.WI['cbx_L'],1,2)
            self.WI['linedit_L'].editingFinished.connect(partial(self.editing_finished_impedancia,'L',3,0))
            self.WI['linedit_L'].textChanged.connect(partial(self.text_changed_impedancia,self.WI['linedit_L'],3,0))
            self.WI['cbx_L'].currentTextChanged.connect(partial(self.accion_cbx_unidades_impedancia,'L',3,0))
            
            if (self.cbx_modelo.currentText()=='R-s-L'): pixmap = QPixmap('./imagenes_impedancias/impedancia_generador/R-s-L.png')
            elif (self.cbx_modelo.currentText()=='R-p-L'): pixmap = QPixmap('./imagenes_impedancias/impedancia_generador/R-p-L.png')
            
            self.lbl_modelo.setPixmap(pixmap)
            
        elif (self.cbx_modelo.currentText()=='R-s-C')or(self.cbx_modelo.currentText()=='R-p-C'):
            self.WI['lbl_R']=QLabel('R:',alignment=Qt.AlignRight)
            self.WI['lbl_R'].setStyleSheet(self.cvp.SS_lbl)
            self.WI['lbl_R'].setMinimumWidth(75)
            self.WI['lbl_R'].setFixedHeight(20)
            self.WI['linedit_R']=QLineEdit(alignment=Qt.AlignLeft)
            self.WI['linedit_R'].setStyleSheet(self.cvp.SS_linedit)
            self.WI['linedit_R'].setMinimumWidth(69)
            self.WI['linedit_R'].setMaximumWidth(69)
            self.WI['linedit_R'].setFixedHeight(20)
            self.WI['linedit_R'].setValidator(QDoubleValidator())
            self.WI['cbx_R']=QComboBox()
            self.WI['cbx_R'].addItem('kΩ')
            self.WI['cbx_R'].addItem('Ω')
            self.WI['cbx_R'].addItem('mΩ')   
            self.WI['cbx_R'].setCurrentText('Ω')
            self.WI['cbx_R'].setStyleSheet(self.cvp.SS_cbx_und)
            self.layout_impedancia.addWidget(self.WI['lbl_R'],0,0)
            self.layout_impedancia.addWidget(self.WI['linedit_R'],0,1)
            self.layout_impedancia.addWidget(self.WI['cbx_R'],0,2)
            self.WI['linedit_R'].editingFinished.connect(partial(self.editing_finished_impedancia,'R',2,0))
            self.WI['linedit_R'].textChanged.connect(partial(self.text_changed_impedancia,self.WI['linedit_R'],2,0))
            self.WI['cbx_R'].currentTextChanged.connect(partial(self.accion_cbx_unidades_impedancia,'R',2,0))
            
            self.WI['lbl_C']=QLabel('C:',alignment=Qt.AlignRight)
            self.WI['lbl_C'].setStyleSheet(self.cvp.SS_lbl)
            self.WI['lbl_C'].setMinimumWidth(75)
            self.WI['lbl_C'].setFixedHeight(20)
            self.WI['linedit_C']=QLineEdit(alignment=Qt.AlignLeft)
            self.WI['linedit_C'].setStyleSheet(self.cvp.SS_linedit)
            self.WI['linedit_C'].setMinimumWidth(69)
            self.WI['linedit_C'].setMaximumWidth(69)
            self.WI['linedit_C'].setFixedHeight(20)
            self.WI['linedit_C'].setValidator(QDoubleValidator())
            self.WI['cbx_C']=QComboBox()
            self.WI['cbx_C'].addItem('F')
            self.WI['cbx_C'].addItem('mF')
            self.WI['cbx_C'].addItem('μF') 
            self.WI['cbx_C'].addItem('nF')
            self.WI['cbx_C'].addItem('pF')
            self.WI['cbx_C'].setCurrentText('pF')
            self.WI['cbx_C'].setStyleSheet(self.cvp.SS_cbx_und)
            self.layout_impedancia.addWidget(self.WI['lbl_C'],1,0)
            self.layout_impedancia.addWidget(self.WI['linedit_C'],1,1)
            self.layout_impedancia.addWidget(self.WI['cbx_C'],1,2)
            self.WI['linedit_C'].editingFinished.connect(partial(self.editing_finished_impedancia,'C',3,0))
            self.WI['linedit_C'].textChanged.connect(partial(self.text_changed_impedancia,self.WI['linedit_C'],3,0))
            self.WI['cbx_C'].currentTextChanged.connect(partial(self.accion_cbx_unidades_impedancia,'C',3,0))
            
            if (self.cbx_modelo.currentText()=='R-s-C'): pixmap = QPixmap('./imagenes_impedancias/impedancia_generador/R-s-C.png')
            elif (self.cbx_modelo.currentText()=='R-p-C'): pixmap = QPixmap('./imagenes_impedancias/impedancia_generador/R-p-C.png')
            
            self.lbl_modelo.setPixmap(pixmap)
                                    
        elif (self.cbx_modelo.currentText()=='R-s-L-s-C')or(self.cbx_modelo.currentText()=='R-p-L-p-C')or(
                    self.cbx_modelo.currentText()=='R-s-(L-p-C)')or(self.cbx_modelo.currentText()=='R-p-(L-s-C)')or(
                        self.cbx_modelo.currentText()=='L-s-(R-p-C)')or(self.cbx_modelo.currentText()=='L-p-(R-s-C)')or(
                            self.cbx_modelo.currentText()=='C-s-(R-p-L)')or(self.cbx_modelo.currentText()=='C-p-(R-s-L)'):
                                
                                self.WI['lbl_R']=QLabel('R:',alignment=Qt.AlignRight)
                                self.WI['lbl_R'].setStyleSheet(self.cvp.SS_lbl)
                                self.WI['lbl_R'].setMinimumWidth(75)
                                self.WI['lbl_R'].setFixedHeight(20)
                                self.WI['linedit_R']=QLineEdit(alignment=Qt.AlignLeft)
                                self.WI['linedit_R'].setStyleSheet(self.cvp.SS_linedit)
                                self.WI['linedit_R'].setMinimumWidth(69)
                                self.WI['linedit_R'].setMaximumWidth(69)
                                self.WI['linedit_R'].setFixedHeight(20)
                                self.WI['linedit_R'].setValidator(QDoubleValidator())
                                self.WI['cbx_R']=QComboBox()
                                self.WI['cbx_R'].addItem('kΩ')
                                self.WI['cbx_R'].addItem('Ω')
                                self.WI['cbx_R'].addItem('mΩ')   
                                self.WI['cbx_R'].setCurrentText('Ω')
                                self.WI['cbx_R'].setStyleSheet(self.cvp.SS_cbx_und)
                                self.layout_impedancia.addWidget(self.WI['lbl_R'],0,0)
                                self.layout_impedancia.addWidget(self.WI['linedit_R'],0,1)
                                self.layout_impedancia.addWidget(self.WI['cbx_R'],0,2)
                                self.WI['linedit_R'].editingFinished.connect(partial(self.editing_finished_impedancia,'R',2,0))
                                self.WI['linedit_R'].textChanged.connect(partial(self.text_changed_impedancia,self.WI['linedit_R'],2,0))
                                self.WI['cbx_R'].currentTextChanged.connect(partial(self.accion_cbx_unidades_impedancia,'R',2,0))
                                
                                self.WI['lbl_L']=QLabel('L:',alignment=Qt.AlignRight)
                                self.WI['lbl_L'].setStyleSheet(self.cvp.SS_lbl)
                                self.WI['lbl_L'].setMinimumWidth(75)
                                self.WI['lbl_L'].setFixedHeight(20)
                                self.WI['linedit_L']=QLineEdit(alignment=Qt.AlignLeft)
                                self.WI['linedit_L'].setStyleSheet(self.cvp.SS_linedit)
                                self.WI['linedit_L'].setMinimumWidth(69)
                                self.WI['linedit_L'].setMaximumWidth(69)
                                self.WI['linedit_L'].setFixedHeight(20)
                                self.WI['linedit_L'].setValidator(QDoubleValidator())
                                self.WI['cbx_L']=QComboBox()
                                self.WI['cbx_L'].addItem('H')
                                self.WI['cbx_L'].addItem('mH')
                                self.WI['cbx_L'].addItem('μH') 
                                self.WI['cbx_L'].addItem('nH')
                                self.WI['cbx_L'].addItem('pH')
                                self.WI['cbx_L'].setCurrentText('nH')
                                self.WI['cbx_L'].setStyleSheet(self.cvp.SS_cbx_und)
                                self.layout_impedancia.addWidget(self.WI['lbl_L'],1,0)
                                self.layout_impedancia.addWidget(self.WI['linedit_L'],1,1)
                                self.layout_impedancia.addWidget(self.WI['cbx_L'],1,2)
                                self.WI['linedit_L'].editingFinished.connect(partial(self.editing_finished_impedancia,'L',3,0))
                                self.WI['linedit_L'].textChanged.connect(partial(self.text_changed_impedancia,self.WI['linedit_L'],3,0))
                                self.WI['cbx_L'].currentTextChanged.connect(partial(self.accion_cbx_unidades_impedancia,'L',3,0))
                                
                                self.WI['lbl_C']=QLabel('C:',alignment=Qt.AlignRight)
                                self.WI['lbl_C'].setStyleSheet(self.cvp.SS_lbl)
                                self.WI['lbl_C'].setMinimumWidth(75)
                                self.WI['lbl_C'].setFixedHeight(20)
                                self.WI['linedit_C']=QLineEdit(alignment=Qt.AlignLeft)
                                self.WI['linedit_C'].setStyleSheet(self.cvp.SS_linedit)
                                self.WI['linedit_C'].setMinimumWidth(69)
                                self.WI['linedit_C'].setMaximumWidth(69)
                                self.WI['linedit_C'].setFixedHeight(20)
                                self.WI['linedit_C'].setValidator(QDoubleValidator())
                                self.WI['cbx_C']=QComboBox()
                                self.WI['cbx_C'].addItem('F')
                                self.WI['cbx_C'].addItem('mF')
                                self.WI['cbx_C'].addItem('μF') 
                                self.WI['cbx_C'].addItem('nF')
                                self.WI['cbx_C'].addItem('pF')
                                self.WI['cbx_C'].setCurrentText('pF')
                                self.WI['cbx_C'].setStyleSheet(self.cvp.SS_cbx_und)
                                self.layout_impedancia.addWidget(self.WI['lbl_C'],2,0)
                                self.layout_impedancia.addWidget(self.WI['linedit_C'],2,1)
                                self.layout_impedancia.addWidget(self.WI['cbx_C'],2,2)
                                self.WI['linedit_C'].editingFinished.connect(partial(self.editing_finished_impedancia,'C',4,0))
                                self.WI['linedit_C'].textChanged.connect(partial(self.text_changed_impedancia,self.WI['linedit_C'],4,0))
                                self.WI['cbx_C'].currentTextChanged.connect(partial(self.accion_cbx_unidades_impedancia,'C',4,0))
                                
                                if(self.cbx_modelo.currentText()=='R-s-L-s-C'): pixmap=QPixmap('./imagenes_impedancias/impedancia_generador/R-s-L-s-C.png')
                                elif(self.cbx_modelo.currentText()=='R-p-L-p-C'): pixmap=QPixmap('./imagenes_impedancias/impedancia_generador/R-p-L-p-C.png')
                                elif(self.cbx_modelo.currentText()=='R-s-(L-p-C)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_generador/R-s-(L-p-C).png')
                                elif(self.cbx_modelo.currentText()=='R-p-(L-s-C)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_generador/R-p-(L-s-C).png')
                                elif(self.cbx_modelo.currentText()=='L-s-(R-p-C)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_generador/L-s-(R-p-C).png')
                                elif(self.cbx_modelo.currentText()=='L-p-(R-s-C)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_generador/L-p-(R-s-C).png')
                                elif(self.cbx_modelo.currentText()=='C-s-(R-p-L)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_generador/C-s-(R-p-L).png')
                                elif(self.cbx_modelo.currentText()=='C-p-(R-s-L)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_generador/C-p-(R-s-L).png')
                                
                                self.lbl_modelo.setPixmap(pixmap)
      
        
    def accionmodelo_impedancia(self): 
        if self.ignorar_senhales_impedancia: return
        self.lbl_importado.hide()
        
        self.eliminar_diccionario_de_widgets()
        self.CrearWidgets_impedancia()

        self.datos_impedancia=self.plantilla_datos_impedancia(tipo='Modelo',modelo=self.cbx_modelo.currentText())
        
    def accion_cbx_unidades_impedancia(self,key,fila,columna): 
        if self.ignorar_senhales_impedancia: return
        
        if key=='R':
            if self.WI['cbx_'+key].currentText()=='kΩ': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='Ω': mult=1
            elif self.WI['cbx_'+key].currentText()=='mΩ': mult=1e-3
            try: self.datos_impedancia[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
            
        elif key=='L':
            if self.WI['cbx_'+key].currentText()=='H': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='mH': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='μH': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='nH': mult=1
            elif self.WI['cbx_'+key].currentText()=='pH': mult=1e-3
            try: self.datos_impedancia[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
        
        elif key=='C':
            if self.WI['cbx_'+key].currentText()=='F': mult=1e12
            elif self.WI['cbx_'+key].currentText()=='mF': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='μF': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='nF': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='pF': mult=1
            try: self.datos_impedancia[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
        
        elif key=='L1':
            if self.WI['cbx_'+key].currentText()=='H': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='mH': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='μH': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='nH': mult=1
            elif self.WI['cbx_'+key].currentText()=='pH': mult=1e-3
            try: self.datos_impedancia[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
        
        elif key=='C1':
            if self.WI['cbx_'+key].currentText()=='F': mult=1e12
            elif self.WI['cbx_'+key].currentText()=='mF': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='μF': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='nF': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='pF': mult=1
            try: self.datos_impedancia[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
        
    def text_changed_impedancia(self,linedit,fila,columna):
        if self.ignorar_senhales_impedancia:
            self.datos_impedancia[fila][columna]=linedit.text()
        else:
            self.ignorar_senhales_impedancia=True
            self.datos_impedancia[fila][columna]=linedit.text()
            self.ignorar_senhales_impedancia=False
    
    def editing_finished_impedancia(self,key,fila,columna): 
        if self.ignorar_senhales_impedancia: return
        self.WI['linedit_'+key].setCursorPosition(0)
        try: self.datos_impedancia[fila][columna]=float(self.WI['linedit_'+key].text())*self.multiplicador_impedancia(key)
        except: pass
        
    def multiplicador_impedancia(self,key): 
        if key=='R':
            if self.WI['cbx_'+key].currentText()=='kΩ': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='Ω': mult=1
            elif self.WI['cbx_'+key].currentText()=='mΩ': mult=1e-3
            
        elif key=='L' or key=='L1':
            if self.WI['cbx_'+key].currentText()=='H': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='mH': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='μH': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='nH': mult=1
            elif self.WI['cbx_'+key].currentText()=='pH': mult=1e-3
        
        elif key=='C' or key=='C1':
            if self.WI['cbx_'+key].currentText()=='F': mult=1e12
            elif self.WI['cbx_'+key].currentText()=='mF': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='μF': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='nF': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='pF': mult=1
                    
        return mult
    
    def datosAventana_impedancia(self): 
        
        if self.datos_impedancia[0][0]=='Modelo':
            # Tipo:Modelo,n
            # Modelo: R-s-L-s-C
            # R
            # L
            # C
            # fmin,fmax
            
            self.lbl_importado.hide()
            
            # Establecer el modelo
            self.cbx_modelo.setCurrentText(self.datos_impedancia[1][0])
            
            # Eliminar Widgets previos y crear los nuevos
            self.eliminar_diccionario_de_widgets()
            self.CrearWidgets_impedancia()
            
            # Cargar los Widgets con la información
            if (self.cbx_modelo.currentText()=='R'):
                self.WI['linedit_R'].setText(str(self.datos_impedancia[2][0]))
                self.WI['linedit_R'].setCursorPosition(0)
                
            elif (self.cbx_modelo.currentText()=='R-s-L')or(self.cbx_modelo.currentText()=='R-p-L'):
                self.WI['linedit_R'].setText(str(self.datos_impedancia[2][0]))
                self.WI['linedit_L'].setText(str(self.datos_impedancia[3][0]))
                self.WI['linedit_R'].setCursorPosition(0)
                self.WI['linedit_L'].setCursorPosition(0)
                
            elif (self.cbx_modelo.currentText()=='R-s-C')or(self.cbx_modelo.currentText()=='R-p-C'):
                self.WI['linedit_R'].setText(str(self.datos_impedancia[2][0]))
                self.WI['linedit_C'].setText(str(self.datos_impedancia[3][0]))
                self.WI['linedit_R'].setCursorPosition(0)
                self.WI['linedit_C'].setCursorPosition(0)
    
            elif (self.cbx_modelo.currentText()=='R-s-L-s-C')or(self.cbx_modelo.currentText()=='R-p-L-p-C')or(
                    self.cbx_modelo.currentText()=='R-s-(L-p-C)')or(self.cbx_modelo.currentText()=='R-p-(L-s-C)')or(
                        self.cbx_modelo.currentText()=='L-s-(R-p-C)')or(self.cbx_modelo.currentText()=='L-p-(R-s-C)')or(
                            self.cbx_modelo.currentText()=='C-s-(R-p-L)')or(self.cbx_modelo.currentText()=='C-p-(R-s-L)'):
                                self.WI['linedit_R'].setText(str(self.datos_impedancia[2][0]))
                                self.WI['linedit_L'].setText(str(self.datos_impedancia[3][0]))
                                self.WI['linedit_C'].setText(str(self.datos_impedancia[4][0]))
                                self.WI['linedit_R'].setCursorPosition(0)
                                self.WI['linedit_L'].setCursorPosition(0)
                                self.WI['linedit_C'].setCursorPosition(0)
                
        elif self.datos_impedancia[0][0]=='Archivo':
            # Tipo:Archivo,n
            # f1,r1,x1
            # f2,r2,x2
            # ...
            # fn,rn,xn
            # fmin,fmax
            
            # Establecer el modelo
            self.cbx_modelo.setCurrentText('R')
            
            # Eliminar Widgets previos y crear los nuevos
            self.eliminar_diccionario_de_widgets()
            self.CrearWidgets_impedancia()
                        
            self.lbl_importado.show()
    
                 
    ### Lógica de Cómputo
    ### Fuente
    def determinar_fmin_fmax_datos_fuente(self): 
        try:
            fmin=Infinity
            fmax=0
            for n  in range(1,int(float(self.datos_fuente[0][1]))+1):
                f=float(self.datos_fuente[n][1])
                if f > fmax: fmax=f
                if f < fmin: fmin=f
                
            self.datos_fuente[-1]=[fmin,fmax]
            self.fmin_fuente=fmin
            self.fmax_fuente=fmax
            
        except:
            self.datos_fuente[-1]=['','']
            self.fmin_fuente=None
            self.fmax_fuente=None
            
    def datos_correcto_fuente(self, advertir=True):  #No verifica fmin,fmax
        # Potencia/Voltaje,Nmed        
        # P1/V1,f1
        # P2/V2,f2
        # ...
        # PN/VN,fN
        # fmin,fmax
        
        try:
            for i in range(1,int(float(self.datos_fuente[0][1]))+1):
                if float(self.datos_fuente[i][0]) < 0: #P/V
                    if advertir:
                        ad=adv('Los valores de la fuente deben ser mayores\no iguales a cero.')
                        ad.exec()
                    return False
                
                if float(self.datos_fuente[i][1]) <= 0: #f
                    if advertir:
                        ad=adv('Los valores de frecuencia de la fuente\ndeben ser mayores que cero.')
                        ad.exec()
                    return False
        except:
            
            if advertir:
                ad=adv('Ingrese correctamente los parámetros\nde la fuente.')
                ad.exec()
            return False
        
        return True
    
    def formato_correcto_fuente(self,datos):
        if datos[0][0]=='Potencia' or datos[0][0]=='Voltaje':pass
        else: return False
        
        Nmed=int(float(datos[0][1]))
        if len(datos)!=(Nmed+2): return False
        
        for i in range(1,Nmed+1):
            if len(datos[i]) != 2: return False
            
        if len(datos[-1]) != 2: return False
        
        return True
    
    def s_vs_f(self):
        s_vs_f=[[],[]]
        
        for i in range(1,int(float(self.datos_fuente[0][1]))+1):
            s=float(self.datos_fuente[i][0])
            f=float(self.datos_fuente[i][1])
            s_vs_f[0].append(s)
            s_vs_f[1].append(f)
            
        return s_vs_f
        
    
    def calcularFuente(self,F):
        return FUENTE(F,self.s_vs_f())
    
    def calcularVoltaje(self,Impedancia,F):
        if self.datos_fuente[0][0]=='Voltaje':
            Vin_F=self.calcularFuente(F) #el voltaje |Vin|, interpolado, en todo F
            Vg=[] #Módulo del voltaje de la fuente
            for indf in range(len(F)):
                Vg.append(2*Vin_F[indf])
                
            return Vg #el modulo del voltaje de la fuente, interpolado, en todo F
        
        elif self.datos_fuente[0][0]=='Potencia':
            Pin_F=self.calcularFuente(F) #la potencia Pin, interpolada, en todo F
            Vg=[] #Módulo del voltaje de la fuente
            for indf in range(len(F)):
                Vg.append(sqrt((8*Pin_F[indf])/((1/((complex(Impedancia[indf])).conjugate())).real)))
                
            return Vg #el modulo del voltaje de la fuente, interpolado, en todo F
        
        
    ### Impedancia
    def determinar_fmin_fmax_datos_impedancia(self): 
        if self.datos_impedancia[0][0]=='Modelo':
            self.datos_impedancia[-1]=[0,Infinity]
            
        elif self.datos_impedancia[0][0]=='Archivo':
            try:
                fmin=Infinity
                fmax=0
                for n  in range(1,int(float(self.datos_impedancia[0][1]))+1):
                    f=float(self.datos_impedancia[n][0])
                    if f > fmax: fmax=f
                    if f < fmin: fmin=f
                    
                self.datos_impedancia[-1]=[fmin,fmax]
                self.fmin_impedancia=fmin
                self.fmax_impedancia=fmax
                
            except:
                self.datos_impedancia[-1]=['','']
                self.fmin_impedancia=None
                self.fmax_impedancia=None
    
    def datos_correcto_impedancia(self, advertir=True):  #No verifica fmin,fmax
        try:
            if self.datos_impedancia[0][0]=='Modelo':
                # tipo:modelo,n
                # modelo:Antena Microstrip
                # L1
                # C1
                # R
                # L
                # C
                # fmin,fmax
                
                for i in range(2,int(float(self.datos_impedancia[0][1]))):
                    if float(self.datos_impedancia[i][0]) <= 0: #R,L,C
                        if advertir:
                            ad=adv('El valor de cada elemento de la impedancia\ndel generador debe ser mayor que cero.')
                            ad.exec()
                        return False
                    
            elif self.datos_impedancia[0][0]=='Archivo':
                # tipo:Archivo,n
                # f1,r1,x1
                # f2,r2,x2
                # ...
                # fn,rn,xn
                # fmin,fmax
                
                if int(float(self.datos_impedancia[0][1])) != (len(self.datos_impedancia)-2):
                    if advertir:
                        ad=adv('Error en el contenido del archivo\nde la impedancia del generador.')
                        ad.exec()
                    return False
                
                for i in range(1,int(float(self.datos_impedancia[0][1]))+1):
                    if float(self.datos_impedancia[i][0]) <= 0: #f
                        if advertir:
                            ad=adv('El archivo .imp de la impedancia del generador\ncontiene valores incorrectos de frecuencia.')
                            ad.exec()
                        return False
                    
                    if float(self.datos_impedancia[i][1]) < 0: #r
                        if advertir:
                            ad=adv('El archivo .imp de la impedancia del generador\ncontiene valores incorrectos de resistencia.')
                            ad.exec()
                        return False
                
        except:
            
            if advertir:
                ad=adv('Ingrese correctamente los parámetros\nde la impedancia del generador.')
                ad.exec()
            return False
        
        return True
    
    def formato_correcto_impedancia(self,datos):
        if datos[0][0]=='Modelo':
            if self.cbx_modelo.findText(datos[1][0]) == -1: return False
            
            n=int(float(datos[0][1]))
            if len(datos) != (n+1): return False
            if len(datos[-1]) != 2: return False
            
        elif datos[0][0]=='Archivo':
            n=int(float(datos[0][1]))
            if len(datos) != (n+2): return False
            for i in range(1,n+1):
                if len(datos[i]) != 3: return False
            if len(datos[-1]) != 2: return False
            
        else:
            return False
        
        return True
        
    
    def z_vs_f(self):
        z_vs_f=[[],[]]
        j=complex(0+1j)
        
        for i in range(1,int(float(self.datos_impedancia[0][1]))+1):
            z=float(self.datos_impedancia[i][1])+j*float(self.datos_impedancia[i][2])
            f=float(self.datos_impedancia[i][0])
            z_vs_f[0].append(z)
            z_vs_f[1].append(f)
            
        return z_vs_f
        
    def calcularImpedancia(self,F):
        self.datos_impedancia=self.formatear_datos_impedancia(self.datos_impedancia)
        Z=[]
        if self.datos_impedancia[0][0]=='Modelo': Z=ZCARGA(F,self.datos_impedancia,None)
        elif self.datos_impedancia[0][0]=='Archivo': Z=ZCARGA(F,self.datos_impedancia,self.z_vs_f())  
        return Z   

    def calcularImpedanciaPrima(self,Z,DGA,Alfa,Beta,Zc,F): 
        dga=int(float(DGA))*1e-3 # en [m]
        if dga > 0:
            Zprima=[]
            j=complex(0+1j)
            for indf in range(len(F)):
                zcarga=Z[indf]
                alfa=Alfa[indf]
                beta=Beta[indf]
                zc=Zc[indf]
                
                Zprima.append(zc*((zcarga+zc*complextanh((alfa+j*beta)*dga))/(zc+zcarga*complextanh((alfa+j*beta)*dga))))
                
            return Zprima
        else:
            return Z    
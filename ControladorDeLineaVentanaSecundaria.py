# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""
from PyQt5.QtGui import QDoubleValidator
from Funciones import rlgc_ABZ_sinPerdidas,rlgc_ABZ_perdidasGenerales,rlgc_ABZ_Ltx
import os.path
import csv
from PyQt5.QtWidgets import QFileDialog,QLabel,QLineEdit,QPushButton,QComboBox,QMainWindow
from PyQt5.QtCore import Qt

from ControladorDeLTx import ControladorDeLTx
from functools import partial
from Advertencia import adv

from PyQt5.QtCore import QThread
from numpy import Infinity

from ventanaSecundaria_linea_ui import Ui_MainWindow as VentanaSecundariaLinea

from Funciones import vectordistancias

            
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
        
class ControladorDeLineaVentanaSecundaria(QMainWindow,VentanaSecundariaLinea):
    def __init__(self,ventana_secundaria):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setWindowTitle('Configurar línea de transmisión')
        
        self.setWindowModality(Qt.ApplicationModal)
        
        self.cvs=ventana_secundaria
        self.layout_parametroslinea.setAlignment(Qt.AlignTop)
        
        self.SS_lbl=self.cvs.cvp.SS_lbl
        self.SS_linedit=self.cvs.cvp.SS_linedit
        self.SS_pbtn=self.cvs.cvp.SS_pbtn
        self.SS_cbx=self.cvs.cvp.SS_cbx
        
        #Inicializar
        
        self.WL=dict() #Widgets de la Linea
        self.Alfa=[]
        self.Beta=[]
        self.Zc=[]
        self.rlgc_vs_f=dict() #diccionario para almacenar rvf,lvf,gvf,cvf
                
        self.fmin=None
        self.fmax=None
                
        self.cbx_perdidaslinea.setCurrentText('Sin pérdidas')
        self.cbx_modolinea.setCurrentText('Parámetros rlgc')
        self.lbl_modolinea.hide()
        self.cbx_modolinea.hide()
        self.datos=self.plantilla_datos(self.cbx_perdidaslinea.currentText(),self.cbx_tipocoero.currentText())
        
        """"
        En esta sección, el término llamado coero se refiere a una variable que puede almacenar 
        el valor de la capacitancia distribuida de la línea, la permitividad eléctrica relativa 
        o la velocidad (porcentual relativa a la velocidad de la luz en el vacío) de propagación 
        de la onda en el material de la línea. Usado en los casos sin pérdidas y bajas pérdidas.
        """
        
        self.WL['lbl_Ro']=self.lbl_Ro
        self.WL['lbl_coero']=self.lbl_coero
        self.WL['linedit_Ro']=self.linedit_Ro
        self.WL['linedit_coero']=self.linedit_coero
        self.WL['linedit_Ro'].setValidator(QDoubleValidator())
        self.WL['linedit_coero'].setValidator(QDoubleValidator())
        self.linedit_coero.editingFinished.connect(partial(self.editing_finished,self.linedit_coero,2,1))
        self.linedit_Ro.editingFinished.connect(partial(self.editing_finished,self.linedit_Ro,2,0))
        self.linedit_coero.textChanged.connect(partial(self.text_changed,self.linedit_coero,2,1))
        self.linedit_Ro.textChanged.connect(partial(self.text_changed,self.linedit_Ro,2,0))
        
        self.linedit_DGA.setValidator(QDoubleValidator())
        self.linedit_DCA.setValidator(QDoubleValidator())
        self.linedit_Pmax.setValidator(QDoubleValidator())
        
        self.ignorar_senhales=False # Util cuando se usa datosAventana

        #Conexiones
        self.cbx_perdidaslinea.currentTextChanged.connect(self.accion_perdidas)
        self.cbx_tipocoero.currentTextChanged.connect(self.actualizartipocoero)
        self.cbx_modolinea.currentTextChanged.connect(self.accion_modo_linea)
        self.linedit_DGA.editingFinished.connect(partial(self.editing_finished,self.linedit_DGA,3,1))
        self.linedit_DCA.editingFinished.connect(partial(self.editing_finished,self.linedit_DCA,3,0))
        self.linedit_Pmax.editingFinished.connect(partial(self.editing_finished,self.linedit_Pmax,1,1))
        
        self.linedit_DGA.textChanged.connect(partial(self.text_changed,self.linedit_DGA,3,1))
        self.linedit_DCA.textChanged.connect(partial(self.text_changed,self.linedit_DCA,3,0))
        self.linedit_Pmax.textChanged.connect(partial(self.text_changed,self.linedit_Pmax,1,1))
        
        self.cbx_Pmax.currentTextChanged.connect(self.accion_cbx_Pmax)
        self.cbx_DGA.currentTextChanged.connect(self.accion_cbx_DGA)
        self.cbx_DCA.currentTextChanged.connect(self.accion_cbx_DCA)
        
        self.actionCargar.triggered.connect(self.cargar)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionReiniciar.triggered.connect(self.reiniciar)
                
        self.pbtn_ok.clicked.connect(self.salir)
        
    ### Lógica de Interfaz Gráfica    
        
    def plantilla_datos(self,tipo_perdidas,coero_modo,tipo_ltx=None):  
        datos=[[tipo_perdidas]]
        if tipo_perdidas=='Sin pérdidas':
            #Tipo pérdidas
            #Tipocoero,Pmax
            #Ro,coero
            #DCA,DGA
            #fmin,fmax
            datos.append([coero_modo,''])
            datos.append(['',''])
            datos.append(['',''])
            datos.append([0,Infinity])
            
        elif tipo_perdidas=='Pérdidas generales':
            if coero_modo=='Parámetros rlgc':
                #Tipo pérdidas
                #Modo:rlgc,Pmax
                #r,l,g,c
                #DCA,DGA
                #fmin,fmax
                datos.append([coero_modo,''])
                datos.append(['','','',''])
                datos.append(['',''])
                datos.append([0,Infinity])

            elif coero_modo=='Tipo de línea de transmisión':
                #Tipo pérdidas
                #Modo:LTx,Pmax
                #'Tipo LTx',dim1,dim2,urc,Dc,urd,erd,Dd
                #DCA,DGA
                #fmin,fmax
                datos.append([coero_modo,''])
                datos.append([tipo_ltx,'','','','','','',''])
                datos.append(['',''])
                datos.append([0,Infinity])
                
        return datos
                
        
    def closeEvent(self, event): self.salir() 
        
        
    def salir(self): 
        self.actualizar_cbx_tipo_grafica()
        self.hide()
        self.cvs.setEnabled(True)
        self.graficar()
        
    def salir_sin_graficar(self): 
        self.actualizar_cbx_tipo_grafica()
        self.hide()
        self.cvs.setEnabled(True)
        
    def actualizar_cbx_tipo_grafica(self):
        if self.cvs.bandera=='buscar':
            
            self.cvs.cbx_tipografica.blockSignals(True)
            tipo=self.cvs.cbx_tipografica.currentText()
            self.cvs.cbx_tipografica.clear()
            
            self.cvs.cbx_tipografica.addItem('Coeficiente de reflexión')
            self.cvs.cbx_tipografica.addItem('Impedancia vista')
            if self.cbx_perdidaslinea.currentText()=='Sin pérdidas': self.cvs.cbx_tipografica.addItem('ROEV')
            if self.cvs.cbx_algoritmos.currentText()!='Todos (comparación)': self.cvs.cbx_tipografica.addItem('Carta de Smith')
            self.cvs.cbx_tipografica.addItem('Potencia activa promedio')
            self.cvs.cbx_tipografica.addItem('Respuesta en frecuencia')
            
            if self.cbx_perdidaslinea.currentText()=='Sin pérdidas':
                self.cvs.cbx_tipografica.setCurrentText(tipo)
            else:
                if tipo=='ROEV': self.cbx_perdidaslinea.setCurrentText('Coeficiente de reflexión')
                else: self.cbx_perdidaslinea.setCurrentText(tipo)
                  
            self.cvs.cbx_tipografica.blockSignals(False)
            
        elif self.cvs.bandera=='graficar':
            
            self.cvs.cbx_tipografica.blockSignals(True)
            tipo=self.cvs.cbx_tipografica.currentText()
            self.cvs.cbx_tipografica.clear()
            
            self.cvs.cbx_tipografica.addItem('Coeficiente de reflexión')
            self.cvs.cbx_tipografica.addItem('Impedancia vista')
            if self.cbx_perdidaslinea.currentText()=='Sin pérdidas': self.cvs.cbx_tipografica.addItem('ROEV')
            self.cvs.cbx_tipografica.addItem('Carta de Smith')
            self.cvs.cbx_tipografica.addItem('Potencia activa promedio')
            self.cvs.cbx_tipografica.addItem('Respuesta en frecuencia')
            
            if self.cbx_perdidaslinea.currentText()=='Sin pérdidas':
                self.cvs.cbx_tipografica.setCurrentText(tipo)
            else:
                if tipo=='ROEV': self.cbx_perdidaslinea.setCurrentText('Coeficiente de reflexión')
                else: self.cbx_perdidaslinea.setCurrentText(tipo)
                  
            self.cvs.cbx_tipografica.blockSignals(False)

    def cargar(self): 
        try:
            carpeta='./Datos/Linea'
            ruta = QFileDialog.getOpenFileName(self, 'Cargar archivo',carpeta,"*.line")[0]
            if os.path.exists(ruta):
                datos=[]
                with open(ruta) as archivo:
                    lector = csv.reader(archivo, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    for fila in lector: datos.append(fila) 
                
                
                if self.formato_correcto(datos): pass
                else: raise Exception
                
                self.datos=datos 
                self.determinar_fmin_fmax_datos()
                    
                self.ignorar_senhales=True
                self.datosAventana()
                self.ignorar_senhales=False
                
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos.')
            ad.exec_()
            self.ignorar_senhales=False
            self.reiniciar() 
            
    def cargar_datos(self,datos): 
        try: 
            if self.formato_correcto(datos): pass
            else: raise Exception
            
            self.datos=datos                
            self.determinar_fmin_fmax_datos()
                
            self.ignorar_senhales=True
            self.datosAventana()
            self.ignorar_senhales=False
                           
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos de\nla línea de transmisión.')
            ad.exec_()
            self.ignorar_senhales=False
            self.reiniciar()
            
    def formatear_datos(self,datos): 
        datos[1][1]=float(datos[1][1]) #Pmax
        datos[3][0]=int(float(datos[3][0])) #DCA
        datos[3][1]=int(float(datos[3][1])) #DGA
        datos[4][0]=float(datos[4][0]) #fmin
        datos[4][1]=float(datos[4][1]) #fmax
        
        if datos[0][0]=='Sin pérdidas':
            #Tipo pérdidas
            #Tipocoero,Pmax
            #Ro,coero
            #DCA,DGA
            #fmin,fmax
            datos[2][0]=float(datos[2][0])
            datos[2][1]=float(datos[2][1])
                        
        elif datos[0][0]=='Pérdidas generales':
            if datos[1][0]=='Parámetros rlgc':
                #Tipo pérdidas
                #Modo:rlgc,Pmax
                #r,l,g,c
                #DCA,DGA
                #fmin,fmax
                for m in range(len(datos[2])): datos[2][m]=float(datos[2][m])

            elif datos[1][0]=='Tipo de línea de transmisión':
                #Tipo pérdidas
                #Modo:LTx,Pmax
                #'Tipo LTx',dim1,dim2,urc,Dc,urd,erd,Dd
                #DCA,DGA
                #fmin,fmax
                for m in range(1,len(datos[2])): datos[2][m]=float(datos[2][m])
                
        return datos
            
    def guardar(self): 
        carpeta='./Datos/Linea'
        ruta = QFileDialog.getSaveFileName(self,'Guardar archivo',carpeta,'*.line')[0]
        if ruta!='':
            if ruta[-5:] != '.line': ruta=ruta+'.line'
            with open(ruta,'w',newline='') as archivo:
                escritor = csv.writer(archivo)
                for fila in self.datos:
                    escritor.writerow(fila)
        
    def reiniciar(self): 
        self.datos=self.plantilla_datos('Sin pérdidas','Capacitancia distribuida (pF/m)')
        self.cbx_perdidaslinea.setCurrentText('Sin pérdidas')
        self.cbx_tipocoero.setCurrentText('Capacitancia distribuida (pF/m)')
        self.WL['linedit_Ro'].setText('')
        self.WL['linedit_coero'].setText('')
        self.linedit_Pmax.setText('')
        self.cbx_Pmax.setCurrentText('W')
        self.linedit_DGA.setText('')
        self.cbx_DGA.setCurrentText('mm')
        self.linedit_DCA.setText('')
        self.cbx_DCA.setCurrentText('mm')
        
        
    def eliminar_diccionario_de_widgets(self): 
        hilo_borrar=EliminarDiccionarioDeWidgets(self.WL)
        hilo_borrar.start()
        while not hilo_borrar.isFinished(): pass
        hilo_borrar.salir()
        hilo_borrar.deleteLater()
        self.WL=dict()
        
    def CrearWidgets(self): 
        
        if self.cbx_perdidaslinea.currentText()=='Sin pérdidas': 
            
            if self.cbx_tipocoero.currentText()=='Capacitancia distribuida (pF/m)':
                palabra='c (pF/m):'
                tooltip='Capacitancia distribuida de la\nlínea de transmisión.'
            elif self.cbx_tipocoero.currentText()=='Constante dieléctrica relativa':
                palabra='\u03B5\u1D63:' #er  
                tooltip='Permitividad eléctrica relativa\ndel dieléctrico de la línea de transmisión.'                                         
            elif self.cbx_tipocoero.currentText()=='Velocidad de propagación (%)':
                palabra='Vp (%):'
                tooltip='Velocidad de propagación en la\nlínea de transmisión, expresada como\nporcentaje de la velocidad de propagación\nde la luz en el vacío.'
            
            self.WL['lbl_Ro']=QLabel('Ro (Ω):',alignment=Qt.AlignRight)
            self.WL['lbl_Ro'].setStyleSheet(self.SS_lbl)
            self.WL['lbl_Ro'].setToolTip('Resistencia característica\nde la línea de transmisión.')
            self.WL['linedit_Ro']=QLineEdit()
            self.WL['linedit_Ro'].setStyleSheet(self.SS_linedit)
            self.WL['lbl_coero']=QLabel(palabra,alignment=Qt.AlignRight)
            self.WL['lbl_coero'].setStyleSheet(self.SS_lbl)
            self.WL['lbl_coero'].setToolTip(tooltip)
            self.WL['linedit_coero']=QLineEdit()
            self.WL['linedit_coero'].setStyleSheet(self.SS_linedit)
            self.WL['linedit_Ro'].setValidator(QDoubleValidator())
            self.WL['linedit_coero'].setValidator(QDoubleValidator())
            self.layout_parametroslinea.addWidget(self.WL['lbl_Ro'],0,0)
            self.layout_parametroslinea.addWidget(self.WL['linedit_Ro'],0,1)
            self.layout_parametroslinea.addWidget(self.WL['lbl_coero'],1,0)
            self.layout_parametroslinea.addWidget(self.WL['linedit_coero'],1,1)
            
            #Conexiones
            self.WL['linedit_Ro'].editingFinished.connect(partial(self.editing_finished,self.WL['linedit_Ro'],2,0))
            self.WL['linedit_coero'].editingFinished.connect(partial(self.editing_finished,self.WL['linedit_coero'],2,1))
            self.WL['linedit_Ro'].textChanged.connect(partial(self.text_changed,self.WL['linedit_Ro'],2,0))
            self.WL['linedit_coero'].textChanged.connect(partial(self.text_changed,self.WL['linedit_coero'],2,1))
            
            
        elif self.cbx_perdidaslinea.currentText()=='Pérdidas generales':
            
            if self.cbx_modolinea.currentText()=='Parámetros rlgc':
                
                self.WL['lbl_r']=QLabel('r (Ω/m):',alignment=Qt.AlignRight)
                self.WL['lbl_r'].setStyleSheet(self.SS_lbl)
                self.WL['lbl_r'].setToolTip('Resistencia distribuida de la\nlínea de transmisión.')
                self.WL['linedit_r']=QLineEdit() 
                self.WL['linedit_r'].setStyleSheet(self.SS_linedit)
                self.WL['linedit_r'].setMinimumWidth(69)  
                self.WL['lbl_l']=QLabel('l (nH/m):',alignment=Qt.AlignRight)
                self.WL['lbl_l'].setStyleSheet(self.SS_lbl)
                self.WL['lbl_l'].setToolTip('Inductancia distribuida de la\nlínea de transmisión.')
                self.WL['linedit_l']=QLineEdit()
                self.WL['linedit_l'].setStyleSheet(self.SS_linedit)
                self.WL['linedit_l'].setMinimumWidth(69)  
                self.WL['lbl_g']=QLabel('g (S/m):',alignment=Qt.AlignRight)
                self.WL['lbl_g'].setStyleSheet(self.SS_lbl)
                self.WL['lbl_g'].setToolTip('Conductancia distribuida de la\nlínea de transmisión.')
                self.WL['linedit_g']=QLineEdit()
                self.WL['linedit_g'].setStyleSheet(self.SS_linedit)
                self.WL['linedit_g'].setMinimumWidth(69)  
                self.WL['lbl_c']=QLabel('c (pF/m):',alignment=Qt.AlignRight)
                self.WL['lbl_c'].setStyleSheet(self.SS_lbl)
                self.WL['lbl_c'].setToolTip('Capacitancia distribuida de la\nlínea de transmisión.')
                self.WL['linedit_c']=QLineEdit()
                self.WL['linedit_c'].setStyleSheet(self.SS_linedit)
                self.WL['linedit_c'].setMinimumWidth(69)  
                                        
                self.WL['linedit_r'].setValidator(QDoubleValidator())
                self.WL['linedit_l'].setValidator(QDoubleValidator())
                self.WL['linedit_g'].setValidator(QDoubleValidator())
                self.WL['linedit_c'].setValidator(QDoubleValidator())
                
                self.layout_parametroslinea.addWidget(self.WL['lbl_r'],0,0)
                self.layout_parametroslinea.addWidget(self.WL['linedit_r'],0,1)
                self.layout_parametroslinea.addWidget(self.WL['lbl_l'],1,0)
                self.layout_parametroslinea.addWidget(self.WL['linedit_l'],1,1)
                self.layout_parametroslinea.addWidget(self.WL['lbl_g'],2,0)
                self.layout_parametroslinea.addWidget(self.WL['linedit_g'],2,1)
                self.layout_parametroslinea.addWidget(self.WL['lbl_c'],3,0)
                self.layout_parametroslinea.addWidget(self.WL['linedit_c'],3,1)
                
                #Conexiones
                self.WL['linedit_r'].editingFinished.connect(partial(self.editing_finished,self.WL['linedit_r'],2,0))
                self.WL['linedit_l'].editingFinished.connect(partial(self.editing_finished,self.WL['linedit_l'],2,1))
                self.WL['linedit_g'].editingFinished.connect(partial(self.editing_finished,self.WL['linedit_g'],2,2))
                self.WL['linedit_c'].editingFinished.connect(partial(self.editing_finished,self.WL['linedit_c'],2,3))
                self.WL['linedit_r'].textChanged.connect(partial(self.text_changed,self.WL['linedit_r'],2,0))
                self.WL['linedit_l'].textChanged.connect(partial(self.text_changed,self.WL['linedit_l'],2,1))
                self.WL['linedit_g'].textChanged.connect(partial(self.text_changed,self.WL['linedit_g'],2,2))
                self.WL['linedit_c'].textChanged.connect(partial(self.text_changed,self.WL['linedit_c'],2,3))
            
            elif self.cbx_modolinea.currentText()=='Tipo de línea de transmisión':
                               
                self.WL['cbx_ltx']=QComboBox()
                self.WL['cbx_ltx'].setStyleSheet(self.SS_cbx)
                self.WL['cbx_ltx'].addItem('Coaxial')
                self.WL['cbx_ltx'].addItem('Bifilar')
                self.WL['cbx_ltx'].addItem('Plana')
                self.WL['pbtn_ver']=QPushButton('ver') 
                self.WL['pbtn_ver'].setStyleSheet(self.SS_pbtn)
                self.WL['pbtn_ver'].setMinimumWidth(35)
                self.WL['pbtn_ver'].setMaximumHeight(20)
                self.WL['pbtn_ver'].setFocusPolicy(Qt.NoFocus)
                
                self.WL['cbx_ltx'].setCurrentText('Coaxial')
                                          
                self.layout_parametroslinea.addWidget(self.WL['cbx_ltx'],0,0)
                self.layout_parametroslinea.addWidget(self.WL['pbtn_ver'],0,1)
                
                #Conexiones
                self.WL['pbtn_ver'].clicked.connect(self.abrir_ventana_ltx)
                self.WL['cbx_ltx'].currentTextChanged.connect(self.accion_cbx_ltx)
        
    def accion_perdidas(self): 
        if self.ignorar_senhales: return
            
        Pmax=self.datos[1][1]
        DCA=self.datos[3][0]
        DGA=self.datos[3][1]
        fmin=self.datos[4][0]
        fmax=self.datos[4][1]
        
        if self.cbx_perdidaslinea.currentText()=='Sin pérdidas':
            self.cbx_tipocoero.show()
            self.lbl_modolinea.hide()
            self.cbx_modolinea.hide()
                                       
        elif self.cbx_perdidaslinea.currentText()=='Pérdidas generales':
            self.cbx_tipocoero.hide()
            self.lbl_modolinea.show()
            self.cbx_modolinea.show()
                   
        self.eliminar_diccionario_de_widgets()
        self.CrearWidgets()
        
        if self.cbx_perdidaslinea.currentText()=='Sin pérdidas':
            self.datos=self.plantilla_datos(self.cbx_perdidaslinea.currentText(),self.cbx_tipocoero.currentText())
        elif self.cbx_perdidaslinea.currentText()=='Pérdidas generales':
            if self.cbx_modolinea.currentText()=='Parámetros rlgc':
                self.datos=self.plantilla_datos(self.cbx_perdidaslinea.currentText(),self.cbx_modolinea.currentText())
            elif self.cbx_modolinea.currentText()=='Tipo de línea de transmisión':
                self.datos=self.plantilla_datos(self.cbx_perdidaslinea.currentText(),self.cbx_modolinea.currentText(),self.WL['cbx_ltx'].currentText())
        
        self.datos[1][1]=Pmax
        self.datos[3][0]=DCA
        self.datos[3][1]=DGA
        self.datos[4][0]=fmin
        self.datos[4][1]=fmax
        
    def actualizartipocoero(self): 
        if self.ignorar_senhales: return
        
        if self.cbx_tipocoero.currentText()=='Capacitancia distribuida (pF/m)':
            palabra='c (pF/m):'
            tooltip='Capacitancia distribuida de la\nlínea de transmisión.'
        elif self.cbx_tipocoero.currentText()=='Constante dieléctrica relativa':
            palabra='\u03B5\u1D63:' #er  
            tooltip='Permitividad eléctrica relativa\ndel dieléctrico de la línea de transmisión.'                                         
        elif self.cbx_tipocoero.currentText()=='Velocidad de propagación (%)':
            palabra='Vp (%):'
            tooltip='Velocidad de propagación en la\nlínea de transmisión, expresada como\nporcentaje de la velocidad de propagación\nde la luz en el vacío.'
        
        self.WL['lbl_coero'].setText(palabra)
        self.WL['lbl_coero'].setToolTip(tooltip)
        self.WL['linedit_coero'].setText('')
        
        self.datos[1][0]=self.cbx_tipocoero.currentText()    
        self.datos[2][1]=''
        
                        
    def accion_modo_linea(self): 
        if self.ignorar_senhales: return
        
        Pmax=self.datos[1][1]
        DCA=self.datos[3][0]
        DGA=self.datos[3][1]
        fmin=self.datos[4][0]
        fmax=self.datos[4][1]
        
        self.eliminar_diccionario_de_widgets()
        self.CrearWidgets()
        
        if self.cbx_modolinea.currentText()=='Parámetros rlgc':
            self.datos=self.plantilla_datos(self.cbx_perdidaslinea.currentText(),self.cbx_modolinea.currentText())
        elif self.cbx_modolinea.currentText()=='Tipo de línea de transmisión':
            self.datos=self.plantilla_datos(self.cbx_perdidaslinea.currentText(),self.cbx_modolinea.currentText(),self.WL['cbx_ltx'].currentText())
        
        self.datos[1][1]=Pmax
        self.datos[3][0]=DCA
        self.datos[3][1]=DGA
        self.datos[4][0]=fmin
        self.datos[4][1]=fmax
         
    def accion_cbx_ltx(self): 
        if self.ignorar_senhales: return
        self.datos[2]=[self.WL['cbx_ltx'].currentText(),'','','','','','','']

    def abrir_ventana_ltx(self): 
        VLTx=ControladorDeLTx(self)
        VLTx.exec()
                    
    def accion_cbx_Pmax(self): 
        if self.ignorar_senhales: return
        
        if self.cbx_Pmax.currentText()=='kW': mult=1e3
        elif self.cbx_Pmax.currentText()=='W': mult=1
        elif self.cbx_Pmax.currentText()=='mW': mult=1e-3
        
        try: self.datos[1][1]=float(self.linedit_Pmax.text())*mult
        except: pass

    def accion_cbx_DGA(self): 
        if self.ignorar_senhales: return
        
        if self.cbx_DGA.currentText()=='m': mult=1e3
        elif self.cbx_DGA.currentText()=='cm': mult=10
        elif self.cbx_DGA.currentText()=='mm': mult=1
        
        try: self.datos[3][1]=float(self.linedit_DGA.text())*mult
        except: pass

    def accion_cbx_DCA(self): 
        if self.ignorar_senhales: return
        
        if self.cbx_DCA.currentText()=='m': mult=1e3
        elif self.cbx_DCA.currentText()=='cm': mult=10
        elif self.cbx_DCA.currentText()=='mm': mult=1
        
        try: self.datos[3][0]=float(self.linedit_DCA.text())*mult
        except: pass
    
    def text_changed(self,linedit,fila,columna):
        if self.ignorar_senhales:
            self.datos[fila][columna]=linedit.text()
        else:
            self.ignorar_senhales=True
            self.datos[fila][columna]=linedit.text()
            self.ignorar_senhales=False
            
    def editing_finished(self,linedit,fila,columna): 
        if self.ignorar_senhales: return
        linedit.setCursorPosition(0)
        try: self.datos[fila][columna]=float(linedit.text())*self.multiplicador(fila,columna)
        except: pass
    
    def multiplicador(self,fila,columna): 
        if fila==1 and columna==1: #Pmax
            if self.cbx_Pmax.currentText()=='kW': mult=1e3
            elif self.cbx_Pmax.currentText()=='W': mult=1
            elif self.cbx_Pmax.currentText()=='mW': mult=1e-3
                    
        elif fila==3 and columna==1: #DGA
            if self.cbx_DGA.currentText()=='m': mult=1e3
            elif self.cbx_DGA.currentText()=='cm': mult=10
            elif self.cbx_DGA.currentText()=='mm': mult=1
            
        elif fila==3 and columna==0: #DCA
            if self.cbx_DCA.currentText()=='m': mult=1e3
            elif self.cbx_DCA.currentText()=='cm': mult=10
            elif self.cbx_DCA.currentText()=='mm': mult=1
            
        else:
            mult=1
            
        return mult
        
    def datosAventana(self): 
        # Establecer el tipo de línea y tipo de parametros 
        self.cbx_perdidaslinea.setCurrentText(self.datos[0][0])
        
        if self.cbx_perdidaslinea.currentText()=='Sin pérdidas':
            self.cbx_tipocoero.show()
            self.lbl_modolinea.hide()
            self.cbx_modolinea.hide()
            self.cbx_tipocoero.setCurrentText(self.datos[1][0])
                        
        elif self.cbx_perdidaslinea.currentText()=='Pérdidas generales':
            self.cbx_tipocoero.hide()
            self.lbl_modolinea.show()
            self.cbx_modolinea.show()
            self.cbx_modolinea.setCurrentText(self.datos[1][0])
            
        # Eliminar Widgets previos y crear los nuevos
        self.eliminar_diccionario_de_widgets()
        self.CrearWidgets()
        # Cargar los Widgets con la información
        self.linedit_DGA.setText(str(self.datos[3][1]))
        self.linedit_DCA.setText(str(self.datos[3][0]))
        self.linedit_Pmax.setText(str(self.datos[1][1]))
        self.cbx_DGA.setCurrentText('mm')
        self.cbx_DCA.setCurrentText('mm')
        self.cbx_Pmax.setCurrentText('W')
        self.linedit_DGA.setCursorPosition(0)
        self.linedit_DCA.setCursorPosition(0)
        self.linedit_Pmax.setCursorPosition(0)
                                
        if self.cbx_perdidaslinea.currentText()=='Sin pérdidas':
            # Tipo pérdidas
            # Tipocoero,Pmax
            # Ro,coero
            # DCA,DGA
            # fmin,fmax
            
            self.WL['linedit_Ro'].setText(str(self.datos[2][0]))
            self.WL['linedit_coero'].setText(str(self.datos[2][1]))
            self.WL['linedit_Ro'].setCursorPosition(0)
            self.WL['linedit_coero'].setCursorPosition(0)
                        
        elif self.cbx_perdidaslinea.currentText()=='Pérdidas generales':
                        
            if self.cbx_modolinea.currentText()=='Parámetros rlgc':
                # Tipo pérdidas
                # Modo,Pmax
                # r,l,g,c
                # DCA,DGA
                # fmin,fmax
                
                self.WL['linedit_r'].setText(str(self.datos[2][0]))
                self.WL['linedit_l'].setText(str(self.datos[2][1]))
                self.WL['linedit_g'].setText(str(self.datos[2][2]))
                self.WL['linedit_c'].setText(str(self.datos[2][3]))
                self.WL['linedit_r'].setCursorPosition(0)
                self.WL['linedit_l'].setCursorPosition(0)
                self.WL['linedit_g'].setCursorPosition(0)
                self.WL['linedit_c'].setCursorPosition(0)
                    
            elif self.cbx_modolinea.currentText()=='Tipo de línea de transmisión':
                # Tipo pérdidas
                # Modo,Pmax
                # 'Tipo LTx',dim1,dim2,urc,Dc,urd,erd,Dd
                # DCA,DGA
                # fmin,fmax
                self.WL['cbx_ltx'].setCurrentText(self.datos[2][0])
                        
                
    def bloquear(self):
        self.cvs.pbtn_configurar_linea.setEnabled(False)
        self.hide()
        
    def desbloquear(self):
        self.cvs.pbtn_configurar_linea.setEnabled(True)
        
    def NoGrafica(self): 
        self.cvs.Cgrafica.ocultar()
        self.cvs.Cbarra.ocultar()
        self.cvs.pbtn_figuras_merito.hide()
        self.cvs.lbl_todos_msmn.hide()
                
                
    ### Lógica de Cómputo
        
    def graficar(self):
        try:
            self.datos=self.formatear_datos(self.datos)
            if self.cvs.bandera=='buscar':
                if self.cvs.cbx_algoritmos.currentText()=='':
                    return
            
                elif self.cvs.cbx_algoritmos.currentText()=='Todos (comparación)':
                    Pmax=float(self.datos[1][1])
                    DCA=int(float(self.datos[3][0]))
                    DGA=int(float(self.datos[3][1]))
                    self.Alfa,self.Beta,self.Zc = self.calcularABZ(self.cvs.Fvisual)
                    
                    for nombre in self.cvs.algoritmos_a_graficar:
                        self.cvs.cvp.Buscadores[nombre].vectorD=vectordistancias(self.cvs.cvp.Buscadores[nombre].datos,DCA,DGA)
                        self.cvs.Cbarra.configurar(self.cvs.cvp.Buscadores[nombre].vectorD,self.cvs.cvp.Buscadores[nombre].posicion) 
                        self.cvs.cvp.Buscadores[nombre].Zins=self.cvs.cvp.Buscadores[nombre].calcularZins(self.cvs.Fvisual,self.Alfa,self.Beta,self.Zc)
                        
                        self.cvs.cvp.Buscadores[nombre].crear_grafica(self.cvs.cbx_tipografica.currentText(),
                                                                      self.cvs.cbx_presentaciongrafica.currentText(),
                                                                      self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                                                      self.Alfa,self.Beta,self.Zc,
                                                                      self.rlgc_vs_f,Pmax,DCA,DGA,
                                                                      self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                                      self.cvs.cvp.Buscadores[nombre].posicion_entrada_adaptador)
                    
                    self.cvs.Cgrafica.borrar()
                    self.cvs.Cgrafica.graficar()
                    self.cvs.Cbarra.ocultar()
                    self.cvs.pbtn_figuras_merito.show()
                    self.cvs.lbl_todos_msmn.show()
                    
                    if self.cvs.chkbx_Pmax.isChecked():
                        self.cvs.Cgrafica.quitar_linea_potencia()
                        try: self.cvs.Cgrafica.graficar_linea_potencia()
                        except: pass
                        
                        
                elif self.cvs.cbx_algoritmos.currentText()!='Todos (comparación)':
                    nombre=self.cvs.cbx_algoritmos.currentText()
                    Pmax=float(self.datos[1][1])
                    DCA=int(float(self.datos[3][0]))
                    DGA=int(float(self.datos[3][1]))
                    self.Alfa,self.Beta,self.Zc = self.calcularABZ(self.cvs.Fvisual)
                    
                    self.cvs.cvp.Buscadores[nombre].vectorD=vectordistancias(self.cvs.cvp.Buscadores[nombre].datos,DCA,DGA)
                    self.cvs.CgridStubs.determinar_posicion_entrada_adaptador()
                    self.cvs.Cbarra.configurar(self.cvs.cvp.Buscadores[nombre].vectorD,self.cvs.cvp.Buscadores[nombre].posicion) 
                    self.cvs.cvp.Buscadores[nombre].Zins=self.cvs.cvp.Buscadores[nombre].calcularZins(self.cvs.Fvisual,self.Alfa,self.Beta,self.Zc)
                    
                    self.cvs.cvp.Buscadores[nombre].crear_grafica(self.cvs.cbx_tipografica.currentText(),
                                                                  self.cvs.cbx_presentaciongrafica.currentText(),
                                                                  self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                                                  self.Alfa,self.Beta,self.Zc,
                                                                  self.rlgc_vs_f,Pmax,DCA,DGA,
                                                                  self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                                  self.cvs.Cbarra.posicion)
                    
                    self.cvs.Cgrafica.borrar()
                    self.cvs.Cgrafica.graficar()
                    if self.cvs.cbx_tipografica.currentText()=='Respuesta en frecuencia': self.cvs.Cbarra.ocultar()
                    else: self.cvs.Cbarra.mostrar()
                    self.cvs.pbtn_figuras_merito.show()
                    
                    if self.cvs.chkbx_Pmax.isChecked():
                        self.cvs.Cgrafica.quitar_linea_potencia()
                        try: self.cvs.Cgrafica.graficar_linea_potencia()
                        except: pass
                    
                
            elif self.cvs.bandera=='graficar':
                Pmax=float(self.datos[1][1])
                DCA=int(float(self.datos[3][0]))
                DGA=int(float(self.datos[3][1]))
                self.Alfa,self.Beta,self.Zc = self.calcularABZ(self.cvs.Fvisual)
                
                self.cvs.vectorD=vectordistancias(self.cvs.CgridStubs.datos,DCA,DGA)
                self.cvs.CgridStubs.determinar_posicion_entrada_adaptador()
                self.cvs.Cbarra.configurar(self.cvs.vectorD,self.cvs.posicion) 
                self.cvs.CgridStubs.Zins=self.cvs.CgridStubs.calcularZins(self.cvs.Fvisual,self.Alfa,self.Beta,self.Zc)      
                self.cvs.crear_grafica(self.cvs.cbx_tipografica.currentText(),
                                       self.cvs.cbx_presentaciongrafica.currentText(),
                                       self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                       self.Alfa,self.Beta,self.Zc,
                                       self.rlgc_vs_f,Pmax,DCA,DGA,
                                       self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                       self.cvs.Cbarra.posicion)
                
                self.cvs.Cgrafica.borrar()
                self.cvs.Cgrafica.graficar()
                if self.cvs.cbx_tipografica.currentText()=='Respuesta en frecuencia': self.cvs.Cbarra.ocultar()
                else: self.cvs.Cbarra.mostrar()
                self.cvs.pbtn_figuras_merito.show()
                
                if self.cvs.chkbx_Pmax.isChecked():
                    self.cvs.Cgrafica.quitar_linea_potencia()
                    try: self.cvs.Cgrafica.graficar_linea_potencia()
                    except: pass
            
            self.cvs.lbl_revisar_parametros.hide()
        except:
            # import traceback
            # traceback.print_exc()
            self.NoGrafica()
            self.cvs.lbl_revisar_parametros.show()
                                     
    def determinar_fmin_fmax_datos(self): 
        
        if self.datos[0][0]=='Sin pérdidas' or self.datos[0][0]=='Pérdidas generales':
            self.datos[4]=[0,Infinity]
            self.fmin=0
            self.fmax=Infinity
            
                
    def datos_correcto(self, advertir=True):  #No verifica fmin,fmax
        try:
            if self.datos[0][0]=='Sin pérdidas':
                # Tipo pérdidas
                # Tipocoero,Pmax
                # Ro,coero
                # DCA,DGA
                # fmin,fmax
                if float(self.datos[2][0]) <= 0: #Ro
                    if advertir:
                        ad=adv('La resistencia característica de la\nlínea debe ser mayor que cero.')
                        ad.exec()
                    return False
                    
                if self.datos[1][0]=='Capacitancia distribuida (pF/m)':
                    if float(self.datos[2][1]) <= 0: #coero
                        if advertir:
                            ad=adv('La capacitancia distribuida de la\nlínea debe ser mayor que cero.')
                            ad.exec()
                        return False
                    
                elif self.datos[1][0]=='Constante dieléctrica relativa': 
                    if float(self.datos[2][1]) < 1: #coero
                        if advertir:
                            ad=adv('La constante dieléctrica relativa de la\nlínea debe ser mayor o igual a uno.')
                            ad.exec()
                        return False
                                           
                elif self.datos[1][0]=='Velocidad de propagación (%)': 
                    if (float(self.datos[2][1])<=0) or (float(self.datos[2][1])>100): #coero
                        if advertir:
                            ad=adv('La velocidad de propagación en la\nlínea debe ser mayor que 0 %\ny menor o igual a 100 %.')
                            ad.exec()
                        return False
                else:
                    return False
        
                                
            elif self.datos[0][0]=='Pérdidas generales':
                if self.datos[1][0]=='Parámetros rlgc':
                    # Tipo pérdidas
                    # Modo,Pmax
                    # r,l,g,c
                    # DCA,DGA
                    # fmin,fmax
                    if float(self.datos[2][0]) < 0: #r
                        if advertir:
                            ad=adv('La resistencia distribuida de la\nlínea debe ser positiva.')
                            ad.exec()
                        return False
                    
                    if float(self.datos[2][1]) <= 0: #l
                        if advertir:
                            ad=adv('La inductancia distribuida de la\nlínea debe ser mayor o igual que cero.')
                            ad.exec()
                        return False
                    
                    if float(self.datos[2][2]) < 0: #g
                        if advertir:
                            ad=adv('La conductancia distribuida de la\nlínea debe ser positiva.')
                            ad.exec()
                        return False
                    
                    if float(self.datos[2][3]) <= 0: #c
                        if advertir:
                            ad=adv('La capacitancia distribuida de la\nlínea debe ser mayor o igual que cero.')
                            ad.exec()
                        return False
    
                elif self.datos[1][0]=='Tipo de línea de transmisión':
                    # Tipo pérdidas
                    # Modo,Pmax
                    # 'Tipo LTx',dim1,dim2,urc,Dc,urd,erd,Dd
                    # DCA,DGA
                    # fmin,fmax
                    if float(self.datos[2][1])<=0 or float(self.datos[2][2])<=0:
                        if advertir:
                            ad=adv('Las dimensiones de la línea\ndeben ser mayores que cero.')
                            ad.exec()
                        return False
                    
                    if not self.dim_LTx_correcto(): return False
                    
                    if float(self.datos[2][3]) < 1: #urc
                        if advertir:
                            ad=adv('La permeabilidad magnética relativa de los\nconductores de la línea debe ser\nmayor o igual a uno.')
                            ad.exec()
                        return False
                    
                    if float(self.datos[2][4]) <= 0 : #Dc
                        if advertir:
                            ad=adv('La conductividad de los conductores de\nla línea debe ser mayor que cero.')
                            ad.exec()
                        return False
                    
                    if float(self.datos[2][5]) < 1: #urd
                        if advertir:
                            ad=adv('La permeabilidad magnética relativa\ndel dieléctrico de la línea debe ser\nmayor o igual a uno.')
                            ad.exec()
                        return False
                    
                    if float(self.datos[2][6]) < 1: #erd
                        if advertir:
                            ad=adv('La permitividad eléctrica relativa\ndel dieléctrico de la línea debe ser\nmayor o igual a uno.')
                            ad.exec()
                        return False
                    
                    if float(self.datos[2][7]) < 0 : #Dd
                        if advertir:
                            ad=adv('La conductividad del dieléctrico de\nla línea debe ser positiva.')
                            ad.exec()
                        return False
                    
                else:
                    return False
                            
            else:
                return False
            
            if float(self.datos[1][1]) < 0: #Pmax
                if advertir:
                    ad=adv('La potencia máxima de la línea\ndebe ser mayor que cero.')
                    ad.exec()
                return False
            

            if float(self.datos[3][0]) < 0: #DCA
                if advertir:
                    ad=adv('La distancia DCA debe ser positiva.')
                    ad.exec()
                return False
                
            if float(self.datos[3][1]) < 0: #DGA
                if advertir:
                    ad=adv('La distancia DGA debe ser positiva.')
                    ad.exec()
                return False
        
        except:
            if advertir:
                ad=adv('Ingrese correctamente los parámetros\nde la línea de transmisión.')
                ad.exec()
            return False
        
        return True
            
    def dim_LTx_correcto(self,advertir=True): 
        if self.datos[0][0] == 'Pérdidas generales' and self.datos[1][0] == 'Tipo de línea de transmisión': pass
        else:return False
        
        try:
            if self.datos[2][0]=='Coaxial': 
                if float(self.datos[2][1]) >= float(self.datos[2][2]): #a>=b
                    if advertir:
                        ad=adv('En la línea, el radio del conductor interno\ndebe ser menor que el radio del conductor externo.')
                        ad.exec()
                    return False
           
            elif self.datos[2][0]=='Bifilar':
                if float(self.datos[2][1]) >= float(self.datos[2][2])/2: #a>=d/2
                    if advertir:
                        ad=adv('En la línea, la separación entre los\nconductores debe ser mayor que\nel diámetro de éstos.')
                        ad.exec()
                    return False
                
            elif self.datos[2][0]=='Plana':
                pass
            
            else:
                return False
        except:
            return False
        
        return True
    
    def formato_correcto(self,datos): 
        if len(datos) == 5: 
            if len(datos[1]) != 2: return False
            if len(datos[3]) != 2: return False
            if len(datos[4]) != 2: return False
            
            if datos[0][0]=='Sin pérdidas':
                if datos[1][0]=='Capacitancia distribuida (pF/m)': pass
                elif datos[1][0]=='Constante dieléctrica relativa': pass                                         
                elif datos[1][0]=='Velocidad de propagación (%)': pass
                else: return False
                
                if len(datos[2]) != 2: return False
                                
            elif datos[0][0]=='Pérdidas generales':
                if datos[1][0]=='Parámetros rlgc':
                    if len(datos[2]) != 4: return False
                    
                elif datos[1][0]=='Tipo de línea de transmisión':
                    if len(datos[2]) != 8: return False
                    
                else:
                    return False
                    
            else:
                return False
        else: 
            return False
        
        return True
    
    def calcularABZ(self,F): 
        self.datos=self.formatear_datos(self.datos)
        Zc=[]
        Alfa=[]
        Beta=[]
        if self.cbx_perdidaslinea.currentText()=='Sin pérdidas':
            # Tipo pérdidas
            # Tipocoero,Pmax
            # Ro,coero
            # DCA,DGA
            # fmin,fmax
            
            rvf,lvf,gvf,cvf,Alfa,Beta,Zc=rlgc_ABZ_sinPerdidas(F,self.datos[1][0],self.datos[2][1],self.datos[2][0]) #(F,tipocoero,coero,Ro)
                        
        elif self.cbx_perdidaslinea.currentText()=='Pérdidas generales':
            if self.cbx_modolinea.currentText()=='Parámetros rlgc':
                # Tipo pérdidas
                # Modo,Pmax
                # r,l,g,c
                # DCA,DGA
                # fmin,fmax
                
                rvf,lvf,gvf,cvf,Alfa,Beta,Zc=rlgc_ABZ_perdidasGenerales(F,self.datos[2][0],self.datos[2][1],self.datos[2][2],self.datos[2][3])#(F,r,l,g,c)
                
   
            elif self.cbx_modolinea.currentText()=='Tipo de línea de transmisión':
                # Tipo pérdidas
                # Modo,Pmax
                # 'Tipo LTx',dim1,dim2,urc,Dc,urd,erd,Dd
                # DCA,DGA
                # fmin,fmax

                #F,tipoltx,dim1,dim2,urc,Dc,urd,erd,Dd)
                rvf,lvf,gvf,cvf,Alfa,Beta,Zc=rlgc_ABZ_Ltx(F,self.datos[2][0],self.datos[2][1],self.datos[2][2],self.datos[2][3],self.datos[2][4],self.datos[2][5],self.datos[2][6],self.datos[2][7])
        
        self.rlgc_vs_f['r']=rvf
        self.rlgc_vs_f['l']=lvf
        self.rlgc_vs_f['g']=gvf
        self.rlgc_vs_f['c']=cvf
        
        return Alfa,Beta,Zc
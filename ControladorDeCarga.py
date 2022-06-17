# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

from Funciones import ZCARGA
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QFileDialog
import csv
import os.path
from Advertencia import adv
from numpy import Infinity
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QLabel,QLineEdit,QComboBox,QMainWindow
from PyQt5.QtGui import QPixmap
from functools import partial
import traceback
from ventana_carga_ui import Ui_MainWindow as VentanaCarga
from cmath import tanh as complextanh

        
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
        

class ControladorDeCarga(QMainWindow,VentanaCarga):
    def __init__(self,ventana_principal):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setWindowTitle('Configurar impedancia de carga')
        
        self.cvp=ventana_principal
        
        self.lbl_importado.hide()
        self.WI=dict() # diccionario de los widgets de impedancia
        self.WI['lbl_R']=self.lbl_R
        self.WI['linedit_R']=self.linedit_R
        self.WI['linedit_R'].setValidator(QDoubleValidator())
        self.WI['linedit_R'].setAlignment(Qt.AlignLeft)
        self.WI['lbl_R'].setAlignment(Qt.AlignRight)
        self.WI['cbx_R']=self.cbx_R
        self.layout_impedancia.setAlignment(Qt.AlignTop)
        self.WI['cbx_R'].setCurrentText('Ω')
        
        self.Z=[]
        self.Z_original=[]
        self.Zprima=[]
        self.fmin=None
        self.fmax=None
        self.datos=self.plantilla_datos()
        self.ignorar_senhales=False

        #Conexiones
        self.linedit_R.editingFinished.connect(partial(self.editing_finished,'R',2,0))
        self.cbx_modelo.currentTextChanged.connect(self.accionmodelo)
        self.actionCargarModelo.triggered.connect(self.cargar_modelo)
        self.actionCargarArchivo_imp.triggered.connect(self.cargar_archivo_imp)
        self.actionGuardarModelo.triggered.connect(self.guardar_modelo)
        self.actionReiniciar.triggered.connect(self.reiniciar)
        
        self.pbtn_ok.clicked.connect(self.salir)
        
    ### Lógica de Interfaz Grafica
        
    def plantilla_datos(self,tipo='Modelo',n=None,modelo='R'): 
        
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
        
    def closeEvent(self, event): 
        self.salir()
        
    def salir(self): 
        self.hide()
        self.cvp.pbtn_configurar_carga.setEnabled(True)

    def cargar_modelo(self): 
        try:
            carpeta='./Datos/Carga'
            ruta = QFileDialog.getOpenFileName(self, 'Cargar archivo',carpeta,"*.modelimp")[0]
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
            # import traceback
            # traceback.print_exc()
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos.')
            ad.exec_()
            self.ignorar_senhales=False
            self.reiniciar()
            
    def cargar_archivo_imp(self): 
        try:
            carpeta='./Datos/Carga'
            ruta = QFileDialog.getOpenFileName(self, 'Cargar archivo',carpeta,"*.imp")[0]
            if os.path.exists(ruta):
                archivo_imp=[]
                with open(ruta) as archivo:
                    lector = csv.reader(archivo, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    for fila in lector: archivo_imp.append(fila)
                    
                if self.formato_correcto(archivo_imp): pass
                else: raise Exception

                self.datos=archivo_imp 
                self.determinar_fmin_fmax_datos()
                            
                self.ignorar_senhales=True
                self.datosAventana()
                self.ignorar_senhales=False
                
                self.WI['linedit_R'].setEnabled(False)
                self.WI['cbx_R'].setEnabled(False)
                           
        except:
            # import traceback
            # traceback.print_exc()
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos.')
            ad.exec_()
            self.ignorar_senhales=False
            self.WI['linedit_R'].setEnabled(True)
            self.WI['cbx_R'].setEnabled(True)
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
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos de\nla impedancia de carga.')
            ad.exec_()
            self.ignorar_senhales=False
            self.reiniciar()
    
    def formatear_datos(self,datos): 
        tipo=datos[0][0]
        n=int(datos[0][1])
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
    
    def guardar_modelo(self): 
        # Tipo:Modelo,n
        # Modelo: R-s-L-s-C
        # R
        # L
        # C
        # fmin,fmax
        
        if self.datos[0][0]=='Archivo': self.datos=self.plantilla_datos()
                    
        carpeta='./Datos/Carga'
        ruta = QFileDialog.getSaveFileName(self,'Guardar archivo',carpeta,'*.modelimp')[0]
        if ruta!='':
            if ruta[-9:] != '.modelimp': ruta=ruta+'.modelimp'
            with open(ruta,'w',newline='') as archivo:
                escritor = csv.writer(archivo)
                for fila in self.datos:
                    escritor.writerow(fila)
                    
    def reiniciar(self): 
        self.datos=self.plantilla_datos()
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
        
    def CrearWidgets(self): 
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
            self.WI['linedit_R'].editingFinished.connect(partial(self.editing_finished,'R',2,0))
            self.WI['linedit_R'].textChanged.connect(partial(self.text_changed,self.WI['linedit_R'],2,0))
            self.WI['cbx_R'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'R',2,0))
            
            pixmap = QPixmap('./imagenes_impedancias/impedancia_carga/R.png')
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
            self.WI['linedit_R'].editingFinished.connect(partial(self.editing_finished,'R',2,0))
            self.WI['linedit_R'].textChanged.connect(partial(self.text_changed,self.WI['linedit_R'],2,0))
            self.WI['cbx_R'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'R',2,0))
            
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
            self.WI['linedit_L'].editingFinished.connect(partial(self.editing_finished,'L',3,0))
            self.WI['linedit_L'].textChanged.connect(partial(self.text_changed,self.WI['linedit_L'],3,0))
            self.WI['cbx_L'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'L',3,0))
            
            if (self.cbx_modelo.currentText()=='R-s-L'): pixmap = QPixmap('./imagenes_impedancias/impedancia_carga/R-s-L.png')
            elif (self.cbx_modelo.currentText()=='R-p-L'): pixmap = QPixmap('./imagenes_impedancias/impedancia_carga/R-p-L.png')
            
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
            self.WI['linedit_R'].editingFinished.connect(partial(self.editing_finished,'R',2,0))
            self.WI['linedit_R'].textChanged.connect(partial(self.text_changed,self.WI['linedit_R'],2,0))
            self.WI['cbx_R'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'R',2,0))
            
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
            self.WI['linedit_C'].editingFinished.connect(partial(self.editing_finished,'C',3,0))
            self.WI['linedit_C'].textChanged.connect(partial(self.text_changed,self.WI['linedit_C'],3,0))
            self.WI['cbx_C'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'C',3,0))
            
            if (self.cbx_modelo.currentText()=='R-s-C'): pixmap = QPixmap('./imagenes_impedancias/impedancia_carga/R-s-C.png')
            elif (self.cbx_modelo.currentText()=='R-p-C'): pixmap = QPixmap('./imagenes_impedancias/impedancia_carga/R-p-C.png')
            
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
                                self.WI['linedit_R'].editingFinished.connect(partial(self.editing_finished,'R',2,0))
                                self.WI['linedit_R'].textChanged.connect(partial(self.text_changed,self.WI['linedit_R'],2,0))
                                self.WI['cbx_R'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'R',2,0))
                                
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
                                self.WI['linedit_L'].editingFinished.connect(partial(self.editing_finished,'L',3,0))
                                self.WI['linedit_L'].textChanged.connect(partial(self.text_changed,self.WI['linedit_L'],3,0))
                                self.WI['cbx_L'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'L',3,0))
                                
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
                                self.WI['linedit_C'].editingFinished.connect(partial(self.editing_finished,'C',4,0))
                                self.WI['linedit_C'].textChanged.connect(partial(self.text_changed,self.WI['linedit_C'],4,0))
                                self.WI['cbx_C'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'C',4,0))
                                
                                if(self.cbx_modelo.currentText()=='R-s-L-s-C'): pixmap=QPixmap('./imagenes_impedancias/impedancia_carga/R-s-L-s-C.png')
                                elif(self.cbx_modelo.currentText()=='R-p-L-p-C'): pixmap=QPixmap('./imagenes_impedancias/impedancia_carga/R-p-L-p-C.png')
                                elif(self.cbx_modelo.currentText()=='R-s-(L-p-C)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_carga/R-s-(L-p-C).png')
                                elif(self.cbx_modelo.currentText()=='R-p-(L-s-C)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_carga/R-p-(L-s-C).png')
                                elif(self.cbx_modelo.currentText()=='L-s-(R-p-C)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_carga/L-s-(R-p-C).png')
                                elif(self.cbx_modelo.currentText()=='L-p-(R-s-C)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_carga/L-p-(R-s-C).png')
                                elif(self.cbx_modelo.currentText()=='C-s-(R-p-L)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_carga/C-s-(R-p-L).png')
                                elif(self.cbx_modelo.currentText()=='C-p-(R-s-L)'): pixmap=QPixmap('./imagenes_impedancias/impedancia_carga/C-p-(R-s-L).png')
                                
                                self.lbl_modelo.setPixmap(pixmap)
            
        elif self.cbx_modelo.currentText()=='Antena Microstrip':
            self.WI['lbl_L1']=QLabel('L1:',alignment=Qt.AlignRight)
            self.WI['lbl_L1'].setStyleSheet(self.cvp.SS_lbl)
            self.WI['lbl_L1'].setMinimumWidth(75)
            self.WI['lbl_L1'].setFixedHeight(20)
            self.WI['linedit_L1']=QLineEdit(alignment=Qt.AlignLeft)
            self.WI['linedit_L1'].setStyleSheet(self.cvp.SS_linedit)
            self.WI['linedit_L1'].setMinimumWidth(69)
            self.WI['linedit_L1'].setMaximumWidth(69)
            self.WI['linedit_L1'].setFixedHeight(20)
            self.WI['linedit_L1'].setValidator(QDoubleValidator())
            self.WI['cbx_L1']=QComboBox()
            self.WI['cbx_L1'].addItem('H')
            self.WI['cbx_L1'].addItem('mH')
            self.WI['cbx_L1'].addItem('μH') 
            self.WI['cbx_L1'].addItem('nH')
            self.WI['cbx_L1'].addItem('pH')
            self.WI['cbx_L1'].setCurrentText('nH')
            self.WI['cbx_L1'].setStyleSheet(self.cvp.SS_cbx_und)
            self.layout_impedancia.addWidget(self.WI['lbl_L1'],0,0)
            self.layout_impedancia.addWidget(self.WI['linedit_L1'],0,1)
            self.layout_impedancia.addWidget(self.WI['cbx_L1'],0,2)
            self.WI['linedit_L1'].editingFinished.connect(partial(self.editing_finished,'L1',2,0))
            self.WI['linedit_L1'].textChanged.connect(partial(self.text_changed,self.WI['linedit_L1'],2,0))
            self.WI['cbx_L1'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'L1',2,0))
            
            self.WI['lbl_C1']=QLabel('C1:',alignment=Qt.AlignRight)
            self.WI['lbl_C1'].setStyleSheet(self.cvp.SS_lbl)
            self.WI['lbl_C1'].setMinimumWidth(75)
            self.WI['lbl_C1'].setFixedHeight(20)
            self.WI['linedit_C1']=QLineEdit(alignment=Qt.AlignLeft)
            self.WI['linedit_C1'].setStyleSheet(self.cvp.SS_linedit)
            self.WI['linedit_C1'].setMinimumWidth(69)
            self.WI['linedit_C1'].setMaximumWidth(69)
            self.WI['linedit_C1'].setFixedHeight(20)
            self.WI['linedit_C1'].setValidator(QDoubleValidator())
            self.WI['cbx_C1']=QComboBox()
            self.WI['cbx_C1'].addItem('F')
            self.WI['cbx_C1'].addItem('mF')
            self.WI['cbx_C1'].addItem('μF') 
            self.WI['cbx_C1'].addItem('nF')
            self.WI['cbx_C1'].addItem('pF')
            self.WI['cbx_C1'].setCurrentText('pF')
            self.WI['cbx_C1'].setStyleSheet(self.cvp.SS_cbx_und)
            self.layout_impedancia.addWidget(self.WI['lbl_C1'],1,0)
            self.layout_impedancia.addWidget(self.WI['linedit_C1'],1,1)
            self.layout_impedancia.addWidget(self.WI['cbx_C1'],1,2)
            self.WI['linedit_C1'].editingFinished.connect(partial(self.editing_finished,'C1',3,0))
            self.WI['linedit_C1'].textChanged.connect(partial(self.text_changed,self.WI['linedit_C1'],3,0))
            self.WI['cbx_C1'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'C1',3,0))
            
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
            self.layout_impedancia.addWidget(self.WI['lbl_R'],2,0)
            self.layout_impedancia.addWidget(self.WI['linedit_R'],2,1)
            self.layout_impedancia.addWidget(self.WI['cbx_R'],2,2)
            self.WI['linedit_R'].editingFinished.connect(partial(self.editing_finished,'R',4,0))
            self.WI['linedit_R'].textChanged.connect(partial(self.text_changed,self.WI['linedit_R'],4,0))
            self.WI['cbx_R'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'R',4,0))
            
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
            self.layout_impedancia.addWidget(self.WI['lbl_L'],3,0)
            self.layout_impedancia.addWidget(self.WI['linedit_L'],3,1)
            self.layout_impedancia.addWidget(self.WI['cbx_L'],3,2)
            self.WI['linedit_L'].editingFinished.connect(partial(self.editing_finished,'L',5,0))
            self.WI['linedit_L'].textChanged.connect(partial(self.text_changed,self.WI['linedit_L'],5,0))
            self.WI['cbx_L'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'L',5,0))
            
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
            self.layout_impedancia.addWidget(self.WI['lbl_C'],4,0)
            self.layout_impedancia.addWidget(self.WI['linedit_C'],4,1)
            self.layout_impedancia.addWidget(self.WI['cbx_C'],4,2)
            self.WI['linedit_C'].editingFinished.connect(partial(self.editing_finished,'C',6,0))
            self.WI['linedit_C'].textChanged.connect(partial(self.text_changed,self.WI['linedit_C'],6,0))
            self.WI['cbx_C'].currentTextChanged.connect(partial(self.accion_cbx_unidades,'C',6,0))
            
            pixmap = QPixmap('./imagenes_impedancias/impedancia_carga/microstrip.png')
            self.lbl_modelo.setPixmap(pixmap)

    def accionmodelo(self): 
        if self.ignorar_senhales: return
        self.lbl_importado.hide()
        
        self.eliminar_diccionario_de_widgets()
        self.CrearWidgets()

        self.datos=self.plantilla_datos(tipo='Modelo',modelo=self.cbx_modelo.currentText())
        
    def accion_cbx_unidades(self,key,fila,columna): 
        if self.ignorar_senhales: return
        
        if key=='R':
            if self.WI['cbx_'+key].currentText()=='kΩ': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='Ω': mult=1
            elif self.WI['cbx_'+key].currentText()=='mΩ': mult=1e-3
            try: self.datos[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
            
        elif key=='L':
            if self.WI['cbx_'+key].currentText()=='H': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='mH': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='μH': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='nH': mult=1
            elif self.WI['cbx_'+key].currentText()=='pH': mult=1e-3
            try: self.datos[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
        
        elif key=='C':
            if self.WI['cbx_'+key].currentText()=='F': mult=1e12
            elif self.WI['cbx_'+key].currentText()=='mF': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='μF': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='nF': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='pF': mult=1
            try: self.datos[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
        
        elif key=='L1':
            if self.WI['cbx_'+key].currentText()=='H': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='mH': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='μH': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='nH': mult=1
            elif self.WI['cbx_'+key].currentText()=='pH': mult=1e-3
            try: self.datos[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
        
        elif key=='C1':
            if self.WI['cbx_'+key].currentText()=='F': mult=1e12
            elif self.WI['cbx_'+key].currentText()=='mF': mult=1e9
            elif self.WI['cbx_'+key].currentText()=='μF': mult=1e6
            elif self.WI['cbx_'+key].currentText()=='nF': mult=1e3
            elif self.WI['cbx_'+key].currentText()=='pF': mult=1
            try: self.datos[fila][columna]=float(self.WI['linedit_'+key].text())*mult
            except: pass
        
    def text_changed(self,linedit,fila,columna):
        if self.ignorar_senhales:
            self.datos[fila][columna]=linedit.text()
        else:
            self.ignorar_senhales=True
            self.datos[fila][columna]=linedit.text()
            self.ignorar_senhales=False

    def editing_finished(self,key,fila,columna): 
        if self.ignorar_senhales: return
        self.WI['linedit_'+key].setCursorPosition(0)
        try: self.datos[fila][columna]=float(self.WI['linedit_'+key].text())*self.multiplicador(key)
        except: pass
        
    def multiplicador(self,key): 
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
    
    def datosAventana(self): 
        
        if self.datos[0][0]=='Modelo':
            # Tipo:Modelo,n
            # Modelo: R-s-L-s-C
            # R
            # L
            # C
            # fmin,fmax
            
            self.lbl_importado.hide()
            
            # Establecer el modelo
            self.cbx_modelo.setCurrentText(self.datos[1][0])
            
            # Eliminar Widgets previos y crear los nuevos
            self.eliminar_diccionario_de_widgets()
            self.CrearWidgets()
            
            # Cargar los Widgets con la información
            if (self.cbx_modelo.currentText()=='R'):
                self.WI['linedit_R'].setText(str(self.datos[2][0]))
                self.WI['linedit_R'].setCursorPosition(0)
                
            elif (self.cbx_modelo.currentText()=='L'):
                self.WI['linedit_L'].setText(str(self.datos[2][0]))
                self.WI['linedit_L'].setCursorPosition(0)
                
            elif (self.cbx_modelo.currentText()=='C'):
                self.WI['linedit_C'].setText(str(self.datos[2][0]))
                self.WI['linedit_C'].setCursorPosition(0)
                
            elif (self.cbx_modelo.currentText()=='R-s-L')or(self.cbx_modelo.currentText()=='R-p-L'):
                self.WI['linedit_R'].setText(str(self.datos[2][0]))
                self.WI['linedit_L'].setText(str(self.datos[3][0]))
                self.WI['linedit_R'].setCursorPosition(0)
                self.WI['linedit_L'].setCursorPosition(0)
                
            elif (self.cbx_modelo.currentText()=='R-s-C')or(self.cbx_modelo.currentText()=='R-p-C'):
                self.WI['linedit_R'].setText(str(self.datos[2][0]))
                self.WI['linedit_C'].setText(str(self.datos[3][0]))
                self.WI['linedit_R'].setCursorPosition(0)
                self.WI['linedit_C'].setCursorPosition(0)
                
            elif (self.cbx_modelo.currentText()=='L-s-C')or(self.cbx_modelo.currentText()=='L-p-C'):
                self.WI['linedit_L'].setText(str(self.datos[2][0]))
                self.WI['linedit_C'].setText(str(self.datos[3][0]))
                self.WI['linedit_L'].setCursorPosition(0)
                self.WI['linedit_C'].setCursorPosition(0)
    
            elif (self.cbx_modelo.currentText()=='R-s-L-s-C')or(self.cbx_modelo.currentText()=='R-p-L-p-C')or(
                    self.cbx_modelo.currentText()=='R-s-(L-p-C)')or(self.cbx_modelo.currentText()=='R-p-(L-s-C)')or(
                        self.cbx_modelo.currentText()=='L-s-(R-p-C)')or(self.cbx_modelo.currentText()=='L-p-(R-s-C)')or(
                            self.cbx_modelo.currentText()=='C-s-(R-p-L)')or(self.cbx_modelo.currentText()=='C-p-(R-s-L)'):
                                self.WI['linedit_R'].setText(str(self.datos[2][0]))
                                self.WI['linedit_L'].setText(str(self.datos[3][0]))
                                self.WI['linedit_C'].setText(str(self.datos[4][0]))
                                self.WI['linedit_R'].setCursorPosition(0)
                                self.WI['linedit_L'].setCursorPosition(0)
                                self.WI['linedit_C'].setCursorPosition(0)
            
            elif self.cbx_modelo.currentText()=='Antena Microstrip':
                self.WI['linedit_L1'].setText(str(self.datos[2][0]))
                self.WI['linedit_C1'].setTextstr((self.datos[3][0]))
                self.WI['linedit_R'].setText(str(self.datos[4][0]))
                self.WI['linedit_L'].setText(str(self.datos[5][0]))
                self.WI['linedit_C'].setText(str(self.datos[6][0]))
                self.WI['linedit_L1'].setCursorPosition(0)
                self.WI['linedit_C1'].setCursorPosition(0)
                self.WI['linedit_R'].setCursorPosition(0)
                self.WI['linedit_L'].setCursorPosition(0)
                self.WI['linedit_C'].setCursorPosition(0)
                
        elif self.datos[0][0]=='Archivo':
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
            self.CrearWidgets()
                        
            self.lbl_importado.show()
            
    def bloquear(self):
        self.cvp.pbtn_configurar_carga.setEnabled(False)
        self.hide()
    
    def desbloquear(self):
        self.cvp.pbtn_configurar_carga.setEnabled(True)
    
    ### Lógica de Cómputo
            
    def determinar_fmin_fmax_datos(self): 
        if self.datos[0][0]=='Modelo':
            self.datos[-1]=[0,Infinity]
            self.fmin=0
            self.fmax=Infinity
            
        elif self.datos[0][0]=='Archivo':
            try:
                fmin=Infinity
                fmax=0
                for n  in range(1,int(self.datos[0][1])+1):
                    f=float(self.datos[n][0])
                    if f > fmax: fmax=f
                    if f < fmin: fmin=f
                    
                self.datos[-1]=[fmin,fmax]
                self.fmin=fmin
                self.fmax=fmax
                
            except:
                self.datos[-1]=['','']
                self.fmin=None
                self.fmax=None
    
    def datos_correcto(self, advertir=True):  #No verifica fmin,fmax
        try:
            if self.datos[0][0]=='Modelo':
                # tipo:modelo,n
                # modelo:Antena Microstrip
                # L1
                # C1
                # R
                # L
                # C
                # fmin,fmax
                
                for i in range(2,int(self.datos[0][1])):
                    if float(self.datos[i][0]) <= 0: #L1,C1,R,L,C
                        if advertir:
                            ad=adv('El valor de cada elemento de la impedancia\nde carga debe ser mayor que cero.')
                            ad.exec()
                        return False
                    
            elif self.datos[0][0]=='Archivo':
                # tipo:Archivo,n
                # f1,r1,x1
                # f2,r2,x2
                # ...
                # fn,rn,xn
                # fmin,fmax
                
                if int(self.datos[0][1]) != (len(self.datos)-2):
                    if advertir:
                        ad=adv('Error en el contenido del archivo\nde la impedancia de carga.')
                        ad.exec()
                    return False
                
                for i in range(1,int(self.datos[0][1])+1):
                    if float(self.datos[i][0]) <= 0: #f
                        if advertir:
                            ad=adv('El archivo .imp de la impedancia de carga\ncontiene valores incorrectos de frecuencia.')
                            ad.exec()
                        return False
                    
                    if float(self.datos[i][1]) < 0: #r
                        if advertir:
                            ad=adv('El archivo .imp de la impedancia de carga\ncontiene valores incorrectos de resistencia.')
                            ad.exec()
                        return False
                
        except:
            
            if advertir:
                ad=adv('Ingrese correctamente los parámetros\nde la carga.')
                ad.exec()
            return False
        
        return True
    
    def formato_correcto(self,datos): 
        if datos[0][0]=='Modelo':
            if self.cbx_modelo.findText(datos[1][0]) == -1: return False
            
            n=int(datos[0][1])
            if len(datos) != (n+1): return False
            if len(datos[-1]) != 2: return False
            
        elif datos[0][0]=='Archivo':
            n=int(datos[0][1])
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
        
        for i in range(1,int(self.datos[0][1])+1):
            z=float(self.datos[i][1])+j*float(self.datos[i][2])
            f=float(self.datos[i][0])
            z_vs_f[0].append(z)
            z_vs_f[1].append(f)
            
        return z_vs_f
        
    def calcularZ(self,F): 
        self.datos=self.formatear_datos(self.datos)
        Z=[]
        if self.datos[0][0]=='Modelo': Z=ZCARGA(F,self.datos,None)
        elif self.datos[0][0]=='Archivo': Z=ZCARGA(F,self.datos,self.z_vs_f())  
        return Z
    
    def calcularZprima(self,Z,DCA,Alfa,Beta,Zc,F): 
        dca=int(float(DCA))*1e-3 # en [m]
        if dca > 0:
            Zprima=[]
            j=complex(0+1j)
            for indf in range(len(F)):
                zcarga=Z[indf]
                alfa=Alfa[indf]
                beta=Beta[indf]
                zc=Zc[indf]
                
                Zprima.append(zc*((zcarga+zc*complextanh((alfa+j*beta)*dca))/(zc+zcarga*complextanh((alfa+j*beta)*dca))))
                
            return Zprima
        else:
            return Z
# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve


Para agregar nuevos algoritmos de optimización, modificar:
ventanaPrincipal.ui
ControladorDeObjetivo.py
AlgoritmosDeOptimizacion.py

"""
from multiprocessing import freeze_support
import ctypes

puntosdefrecuencia=101 #201
PIRAmin=0 #Porcentaje de Incumplimiento del Requerimiento de Adaptacion minimo. PIRAmin=0 es criterio Estricto (100% PCRA)
          #se aumenta la cantidad de stubs hasta alcanzar la PIRAmin, o hasta alcanzarse Nmax.

M=5   # La línea de transmión es de parámetros distribuídos, pero se aproxima a muchas celdas de parametros concentrados
      # conectadas en cascada. M es en número de celdas que hay en una longitud de onda, tomando como referencia la 
      # longitud de onda menor correspondiente a la frecuencia mayor en el rango de frecuencia bajo estudio.
      # En un criterio basado en pruebas, M=200 arrojó error relativo de 1.08% respecto a graficas arrojadas por ADS.

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel

from ventanaSecundaria_ui import Ui_Dialog as Ui_ventanaSecundaria
from ventanaPrincipal_ui import Ui_MainWindow as Ui_ventanaPrincipal

from ControladorDeObjetivo import ControladorDeObjetivo
from ControladorDeCarga import ControladorDeCarga
from ControladorDeLinea import ControladorDeLinea
from ControladorDeRequerimientosDeStubs import ControladorDeRequerimientosDeStubs
from ControladorDeGenerador import ControladorDeGenerador
from AlgoritmosDeOptimizacion import Buscador

from ControladorDeCuadriculaDeStubs import ControladorDeCuadriculaDeStubs
from ControladorDeLineaVentanaSecundaria import ControladorDeLineaVentanaSecundaria
from ControladorDeBarra import ControladorDeBarra
from Coleccion import Coleccion
from ControladorDeGrafica import ControladorDeGrafica

from Funciones import mod_Gamma,complex_Z,fase_H_rad


from PyQt5.QtCore import QThread,pyqtSignal,QObject
from functools import partial
import threading
from PyQt5.QtGui import QDoubleValidator
from PyQt5.QtWidgets import QAction



from Funciones import vectordistancias,copia_matriz,copia_dic,copia_lista,funcion_vista_d,descubrir_puntos_supera_Pmax

from Funciones import perdida_Zo_fo, max_perdida_Zo, perdida_conj_fo, max_perdida_conj
from Funciones import distorsion_fase, rizado, gamma_fo ,max_gamma, adaptacion_gamma

from Coleccion import Coleccion
from ControladorDeVentanaComparacionBuscar import ControladorDeVentanaComparacionBuscar
from ControladorDeVentanaComparacionGraficar import ControladorDeVentanaComparacionGraficar
from ControladorDeVentanaMetadata import ControladorDeVentanaMetadata

from PyQt5.QtWidgets import QFileDialog
import csv
import os.path
import traceback
from PyQt5 import QtCore
from MensajeInicial import MensajeInicial
from time import sleep
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from numpy import linspace,Infinity

from Advertencia_salir import adv_salir
from Advertencia import adv



#StyleSheets
SS_lbl="""
        QLabel{
        color:rgb(238, 238, 238);
        font: 75 10pt "MS Shell Dlg 2";
        }
        QToolTip{ 
        background-color: rgb(79, 93, 108); 
        color: rgb(238, 238, 238); 
        border: black solid 2px;
        }
        """
        
SS_linedit="""
            QLineEdit{
            border:1px solid rgb(0, 0, 0);
            border-radius: 10px;
            color:rgb(238, 238, 238);
            font: 75 10pt "MS Shell Dlg 2";
            padding-left: 5px;
            padding-right: 5px;
            background-color: rgb(49, 58, 67);
            }
            QLineEdit:hover{
            border: 1px solid rgb(85,170,255);
            background-color:rgb(79, 93, 108);
            }
            QLineEdit:focus{
            border: 1px solid rgb(85,170,255);
            background-color:rgb(79, 93, 108);
            }
            """
            
SS_cbx="""
        QComboBox {
            border:1px solid rgb(0, 0, 0);
           	border-radius: 10px;
        	color:rgb(238, 238, 238);
        	font: 75 10pt "MS Shell Dlg 2";
        	background-color: rgb(49, 58, 67);
            padding-left: 10px
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
        
SS_cbx_und="""
            QComboBox {
                border:1px solid rgb(0, 0, 0);
               	border-radius: 10px;
            	color:rgb(238, 238, 238);
            	font: 75 10pt "MS Shell Dlg 2";
            	background-color: rgb(49, 58, 67);
                padding-left: 6px;
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

SS_pbtn="""
        QPushButton {
            border: 2px solid rgb(238, 238, 238);
            border-radius: 10px;
            background-color: rgb(49, 58, 67);
        	color:rgb(238, 238, 238);
        	font: 75 10pt "MS Shell Dlg 2";
        }
        QPushButton:pressed {
            background-color: rgb(85,170,255);
        	color:black;
        }
        QPushButton:flat {
            border: none; /* no border for a flat push button */
        }
        QPushButton:default {
            border-color: navy; /* make the default button prominent */
        }
        
        """
        
SS_Vbar="""
        QScrollBar:vertical {
           /* border: 2px solid black;*/
            background: rgb(49, 58, 67);
            width: 5px;
            margin: 20px 0 20px 0;
        }
        QScrollBar::handle:vertical {
            background: rgb(85,170,255);
            min-height: 10px;
        }
        QScrollBar::add-line:vertical {
            border: 1px black;
            background: black;
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        
        QScrollBar::sub-line:vertical {
            border: 1px black;
            background: black;
            height: 0px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
        
        QScrollBar::sub-page:vertical {
            background: rgb(79, 93, 108);
        }
        
        QScrollBar::add-page:vertical {
            background: rgb(79, 93, 108);
        }
        """


class VentanaSecundaria(QtWidgets.QDialog, Ui_ventanaSecundaria):
    
    def __init__(self,ventana_principal,bandera):
        QtWidgets.QDialog.__init__(self)
        QObject.__init__(self)
        self.setupUi(self)
        
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        
        self.setWindowOpacity(0.0)
        
        resolucion=ctypes.windll.user32
        ancho=resolucion.GetSystemMetrics(0)
        alto=resolucion.GetSystemMetrics(1)
        
        if ancho < 1024 :
            self.setMinimumWidth(ancho-18)
            self.setMaximumWidth(ancho-18)
            self.scllarea_master.setMinimumWidth(ancho-18)
            self.scllarea_master.setMaximumWidth(ancho-18)
            
        if alto < 768 :
            self.setMinimumHeight(alto-78)
            self.setMaximumHeight(alto-78)
            self.scllarea_master.setMinimumHeight(alto-78)
            self.scllarea_master.setMaximumHeight(alto-78) 
        
        self.move(0,0)  
        
        self.show()
        
        self.cvp=ventana_principal
        self.SS_lbl=self.cvp.SS_lbl
        self.SS_linedit=self.cvp.SS_linedit
        self.SS_pbtn=self.cvp.SS_pbtn
        self.SS_cbx=self.cvp.SS_cbx
        self.SS_Vbar=self.cvp.SS_Vbar
        self.bandera=bandera
        self.PIRAmin=self.cvp.PIRAmin
        self.puntos=self.cvp.puntos
        
        self.lbl_entrada_msmn.hide()
        self.chkbx_Pmax.hide()
        
        #Inicializar
        self.cbx_filtrar.setCurrentText('Mejor esfuerzo')
        self.cbx_presentaciongrafica.setCurrentText('Magnitud')
        self.linedit_fiv.setValidator(QDoubleValidator())
        self.linedit_fsv.setValidator(QDoubleValidator())
        self.Fvisual=None
        self.fiv=None
        self.fsv=None
        self.cbx_fiv.setCurrentText('MHz')
        self.cbx_fsv.setCurrentText('MHz')
        self.ignorar_senhales=False
        self.evento_salir=None # Usado solo en el caso de bandera=graficar
        self.FigurasDeMerito=dict()
        global M
        self.M=M
        self.lbl_todos_msmn.hide()
        self.lbl_no_hay_algoritmos.hide()
        self.lbl_revisar_parametros.hide()
        
        self.FigurasDeMerito['stubs']=0
        self.FigurasDeMerito['longitud']=0
        self.FigurasDeMerito['perdida_Zo_fo']=0.0
        self.FigurasDeMerito['max_perdida_Zo'], self.FigurasDeMerito['f_max_perdida_Zo']=0.0, 0.0
        self.FigurasDeMerito['perdida_conj_fo']=0.0
        self.FigurasDeMerito['max_perdida_conj'], self.FigurasDeMerito['f_max_perdida_conj']=0.0, 0.0
        self.FigurasDeMerito['distorsion_fase']=0.0
        self.FigurasDeMerito['rizado']=0.0
        self.FigurasDeMerito['gamma_fo']=0.0
        self.FigurasDeMerito['max_gamma'], self.FigurasDeMerito['f_max_gamma']=0.0, 0.0
        self.FigurasDeMerito['adaptacion_gamma']=0.0
        
        #Conexiones
        self.cbx_algoritmos.currentTextChanged.connect(self.accion_cbx_algoritmos)       
        self.cbx_tipografica.currentTextChanged.connect(self.accion_cbx_tipografica)
        self.cbx_presentaciongrafica.currentTextChanged.connect(self.accion_cbx_presentaciongrafica)
        self.chkbx_Pmax.stateChanged.connect(self.graficar_linea_potencia)
        
        self.linedit_fiv.editingFinished.connect(self.editing_finished_fiv)
        self.linedit_fsv.editingFinished.connect(self.editing_finished_fsv)
        self.linedit_fiv.textChanged.connect(self.text_changed_fiv)
        self.linedit_fsv.textChanged.connect(self.text_changed_fsv)
        
        self.cbx_fiv.currentTextChanged.connect(self.accion_cbx_fiv)
        self.cbx_fsv.currentTextChanged.connect(self.accion_cbx_fsv)
        self.pbtn_configurar_linea.clicked.connect(self.abrir_ventana_linea)
        
        self.pbtn_aplicar.clicked.connect(self.aplicar_frecuencia_celdas)
                
        self.grafica_inicial()
        
        
    ### Lógica de Interfaz Gráfica

    def grafica_inicial(self): 
        if self.bandera=='buscar': 
            self.Fvisual=self.cvp.F
            self.fiv=self.Fvisual[0]
            self.fsv=self.Fvisual[-1]
            
            self.ignorar_senhales=True
            self.linedit_fiv.blockSignals(True)
            self.linedit_fsv.blockSignals(True)
            self.linedit_fiv.setText(str(self.fiv))
            self.linedit_fiv.setCursorPosition(0)  
            self.cbx_fiv.setCurrentText('MHz')
            self.linedit_fsv.setText(str(self.fsv))
            self.linedit_fsv.setCursorPosition(0) 
            self.cbx_fsv.setCurrentText('MHz')
            self.linedit_fiv.blockSignals(False)
            self.linedit_fsv.blockSignals(False)
            self.ignorar_senhales=False
            
            
            if self.cbx_filtrar.currentText()=='Mejor esfuerzo': referencia=self.cvp.no_fallidos
            elif self.cbx_filtrar.currentText()=='Modo estricto': referencia=self.cvp.algoritmos_cumplen_req
            
            self.cbx_algoritmos.blockSignals(True)
                
            self.cbx_algoritmos.clear()
            for nombre in referencia: self.cbx_algoritmos.addItem(nombre)
            
            if len(referencia)>1:
                self.setWindowTitle('Gráficas')
                self.cbx_algoritmos.addItem('Todos (comparación)')
                self.algoritmos_a_graficar=copia_lista(referencia)
                
            elif len(referencia)==1:
                self.setWindowTitle('Gráfica')
                self.algoritmos_a_graficar=copia_lista(referencia)
                
                                    
            if self.cbx_algoritmos.count() > 1: self.cbx_algoritmos.setCurrentText('Todos (comparación)')
            elif self.cbx_algoritmos.count() == 1: self.cbx_algoritmos.setCurrentIndex(0)
            
            if self.cbx_algoritmos.count()==0: self.lbl_no_hay_algoritmos.show()
            else: self.lbl_no_hay_algoritmos.hide()
                
            self.cbx_algoritmos.blockSignals(False)
        
        
            self.pbtn_figuras_merito.hide()
            self.pbtn_figuras_merito.clicked.connect(self.ver_figuras_merito)
            
            if self.cbx_algoritmos.currentText()=='Todos (comparación)':
                self.lbl_filtrar.show()
                self.cbx_filtrar.show()
                self.cbx_filtrar.currentTextChanged.connect(self.accion_cbx_filtrar)
                
                self.CgridStubs=ControladorDeCuadriculaDeStubs(self)
                self.gpbx_stubs.setEnabled(False)
                self.Cbarra=ControladorDeBarra(self)
                self.Cbarra.ocultar()
                self.Cgrafica=ControladorDeGrafica(self)
                self.Clinea=ControladorDeLineaVentanaSecundaria(self)
                self.Clinea.cargar_datos(copia_matriz(self.cvp.Clinea.datos))
                 
                self.Clinea.Alfa=copia_lista(self.cvp.Clinea.Alfa)
                self.Clinea.Beta=copia_lista(self.cvp.Clinea.Beta)
                self.Clinea.Zc=copia_lista(self.cvp.Clinea.Zc)
                self.Clinea.rlgc_vs_f=copia_dic(self.cvp.Clinea.rlgc_vs_f)
                
                self.Cgrafica.graficar()
                self.pbtn_figuras_merito.show()
                self.setWindowOpacity(1.0)
                self.cvp.setEnabled(False)
                self.lbl_todos_msmn.show()
                
            else: # Un algoritmo
                self.lbl_filtrar.hide()
                self.cbx_filtrar.hide()
                
                nombre = self.cbx_algoritmos.currentText()
                self.CgridStubs=ControladorDeCuadriculaDeStubs(self)
                self.Cbarra=ControladorDeBarra(self)
                self.Cgrafica=ControladorDeGrafica(self)
                self.Clinea=ControladorDeLineaVentanaSecundaria(self)
                self.Clinea.cargar_datos(copia_matriz(self.cvp.Clinea.datos))
                self.CgridStubs.cargar_datos(self.cvp.Buscadores[nombre].datos)
                 
                self.Clinea.Alfa=copia_lista(self.cvp.Clinea.Alfa)
                self.Clinea.Beta=copia_lista(self.cvp.Clinea.Beta)
                self.Clinea.Zc=copia_lista(self.cvp.Clinea.Zc)
                self.Clinea.rlgc_vs_f=copia_dic(self.cvp.Clinea.rlgc_vs_f)
                
                self.Cgrafica.graficar(self.cvp.Buscadores[nombre].posicion_entrada_adaptador)
                self.Cbarra.configurar(self.cvp.Buscadores[nombre].vectorD,self.cvp.Buscadores[nombre].posicion_entrada_adaptador)
                if self.cbx_tipografica.currentText()=='Respuesta en frecuencia': self.Cbarra.ocultar()
                else: self.Cbarra.mostrar()
                self.pbtn_figuras_merito.show()
                
                self.cbx_tipografica.blockSignals(True)
                tipo=self.cbx_tipografica.currentText()
                self.cbx_tipografica.clear()
                self.cbx_tipografica.addItem('Coeficiente de reflexión')
                self.cbx_tipografica.addItem('Impedancia vista')
                self.cbx_tipografica.addItem('ROEV')
                self.cbx_tipografica.addItem('Carta de Smith')
                self.cbx_tipografica.addItem('Potencia activa promedio')
                self.cbx_tipografica.addItem('Respuesta en frecuencia')
                self.cbx_tipografica.setCurrentText(tipo)
                self.cbx_tipografica.blockSignals(False)
                
                self.setWindowOpacity(1.0)
                self.cvp.setEnabled(False)
                
        elif self.bandera=='graficar':
            
            self.setWindowTitle('Gráfica')
            self.setWindowOpacity(1.0)
            self.cvp.setEnabled(False)
            
            self.cbx_tipografica.blockSignals(True)
            tipo=self.cbx_tipografica.currentText()
            self.cbx_tipografica.clear()
            self.cbx_tipografica.addItem('Coeficiente de reflexión')
            self.cbx_tipografica.addItem('Impedancia vista')
            self.cbx_tipografica.addItem('ROEV')
            self.cbx_tipografica.addItem('Carta de Smith')
            self.cbx_tipografica.addItem('Potencia activa promedio')
            self.cbx_tipografica.addItem('Respuesta en frecuencia')
            self.cbx_tipografica.setCurrentText(tipo)
            self.cbx_tipografica.blockSignals(False)
            
            self.lbl_algoritmos.hide()
            self.cbx_algoritmos.hide()
            self.pbtn_figuras_merito.hide()
            self.lbl_filtrar.hide()
            self.cbx_filtrar.hide()
            
            self.CgridStubs=ControladorDeCuadriculaDeStubs(self)
            self.Cbarra=ControladorDeBarra(self)
            self.Cgrafica=ControladorDeGrafica(self)
            
            self.Clinea=ControladorDeLineaVentanaSecundaria(self)
            self.Clinea.datos=copia_matriz(self.cvp.Clinea.datos)
            self.Clinea.cargar_datos(self.Clinea.datos)
            
            self.NoGrafica()
            self.grafica=None
            self.posicion=0
            self.posicion_entrada_adaptador=0
            self.vectorD=[]
            self.color='b'
            
            self.pbtn_figuras_merito.clicked.connect(self.ver_figuras_merito)
        
    def closeEvent(self, event): 
        if self.bandera=='buscar':
            self.Clinea.salir_sin_graficar()
            event.accept()
            
        elif self.bandera=='graficar':
            adv=adv_salir(self,'Los datos que no hayan sido\nguardados se perderán.\n¿Desea cerrar la ventana actual?')
            adv.exec()
            if self.evento_salir:
                self.Clinea.salir_sin_graficar()
                event.accept()
            else:
                event.ignore()
                   
    def salir(self): 
        self.Clinea.salir_sin_graficar()
        self.hide()
        
    def abrir_ventana_linea(self): 
        self.setEnabled(False)
        self.Clinea.show()
        
    def ver_figuras_merito(self): 
        if self.bandera=='buscar':
            self.calcular_figuras_merito()
            ventana_figuras_merito=ControladorDeVentanaComparacionBuscar(self.cvp.Buscadores)
            self.setEnabled(False)
            ventana_figuras_merito.exec()
            self.setEnabled(True)
            
        elif self.bandera=='graficar':
            self.calcular_figuras_merito()
            ventana_figuras_merito=ControladorDeVentanaComparacionGraficar(self.FigurasDeMerito,self.Fvisual)
            self.setEnabled(False)
            ventana_figuras_merito.exec()
            self.setEnabled(True)
        
    def accion_cbx_algoritmos(self): 
        if self.cbx_algoritmos.currentText()!='Todos (comparación)' and self.cbx_algoritmos.currentText()!='':
            self.cbx_tipografica.blockSignals(True)
            tipo=self.cbx_tipografica.currentText()
            self.cbx_tipografica.clear()
            self.cbx_tipografica.addItem('Coeficiente de reflexión')
            self.cbx_tipografica.addItem('Impedancia vista')
            self.cbx_tipografica.addItem('ROEV')
            self.cbx_tipografica.addItem('Carta de Smith')
            self.cbx_tipografica.addItem('Potencia activa promedio')
            self.cbx_tipografica.addItem('Respuesta en frecuencia')
            self.cbx_tipografica.setCurrentText(tipo)
            self.cbx_tipografica.blockSignals(False)
            
            self.gpbx_stubs.setEnabled(True)
            self.CgridStubs.cargar_datos(self.cvp.Buscadores[self.cbx_algoritmos.currentText()].datos,avisar=False)
            if self.cbx_tipografica.currentText()=='Respuesta en frecuencia': 
                self.Cbarra.ocultar()
            else:
                nombre=self.cbx_algoritmos.currentText()
                self.Cbarra.configurar(self.cvp.Buscadores[nombre].vectorD,self.cvp.Buscadores[nombre].posicion_entrada_adaptador)
                self.Cbarra.mostrar()
                
                
            self.graficar()
            
        elif self.cbx_algoritmos.currentText()=='Todos (comparación)':
            self.cbx_tipografica.blockSignals(True)
            tipo=self.cbx_tipografica.currentText()
            self.cbx_tipografica.clear()
            self.cbx_tipografica.addItem('Coeficiente de reflexión')
            self.cbx_tipografica.addItem('Impedancia vista')
            self.cbx_tipografica.addItem('ROEV')
            self.cbx_tipografica.addItem('Potencia activa promedio')
            self.cbx_tipografica.addItem('Respuesta en frecuencia')
            if tipo != 'Carta de Smith': self.cbx_tipografica.setCurrentText(tipo)
            elif tipo == 'Carta de Smith': self.cbx_tipografica.setCurrentText('Coeficiente de reflexión')
            self.cbx_tipografica.blockSignals(False)
            
            self.gpbx_stubs.setEnabled(False)
            self.CgridStubs.reiniciar_por_codigo()
            self.Cbarra.ocultar()
            self.graficar()
            
        elif self.cbx_algoritmos.currentText()=='':
            self.gpbx_stubs.setEnabled(False)
            self.CgridStubs.reiniciar_por_codigo()
            self.NoGrafica()
            
            
        if (self.cbx_tipografica.currentText()=='Carta de Smith')or(
                self.cbx_tipografica.currentText()=='ROEV')or(
                    self.cbx_tipografica.currentText()=='Potencia activa promedio'):
                        
                        self.cbx_presentaciongrafica.hide()
                        self.lbl_presentaciongrafica.hide()
        else: 
            self.cbx_presentaciongrafica.show()
            self.lbl_presentaciongrafica.show()
           
    def accion_cbx_tipografica(self):   
        if (self.cbx_tipografica.currentText()=='Carta de Smith')or(
                self.cbx_tipografica.currentText()=='ROEV')or(
                    self.cbx_tipografica.currentText()=='Potencia activa promedio'):
                        
                        self.cbx_presentaciongrafica.hide()
                        self.lbl_presentaciongrafica.hide()
        else: 
            self.cbx_presentaciongrafica.show()
            self.lbl_presentaciongrafica.show()
            
        if self.cbx_tipografica.currentText()=='Potencia activa promedio': 
            self.chkbx_Pmax.blockSignals(True)
            self.chkbx_Pmax.setChecked(False)
            self.chkbx_Pmax.blockSignals(False)
            self.chkbx_Pmax.show()
        else:
            self.chkbx_Pmax.blockSignals(True)
            self.chkbx_Pmax.setChecked(False)
            self.chkbx_Pmax.blockSignals(False)
            self.chkbx_Pmax.hide()
        

        self.graficar()
            
    def accion_cbx_presentaciongrafica(self): 
        self.graficar()
    
    def accion_cbx_filtrar(self): 
        algoritmo_actual=self.cbx_algoritmos.currentText()
        
        if self.cbx_filtrar.currentText()=='Mejor esfuerzo': referencia=self.cvp.no_fallidos
        elif self.cbx_filtrar.currentText()=='Modo estricto': referencia=self.cvp.algoritmos_cumplen_req
        
        self.cbx_algoritmos.blockSignals(True)
            
        self.cbx_algoritmos.clear()
        for nombre in referencia: self.cbx_algoritmos.addItem(nombre)
        
        if len(referencia)>1:
            self.setWindowTitle('Gráficas')
            self.cbx_algoritmos.addItem('Todos (comparación)')
        else:
            self.setWindowTitle('Gráfica')
            
        self.algoritmos_a_graficar=copia_lista(referencia)

        indice_actual = self.cbx_algoritmos.findText(algoritmo_actual)
        
        if indice_actual != -1:
            self.cbx_algoritmos.setCurrentIndex(indice_actual)
            self.graficar()
        else:
            if self.cbx_algoritmos.count() > 1: 
                self.cbx_algoritmos.setCurrentText('Todos (comparación)')
                
                self.graficar()
                self.gpbx_stubs.setEnabled(False)
                self.CgridStubs.reiniciar_por_codigo()
                self.lbl_no_hay_algoritmos.hide()
                
            elif self.cbx_algoritmos.count() == 1: 
                self.cbx_algoritmos.setCurrentIndex(0)
                self.graficar()
                self.lbl_no_hay_algoritmos.hide()
                
            elif self.cbx_algoritmos.count()==0: 
                self.gpbx_stubs.setEnabled(False)
                self.CgridStubs.reiniciar_por_codigo()
                self.NoGrafica()
                self.lbl_no_hay_algoritmos.show()
                
        self.cbx_algoritmos.blockSignals(False)
                
    def text_changed_fiv(self):         
        if self.linedit_fiv.text()=='': 
            self.NoGrafica()
            self.lbl_revisar_parametros.show()
    
    def text_changed_fsv(self): 
        if self.linedit_fsv.text()=='': 
            self.NoGrafica()
            self.lbl_revisar_parametros.show()
    
    def editing_finished_fiv(self): 
        if self.ignorar_senhales: return
        try: self.fiv=float(self.linedit_fiv.text())*self.multiplicador(self.cbx_fiv)
        except: self.fiv=None
        self.chequear_generar_Fvisual()
        try: self.Generador_Carga_Linea_cambio_Fvisual()
        except: return
        self.graficar()
    
    def editing_finished_fsv(self): 
        if self.ignorar_senhales: return
        try: self.fsv=float(self.linedit_fsv.text())*self.multiplicador(self.cbx_fsv)
        except: self.fsv=None
        self.chequear_generar_Fvisual()
        try: self.Generador_Carga_Linea_cambio_Fvisual()
        except: return
        self.graficar()
        
    def accion_cbx_fiv(self): 
        if self.ignorar_senhales: return
        try: self.fiv=float(self.linedit_fiv.text())*self.multiplicador(self.cbx_fiv)
        except: self.fiv=None
        self.chequear_generar_Fvisual()
        try: self.Generador_Carga_Linea_cambio_Fvisual()
        except: return
        self.graficar()
        
    def accion_cbx_fsv(self): 
        if self.ignorar_senhales: return
        try: self.fsv=float(self.linedit_fsv.text())*self.multiplicador(self.cbx_fsv)
        except: self.fsv=None
        self.chequear_generar_Fvisual()
        try: self.Generador_Carga_Linea_cambio_Fvisual()
        except: return
        self.graficar()
                
    def aplicar_frecuencia_celdas(self):
        self.M = self.spnbx_celdas.value()
        
        if self.esPar(self.spnbx_puntos_frecuencia.value()):self.spnbx_puntos_frecuencia.setValue(self.spnbx_puntos_frecuencia.value()+1)
        self.puntos=self.spnbx_puntos_frecuencia.value()
        
        self.chequear_generar_Fvisual()
        try: self.Generador_Carga_Linea_cambio_Fvisual()
        except: return
        self.graficar()
        
    def NoGrafica(self): 
        self.Cgrafica.ocultar()
        self.Cbarra.ocultar()
        self.pbtn_figuras_merito.hide()
        self.lbl_todos_msmn.hide()
        
    def graficar_linea_potencia(self):
        if self.chkbx_Pmax.isChecked():
            try: self.Cgrafica.graficar_linea_potencia()
            except: pass
        else:
            self.Cgrafica.quitar_linea_potencia()
            
        
    def graficar(self): 
        if self.bandera=='buscar':
            if self.cbx_algoritmos.currentText()=='':
                self.gpbx_stubs.setEnabled(False)
                self.CgridStubs.reiniciar_por_codigo()
                self.NoGrafica()
                
            elif self.cbx_algoritmos.currentText()=='Todos (comparación)':
                try:
                    if self.Fvisual is None: raise Exception
                    
                    Pmax=float(self.Clinea.datos[1][1])
                    DCA=int(float(self.Clinea.datos[3][0]))
                    DGA=int(float(self.Clinea.datos[3][1]))
                    
                    for nombre in self.algoritmos_a_graficar:
                        self.cvp.Buscadores[nombre].crear_grafica(self.cbx_tipografica.currentText(),
                                                                  self.cbx_presentaciongrafica.currentText(),
                                                                  self.cvp.Cgenerador.Voltaje,self.cvp.Cgenerador.Impedancia,
                                                                  self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,
                                                                  self.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                                  self.cvp.Ccarga.Z,self.Fvisual,
                                                                  self.cvp.Buscadores[nombre].posicion_entrada_adaptador)
                     
                    self.Cgrafica.borrar()
                    self.Cgrafica.graficar()
                    self.Cbarra.ocultar()
                    self.pbtn_figuras_merito.show()
                    self.lbl_todos_msmn.show()
                    self.lbl_revisar_parametros.hide()
                except:
                    #traceback.print_exc()
                    self.NoGrafica()
                    self.lbl_revisar_parametros.show()
                   
            else: # Un solo algoritmo
                
                try: 
                    if self.Fvisual is None: raise Exception
                    nombre = self.cbx_algoritmos.currentText()
                    
                    if self.cbx_tipografica.currentText() == 'Carta de Smith':
                        pass
                    else:
                        
                        Pmax=float(self.Clinea.datos[1][1])
                        DCA=int(float(self.Clinea.datos[3][0]))
                        DGA=int(float(self.Clinea.datos[3][1]))
                        
                        self.Cbarra.configurar(self.cvp.Buscadores[nombre].vectorD,self.cvp.Buscadores[nombre].posicion)
                        self.cvp.Buscadores[nombre].crear_grafica(self.cbx_tipografica.currentText(),
                                                                  self.cbx_presentaciongrafica.currentText(),
                                                                  self.cvp.Cgenerador.Voltaje,self.cvp.Cgenerador.Impedancia,
                                                                  self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,
                                                                  self.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                                  self.cvp.Ccarga.Z,self.Fvisual,
                                                                  self.cvp.Buscadores[nombre].posicion)
                    
                    self.Cgrafica.borrar()
                    self.Cgrafica.graficar(self.cvp.Buscadores[nombre].posicion)
                    self.Cgrafica.mostrar()
                    if self.cbx_tipografica.currentText()=='Respuesta en frecuencia': self.Cbarra.ocultar()
                    else: self.Cbarra.mostrar()
                    self.pbtn_figuras_merito.show()
                    self.lbl_todos_msmn.hide()
                    self.lbl_revisar_parametros.hide()
                except:
                    #traceback.print_exc()
                    self.NoGrafica()
                    self.lbl_revisar_parametros.show()
                                   
        elif self.bandera=='graficar':
            
            try: 
                if self.cbx_tipografica.currentText() == 'Carta de Smith':
                    pass
                else:
                    Pmax=float(self.Clinea.datos[1][1])
                    DCA=int(float(self.Clinea.datos[3][0]))
                    DGA=int(float(self.Clinea.datos[3][1]))
                    
                    self.crear_grafica(self.cbx_tipografica.currentText(),
                                       self.cbx_presentaciongrafica.currentText(),
                                       self.cvp.Cgenerador.Voltaje,self.cvp.Cgenerador.Impedancia,
                                       self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,
                                       self.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                       self.cvp.Ccarga.Z,self.Fvisual,
                                       self.posicion)
                    
                self.Cgrafica.borrar()
                self.Cgrafica.graficar(self.posicion)
                self.Cgrafica.mostrar()
                if self.cbx_tipografica.currentText()=='Respuesta en frecuencia': self.Cbarra.ocultar()
                else: self.Cbarra.mostrar()
                self.pbtn_figuras_merito.show()
                self.lbl_todos_msmn.hide()
                self.lbl_revisar_parametros.hide()
            except: 
                self.NoGrafica()
                self.lbl_revisar_parametros.show()
                
                

    def crear_grafica(self,tipo,presentacion,VoltajeGenerador,ImpedanciaGenerador,Alfa,Beta,Zc,rlgc_vs_f,Pmax,DCA,DGA,ZL,F,d=None): 
        # asume que Zins ya está calculado
        
        if d is None: self.posicion=self.posicion_entrada_adaptador
        else: self.posicion=d
        self.grafica=None
        
        M=self.M
        
        if tipo=='Potencia activa promedio': 
            self.grafica=funcion_vista_d(tipo,presentacion,VoltajeGenerador,ImpedanciaGenerador,
                                         Alfa,Beta,Zc,rlgc_vs_f,Pmax,
                                         self.CgridStubs.datos,self.CgridStubs.Zins,DCA,DGA,
                                         ZL,F,self.vectorD,self.posicion,M)
            
            
        elif tipo=='Respuesta en frecuencia':
            self.grafica=funcion_vista_d(tipo,presentacion,VoltajeGenerador,ImpedanciaGenerador,
                                         Alfa,Beta,Zc,rlgc_vs_f,Pmax,
                                         self.CgridStubs.datos,self.CgridStubs.Zins,DCA,DGA,
                                         ZL,F,self.vectorD,self.posicion,M)
        
        else:
            self.grafica=funcion_vista_d(tipo,presentacion,VoltajeGenerador,ImpedanciaGenerador,
                                         Alfa,Beta,Zc,rlgc_vs_f,Pmax,
                                         self.CgridStubs.datos,self.CgridStubs.Zins,DCA,DGA,
                                         ZL,F,self.vectorD,self.posicion,M)
        
        
    ### Lógica de Cómputo
            
    def esPar(self,numero):
        n=numero/2
        if n-int(n) == 0 : return True
        else: return False
        
    def multiplicador(self,cbx): 
        if cbx.currentText()=='GHz': mult=1e3
        elif cbx.currentText()=='MHz': mult=1
        elif cbx.currentText()=='kHz': mult=1e-3
        return mult
        
    def chequear_generar_Fvisual(self): 
        try:
            if (self.fiv is None)or(self.fsv is None):
                self.Fvisual=None
                self.lbl_revisar_parametros.show()
                
            elif (self.fiv <= 0)or(self.fsv <= 0):
                self.Fvisual=None
                self.lbl_revisar_parametros.show()
                
            elif self.fsv <= self.fiv:
                self.Fvisual=None
                self.lbl_revisar_parametros.show()
                
            else:
                fmin,fmax=self.rango_correcto_frecuencia()
                if self.fiv_fsv_contenido_en_rango_de_frecuencia(fmin,fmax): 
                    self.calcular_vector_F_visual(self.fiv,self.fsv)
                    self.lbl_revisar_parametros.hide()
                else: 
                    self.Fvisual=None
                    self.lbl_revisar_parametros.show()
        except:
            self.Fvisual=None
            self.lbl_revisar_parametros.show()
            
    def Generador_Carga_Linea_cambio_Fvisual(self): 
        if self.bandera=='buscar':
            if self.cbx_algoritmos.currentText()=='':
                return
            
            elif self.cbx_algoritmos.currentText()=='Todos (comparación)':
                try:
                    self.cvp.Cgenerador.Impedancia=self.cvp.Cgenerador.calcularImpedancia(self.Fvisual)
                    self.cvp.Cgenerador.Voltaje=self.cvp.Cgenerador.calcularVoltaje(self.cvp.Cgenerador.Impedancia,self.Fvisual)
                    self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc = self.Clinea.calcularABZ(self.Fvisual)
                    self.cvp.Ccarga.Z=self.cvp.Ccarga.calcularZ(self.Fvisual)
                    
                    for nombre in self.algoritmos_a_graficar:
                        self.cvp.Buscadores[nombre].Zins=self.cvp.Buscadores[nombre].calcularZins(self.Fvisual,
                                                                                                  self.Clinea.Alfa,
                                                                                                  self.Clinea.Beta,
                                                                                                  self.Clinea.Zc)
                except:
                    #traceback.print_exc()
                    self.NoGrafica()
                    raise Exception
                    
            else:# Un solo algoritmo
                try:
                    nombre=self.cbx_algoritmos.currentText()
                    
                    self.cvp.Cgenerador.Impedancia=self.cvp.Cgenerador.calcularImpedancia(self.Fvisual)
                    self.cvp.Cgenerador.Voltaje=self.cvp.Cgenerador.calcularVoltaje(self.cvp.Cgenerador.Impedancia,self.Fvisual)
                    self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc = self.Clinea.calcularABZ(self.Fvisual)
                    self.cvp.Ccarga.Z=self.cvp.Ccarga.calcularZ(self.Fvisual)
                    
                    self.cvp.Buscadores[nombre].Zins=self.cvp.Buscadores[nombre].calcularZins(self.Fvisual,
                                                                                              self.Clinea.Alfa,
                                                                                              self.Clinea.Beta,
                                                                                              self.Clinea.Zc)
                except:
                    self.NoGrafica()
                    raise Exception
                
        elif self.bandera=='graficar':
            
            try:
                self.cvp.Cgenerador.Impedancia=self.cvp.Cgenerador.calcularImpedancia(self.Fvisual)
                self.cvp.Cgenerador.Voltaje=self.cvp.Cgenerador.calcularVoltaje(self.cvp.Cgenerador.Impedancia,self.Fvisual)
                self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc = self.Clinea.calcularABZ(self.Fvisual)
                self.cvp.Ccarga.Z=self.cvp.Ccarga.calcularZ(self.Fvisual)
                
                self.CgridStubs.Zins=self.CgridStubs.calcularZins(self.Fvisual,self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc)
            except:
                self.NoGrafica()
                raise Exception
                
    
    
    def calcular_figuras_merito(self):
                    
        if self.bandera=='buscar':
            for nombre in self.algoritmos_a_graficar:
                Gamma_adp=mod_Gamma(self.cvp.Cgenerador.Impedancia,self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,
                                    self.cvp.Buscadores[nombre].Zins,self.cvp.Buscadores[nombre].vectorD,
                                    self.cvp.Ccarga.Z,self.Fvisual,self.cvp.Buscadores[nombre].posicion_entrada_adaptador)

                Zdin=complex_Z(self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,
                               self.cvp.Buscadores[nombre].Zins,
                               self.cvp.Buscadores[nombre].vectorD,
                               self.cvp.Ccarga.Z,self.Fvisual,self.cvp.Buscadores[nombre].vectorD[-1].posicion)
                
                H_rad=fase_H_rad(self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,
                                 self.Clinea.rlgc_vs_f,self.cvp.Buscadores[nombre].Zins,
                                 self.cvp.Ccarga.Z,self.Fvisual,self.cvp.Buscadores[nombre].vectorD,self.M)
                
                self.cvp.Buscadores[nombre].calcularFigurasDeMerito(self.cvp.Cgenerador.Impedancia,Gamma_adp,Zdin,H_rad,self.Fvisual)
            
        elif self.bandera=='graficar':
            Gamma_adp=mod_Gamma(self.cvp.Cgenerador.Impedancia,self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,
                                self.CgridStubs.Zins,self.vectorD,
                                self.cvp.Ccarga.Z,self.Fvisual,self.posicion_entrada_adaptador)

            Zdin=complex_Z(self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,
                           self.CgridStubs.Zins,
                           self.vectorD,
                           self.cvp.Ccarga.Z,self.Fvisual,self.vectorD[-1].posicion)
            
            H_rad=fase_H_rad(self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,
                             self.Clinea.rlgc_vs_f,self.CgridStubs.Zins,
                             self.cvp.Ccarga.Z,self.Fvisual,self.vectorD,self.M)
            
            longitud=0
            N=int(float(self.CgridStubs.datos[0][2]))
            for n in range(1,N+1): longitud+=int(float(self.CgridStubs.datos[n][0]))
            
            self.FigurasDeMerito['stubs']=int(self.CgridStubs.datos[0][2])
            self.FigurasDeMerito['longitud']=longitud
            
            self.FigurasDeMerito['perdida_Zo_fo']=perdida_Zo_fo(self.cvp.Cgenerador.Impedancia,Zdin,self.Fvisual)
            self.FigurasDeMerito['max_perdida_Zo'],self.FigurasDeMerito['f_max_perdida_Zo']=max_perdida_Zo(self.cvp.Cgenerador.Impedancia,Zdin,self.Fvisual)
            self.FigurasDeMerito['perdida_conj_fo']=perdida_conj_fo(self.cvp.Cgenerador.Impedancia,Zdin,self.Fvisual)
            self.FigurasDeMerito['max_perdida_conj'],self.FigurasDeMerito['f_max_perdida_conj']=max_perdida_conj(self.cvp.Cgenerador.Impedancia,Zdin,self.Fvisual)
            self.FigurasDeMerito['distorsion_fase']=distorsion_fase(H_rad,self.Fvisual)
            self.FigurasDeMerito['rizado']=rizado(Gamma_adp,self.Fvisual)
            self.FigurasDeMerito['gamma_fo']=gamma_fo(Gamma_adp,self.Fvisual)
            self.FigurasDeMerito['max_gamma'],self.FigurasDeMerito['f_max_gamma']=max_gamma(Gamma_adp,self.Fvisual)
            self.FigurasDeMerito['adaptacion_gamma']=adaptacion_gamma(Gamma_adp,self.Fvisual)
            

    def interseccion(self,f1min,f1max,f2min,f2max): 
        fmin=max(f1min,f2min)
        fmax=min(f1max,f2max)
        if fmin < fmax : return fmin,fmax
        else: return None,None
            
    def rango_correcto_frecuencia(self): 
        fmin1,fmax1=self.interseccion(self.cvp.Ccarga.datos[-1][0],self.cvp.Ccarga.datos[-1][1],
                                      self.Clinea.datos[-1][0],self.Clinea.datos[-1][1])
        
        if (fmin1 is not None) and (fmax1 is not None):
            fmin2,fmax2=self.interseccion(fmin1,fmax1,
                                          self.cvp.Cgenerador.datos_impedancia[-1][0],self.cvp.Cgenerador.datos_impedancia[-1][1])
        else: 
            return None,None
            
        if (fmin2 is not None) and (fmax2 is not None): return fmin2,fmax2
        else: return None,None
        
    def fiv_fsv_contenido_en_rango_de_frecuencia(self,fmin,fmax): 
        if (fmin is None) or (fmax is None): return False
        
        if (self.fiv >= fmin) and (self.fsv <= fmax): return True
        else: return False
        
        
    def calcular_vector_F_visual(self,fmin,fmax): 
        if (fmin is not None) and (fmax is not None): self.Fvisual=linspace(fmin,fmax,self.puntos)
        else: self.Fvisual=[]

            
class HiloLabelAnuncio(threading.Thread):
    
    def __init__(self,ventana_principal):
        threading.Thread.__init__(self)
        self.cvpp=ventana_principal
                
    def start(self,mensaje=''):
        self.cvpp.lbl_anuncio.setText(mensaje)
        if mensaje=='Los algoritmos de búsqueda han finalizado.':
            self.cvpp.lbl_anuncio.setStyleSheet("""
                                                color: rgb(72,250,54);
                                                font: 75 10pt "MS Shell Dlg 2";                                    
                                                """)
        else:
            self.cvpp.lbl_anuncio.setStyleSheet("""
                                                color: rgb(238,238,238);
                                                font: 75 10pt "MS Shell Dlg 2";                                    
                                                """)
            
        self.cvpp.lbl_anuncio.show()
            

class HiloBuscador(QThread):
    InicioBusqueda=pyqtSignal()
    FinalBusqueda=pyqtSignal()

    def __init__(self,buscador):
        QThread.__init__(self)
        self.buscador=buscador
        self.mem=None
        self.tid=self.currentThreadId().__int__()
        self.Inicio=False
        
        #Conexiones
        self.buscador.BuscadorIniciado.connect(self.buscador_iniciado)
        self.buscador.BuscadorFinalizado.connect(self.buscador_finalizado)
        
    def buscador_iniciado(self):
        self.InicioBusqueda.emit()
        
    def buscador_finalizado(self):
        self.FinalBusqueda.emit()

    def run(self):
        if self.Inicio: return
        else: pass
    
        if not self.buscador.is_alive(): self.buscador.start()
        else: return
    
        self.Inicio=True
        
        try:
            while self.buscador.is_alive():pass
        except:
            pass
        
        return
        
    def salir(self):
        self.finished.emit()
                

class MainWindow(QtWidgets.QMainWindow, Ui_ventanaPrincipal):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint)
        
        self.setWindowTitle('Eureka MSMN')
        
        resolucion=ctypes.windll.user32
        ancho=resolucion.GetSystemMetrics(0)
        alto=resolucion.GetSystemMetrics(1)
        
        if ancho < 1024 :
            self.setMinimumWidth(ancho-18)
            self.setMaximumWidth(ancho-18)
            self.scllarea_master.setMinimumWidth(ancho-18)
            self.scllarea_master.setMaximumWidth(ancho-18)
            
        if alto < 768 :
            self.setMinimumHeight(alto-78)
            self.setMaximumHeight(alto-78)
            self.scllarea_master.setMinimumHeight(alto-98)
            self.scllarea_master.setMaximumHeight(alto-98) 
        
        self.move(0,0)
        
        
        
        #Variables
        global puntosdefrecuencia
        self.puntos= puntosdefrecuencia
        
        global SS_lbl,SS_linedit,SS_cbx,SS_cbx_und,SS_pbtn,SS_Vbar
        self.SS_lbl=SS_lbl
        self.SS_linedit=SS_linedit
        self.SS_cbx=SS_cbx
        self.SS_cbx_und=SS_cbx_und
        self.SS_pbtn=SS_pbtn
        self.SS_Vbar=SS_Vbar
        
        self.pbtn_cancelar.hide()
        self.pbtn_metadata.hide()
        self.pbtn_resultados_msmn.hide()
        self.lbl_anuncio.hide()
        
        self.Cobjetivo = ControladorDeObjetivo(self)
        self.Ccarga = ControladorDeCarga(self)
        self.Clinea = ControladorDeLinea(self)
        self.CreqStubs = ControladorDeRequerimientosDeStubs(self)
        self.Cgenerador = ControladorDeGenerador(self)
        
        self.anuncio=HiloLabelAnuncio(self)
        self.anuncio.start('')
        self.hilos_finalizados=0
        self.busquedas_iniciadas=0
        self.busquedas_finalizadas=0
        self.datos=[]
        self.respaldo_datos=[]
        self.F=[] # vector que almacena los valores de frecuencia, en MHz
        self.Buscadores=dict()
        self.ventanaSecundariaResultados=None
        self.ventanaSecundariaGraficar=None
        self.Hilos=[]
        self.cancelado=False
        self.fmin_permitido=None
        self.fmax_permitido=None
        self.algoritmos_cumplen_req=[]
        self.no_fallidos=[]
        
        global PIRAmin
        self.PIRAmin=PIRAmin
        
        self.evento_salir=None
        
        #Conexiones
        self.pbtn_buscar.clicked.connect(self.buscar)
        self.pbtn_cancelar.clicked.connect(self.cancelar)
        self.pbtn_graficar.clicked.connect(self.graficar)
        self.pbtn_metadata.clicked.connect(self.ver_metadata)
        self.pbtn_resultados_msmn.clicked.connect(self.ver_resultados_msmn)
        
        self.actionCargar.triggered.connect(self.cargar)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionReiniciar.triggered.connect(self.reiniciar)
        
        self.pbtn_configurar_carga.clicked.connect(self.abrir_ventana_carga)
        self.pbtn_configurar_linea.clicked.connect(self.abrir_ventana_linea)
        self.pbtn_configurar_reqStubs.clicked.connect(self.abrir_ventana_reqStubs)
        self.pbtn_configurar_generador.clicked.connect(self.abrir_ventana_generador)
        
    ### Lógica de Interfaz Gráfica
        
    def closeEvent(self, event): 
        adv=adv_salir(self,'Los datos que no hayan sido\nguardados se perderán.\n¿Desea cerrar la aplicación?')
        adv.exec()
        if self.evento_salir: 
            self.cerrar_ventanas()
            
            try: self.ventanaSecundariaGraficar.salir()
            except: pass
        
            try: self.ventanaSecundariaResultados.salir()
            except: pass
            
            try: self.detener_eliminar_hilos_busqueda()
            except: pass
                    
            event.accept()
        else: 
            event.ignore()  
            
    def cerrar_ventanas(self):
        self.Cgenerador.salir()
        self.Clinea.salir()
        self.CreqStubs.salir()
        self.Ccarga.salir()
            
    def bloquear(self):
        self.Ccarga.bloquear()
        self.CreqStubs.bloquear()
        self.Clinea.bloquear()
        self.Cgenerador.bloquear()
        self.Cobjetivo.bloquear()
        self.menuBar.setEnabled(False)
        
    def desbloquear(self):
        self.Ccarga.desbloquear()
        self.CreqStubs.desbloquear()
        self.Clinea.desbloquear()
        self.Cgenerador.desbloquear()
        self.Cobjetivo.desbloquear()
        self.menuBar.setEnabled(True)
        
    def cargar(self): 
        try:
            carpeta='./Datos/Proyectos'
            ruta = QFileDialog.getOpenFileName(self, 'Cargar archivo',carpeta,"*.search")[0]
            if os.path.exists(ruta):
                datos=[]
                with open(ruta) as archivo:
                    lector = csv.reader(archivo, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    for fila in lector: datos.append(fila) 
                                
                self.datos=datos  

                # .obj (3)
                #
                # .source (Nmed+2)
                #
                # .modelimp (1+n:3,4,5) / .imp (n+2)
                #
                # .line (5)
                #
                # .reqstubs (1)
                #
                # .modelimp (1+n:3,4,5,7) / .imp (n+2)
            
                obj_i=0
                obj_f=2
                self.Cobjetivo.cargar_datos(self.datos[obj_i : obj_f+1])
                
                fuente_i=obj_f+2
                fuente_f=fuente_i+int(self.datos[fuente_i][1])+1
                self.Cgenerador.cargar_datos_fuente(self.datos[fuente_i : fuente_f+1])
                
                imp_gen_i=fuente_f+2
                if self.datos[imp_gen_i][0]=='Modelo': imp_gen_f=imp_gen_i+int(self.datos[imp_gen_i][1])
                if self.datos[imp_gen_i][0]=='Archivo': imp_gen_f=imp_gen_i+int(self.datos[imp_gen_i][1])+1
                self.Cgenerador.cargar_datos_impedancia(self.datos[imp_gen_i : imp_gen_f+1])
                
                linea_i=imp_gen_f+2
                linea_f=linea_i+4
                self.Clinea.cargar_datos(self.datos[linea_i : linea_f+1])
                
                stubs_i=linea_f+2
                stubs_f=stubs_i
                self.CreqStubs.cargar_datos(self.datos[stubs_i : stubs_f+1])
                
                carga_i=stubs_f+2
                if self.datos[carga_i][0]=='Modelo': carga_f=carga_i+int(self.datos[carga_i][1])
                if self.datos[carga_i][0]=='Archivo': carga_f=carga_i+int(self.datos[carga_i][1])+1
                self.Ccarga.cargar_datos(self.datos[carga_i : carga_f+1])
                               
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos del proyecto.')
            ad.exec_()
            
            try: self.Cobjetivo.reiniciar()
            except: pass
        
            try: self.Cgenerador.reiniciar()
            except: pass
        
            try: self.Clinea.reiniciar()
            except: pass
        
            try: self.CreqStubs.reiniciar()
            except: pass
        
            try: self.Ccarga.reiniciar()
            except: pass
        
            self.datos=[]
        
    def guardar(self): 
        try:
            carpeta='./Datos/Proyectos'
            ruta = QFileDialog.getSaveFileName(self,'Guardar archivo',carpeta,'*.search')[0]
            if ruta!='':
                if ruta[-7:] != '.search': ruta=ruta+'.search'
                
                datos=[]
                for fila in self.Cobjetivo.datos:datos.append(fila)
                datos.append([])
                for fila in self.Cgenerador.datos_fuente:datos.append(fila)
                datos.append([])
                for fila in self.Cgenerador.datos_impedancia:datos.append(fila)
                datos.append([])
                for fila in self.Clinea.datos:datos.append(fila)
                datos.append([])
                for fila in self.CreqStubs.datos:datos.append(fila)
                datos.append([])
                for fila in self.Ccarga.datos:datos.append(fila)
                
                with open(ruta,'w',newline='') as archivo:
                    escritor = csv.writer(archivo)
                    for fila in datos:
                        escritor.writerow(fila)
                        
        except:
            ad=adv('Formato incompatible.\nNo se pudo guardar los datos del proyecto.')
            ad.exec_()
                    
    def reiniciar(self): 
        self.Cobjetivo.reiniciar()
        self.Cgenerador.reiniciar()    
        self.Clinea.reiniciar()    
        self.CreqStubs.reiniciar()    
        self.Ccarga.reiniciar()
        
        self.pbtn_buscar.show()
        self.pbtn_graficar.show()
        
        self.datos=[]
        
            
    def abrir_ventana_generador(self): 
        self.pbtn_configurar_generador.setEnabled(False)
        self.Cgenerador.show()
        
    def abrir_ventana_linea(self): 
        self.pbtn_configurar_linea.setEnabled(False)
        self.Clinea.show()
        
    def abrir_ventana_reqStubs(self): 
        self.pbtn_configurar_reqStubs.setEnabled(False)
        self.CreqStubs.show()
              
    def abrir_ventana_carga(self): 
        self.pbtn_configurar_carga.setEnabled(False)
        self.Ccarga.show()
                        
    def ver_metadata(self): 
        vmd=ControladorDeVentanaMetadata(self.Buscadores)
        vmd.exec()
                    
    def ver_resultados_msmn(self):
        self.cerrar_ventanas()
        self.setEnabled(False)
        
        self.datosAventanas(copia_matriz(self.respaldo_datos))
        
        if self.ventanaSecundariaResultados is None:
            fallidos=0
            for nombre in self.Buscadores: 
                if self.Buscadores[nombre].Fallido: 
                    fallidos+=1
            
            if fallidos < len(self.Buscadores): 
                self.ventanaSecundariaResultados=VentanaSecundaria(self,'buscar')
                self.ventanaSecundariaResultados.exec_()
            else:
                if len(self.Cobjetivo.datos[1])==1:
                    ad=adv('El algoritmo tuvo una falla en la ejecución\no no fue capaz de hallar una solución.\nNo hay resultados para mostrar.')
                    ad.exec_()
                elif len(self.Cobjetivo.datos[1])>1:
                    ad=adv('Los algoritmos tuvieron fallas en la ejecución\no no fueron capaces de hallar soluciones.\nNo hay resultados para mostrar.')
                    ad.exec_()
        else:
            self.ventanaSecundariaResultados.exec_()
            
        self.setEnabled(True)
        return

    def buscar(self): 
        
        self.cancelado=False
        self.bloquear()
        self.pbtn_buscar.hide()
        self.pbtn_graficar.hide()
        self.pbtn_resultados_msmn.hide()
        self.pbtn_metadata.hide()
        
        self.hilos_finalizados=0
        self.busquedas_iniciadas=0
        self.busquedas_finalizadas=0
        
        self.ventanaSecundariaResultados=None
        
        try:
            self.detener_eliminar_hilos_busqueda()
            self.eliminar_labels_algoritmos()
        except:
            pass
        
        self.anuncio.start('') #borra el anuncio
                
        self.Hilos=[]
        self.Buscadores=dict()
        self.Labels=dict()
        
               
        if self.Cgenerador.datos_correcto_fuente():
            self.Cgenerador.determinar_fmin_fmax_datos_fuente()
            self.Cgenerador.datos_fuente=self.Cgenerador.formatear_datos_fuente(self.Cgenerador.datos_fuente)
        else:
            self.pbtn_buscar.show()
            self.pbtn_graficar.show()
            self.desbloquear()
            return
        
        if self.Cgenerador.datos_correcto_impedancia():
            self.Cgenerador.determinar_fmin_fmax_datos_impedancia()
            self.Cgenerador.datos_impedancia=self.Cgenerador.formatear_datos_impedancia(self.Cgenerador.datos_impedancia)
        else:
            self.pbtn_buscar.show()
            self.pbtn_graficar.show()
            self.desbloquear()
            return

        if self.Clinea.datos_correcto():
            self.Clinea.determinar_fmin_fmax_datos()
            self.Clinea.datos=self.Clinea.formatear_datos(self.Clinea.datos)
        else:
            self.pbtn_buscar.show()
            self.pbtn_graficar.show()
            self.desbloquear()
            return
                
        if self.CreqStubs.datos_correcto():
            self.CreqStubs.datos=self.CreqStubs.formatear_datos(self.CreqStubs.datos)
        else:
            self.pbtn_buscar.show()
            self.pbtn_graficar.show()
            self.desbloquear()
            return
        
        if self.Ccarga.datos_correcto():
            self.Ccarga.determinar_fmin_fmax_datos()
            self.Ccarga.datos=self.Ccarga.formatear_datos(self.Ccarga.datos)
        else:
            self.pbtn_buscar.show()
            self.pbtn_graficar.show()
            self.desbloquear()
            return
        
        if self.Cobjetivo.datos_correcto():
            self.Cobjetivo.determinar_fmin_fmax_datos()
            self.Cobjetivo.datos=self.Cobjetivo.formatear_datos(self.Cobjetivo.datos)
        else:
            self.pbtn_buscar.show()
            self.pbtn_graficar.show()
            self.desbloquear()
            return
        
        self.crear_respaldo_datos()
        
        self.fmin_permitido,self.fmax_permitido = self.rango_correcto_frecuencia()
        
        if (self.fmin_permitido is not None) and (self.fmax_permitido is not None):
            if self.bw_objetivo_contenido_en_rango_de_frecuencia(self.fmin_permitido,self.fmax_permitido):
                self.calcular_vector_F(self.Cobjetivo.datos[-1][0],self.Cobjetivo.datos[-1][1])
                
            else:
                ad=adv('No se tiene información suficiente del generador,\nla línea o la carga para el rango de frecuencia\nde adaptación requerido. Éste debe estar entre\n['+str(round(self.fmin_permitido,3))+' - '+str(round(self.fmax_permitido,3))+'] MHz. Por favor verifique.')
                ad.exec_()
                self.anuncio.start('')
                self.pbtn_buscar.show()
                self.pbtn_graficar.show()
                self.desbloquear()
                return
        else:
            ad=adv('Los rangos de frecuencia no coinciden.\nVerifique la impedancia del generador,\nla línea de transmisión y la impedancia de carga.')
            ad.exec_()
            self.anuncio.start('')
            self.pbtn_buscar.show()
            self.pbtn_graficar.show()
            self.desbloquear()
            return
                    
        self.Clinea.Alfa_original,self.Clinea.Beta_original,self.Clinea.Zc_original = self.Clinea.calcularABZ(self.F)
        self.Clinea.Alfa=copia_lista(self.Clinea.Alfa_original)
        self.Clinea.Beta=copia_lista(self.Clinea.Beta_original)
        self.Clinea.Zc=copia_lista(self.Clinea.Zc_original)
        self.Clinea.rlgc_vs_f_original=copia_dic(self.Clinea.rlgc_vs_f)
        
        self.Ccarga.Z_original=self.Ccarga.calcularZ(self.F)
        self.Ccarga.Z=copia_lista(self.Ccarga.Z_original)
        self.Ccarga.Zprima=self.Ccarga.calcularZprima(self.Ccarga.Z,self.Clinea.datos[3][0],
                                                      self.Clinea.Alfa,self.Clinea.Beta,self.Clinea.Zc,self.F)
        
        self.Cgenerador.Impedancia_original=self.Cgenerador.calcularImpedancia(self.F)
        self.Cgenerador.Impedancia=copia_lista(self.Cgenerador.Impedancia_original)
        
        self.Cgenerador.Voltaje_original=self.Cgenerador.calcularVoltaje(self.Cgenerador.Impedancia_original,self.F)
        self.Cgenerador.Voltaje=copia_lista(self.Cgenerador.Voltaje_original)
        
        self.Cobjetivo.calcular_funcion_objetivo(self.F)
        
        self.Cobjetivo.eliminar_algoritmos_duplicados()
        
        for nombre in self.Cobjetivo.datos[1]:
            self.Buscadores[nombre]=Buscador(nombre,self)
            self.Labels[nombre]=QLabel(nombre+' inició. Espere...')
            self.Labels[nombre].setStyleSheet("""
                                                color:rgb(238, 238, 238);
                                                font: 75 8pt "MS Shell Dlg 2";
                                                """)
            self.Labels[nombre].setFixedHeight(30)
        
        for nombre in self.Cobjetivo.datos[1]:
            self.Hilos.append(HiloBuscador(self.Buscadores[nombre]))
        
        for hilo in self.Hilos:
            #Conexiones
            hilo.InicioBusqueda.connect(partial(self.aviso_inicio_busqueda, hilo.buscador))
            hilo.FinalBusqueda.connect(partial(self.aviso_final_busqueda, hilo.buscador))
            hilo.finished.connect(self.final_hilo)
            hilo.start()
            
        self.anuncio.start('Configurando estructuras de datos.\nPor favor espere...')
        

    def aviso_inicio_busqueda(self,buscador):
        self.layout_avisos.addWidget(self.Labels[buscador.nombre])
        
        self.busquedas_iniciadas+=1
        if self.busquedas_iniciadas==1: self.anuncio.start('Iniciando algoritmos...')
        if self.busquedas_iniciadas==len(self.Cobjetivo.datos[1]): 
            self.anuncio.start('Algoritmos de búsqueda iniciados.')
            self.pbtn_cancelar.show()

    def aviso_final_busqueda(self,buscador):
        if buscador.Fallido: palabra=buscador.nombre+' falló en la búsqueda.'
        else: palabra=buscador.nombre+' finalizó.'
        self.Labels[buscador.nombre].setText(palabra+'\n   Transcurrido: '+str(round(buscador.FigurasDeMerito['tiempo'],2))+' s.')
        self.busquedas_finalizadas+=1
        if self.busquedas_finalizadas==len(self.Cobjetivo.datos[1]):
            self.anuncio.start('Los algoritmos de búsqueda han finalizado.')
            
    def final_hilo(self):
        self.hilos_finalizados+=1
        
        if self.hilos_finalizados==len(self.Cobjetivo.datos[1]): pass
        else: return
        
        if not self.cancelado:
            self.calculos_previos_de_algoritmos()   
            
            self.pbtn_buscar.show()
            self.pbtn_cancelar.hide()
            self.pbtn_graficar.show()
            self.pbtn_metadata.show()
            self.pbtn_resultados_msmn.show()
            self.desbloquear()
        else:
            self.anuncio.start('')
            self.pbtn_buscar.show()
            self.pbtn_graficar.show()
            self.pbtn_resultados_msmn.hide()
            self.pbtn_metadata.hide()
            self.desbloquear()
            
        
                
    def cancelar(self):
        self.cancelado=True
        self.pbtn_cancelar.hide()

        self.detener_eliminar_hilos_busqueda()
        self.eliminar_labels_algoritmos()
        self.desbloquear()
        
        
    def detener_eliminar_hilos_busqueda(self):
        if len(self.Hilos) ==0: return
        
        for hilo in self.Hilos:
            try:
                hilo.buscador.detener()
                del(hilo.buscador)
                while hilo.isRunning():pass
                hilo.deleteLater()
            except:
                pass
            
               
    def eliminar_labels_algoritmos(self):
        try:
            for palabra in self.Labels: 
                self.Labels[palabra].deleteLater()
        except:
            pass
        
    def graficar(self):
        self.cerrar_ventanas()
        self.setEnabled(False)
        
        if self.Cgenerador.datos_correcto_fuente():
            self.Cgenerador.determinar_fmin_fmax_datos_fuente()
            self.Cgenerador.datos_fuente=self.Cgenerador.formatear_datos_fuente(self.Cgenerador.datos_fuente)
        else:
            self.setEnabled(True)
            return
        
        if self.Cgenerador.datos_correcto_impedancia():
            self.Cgenerador.determinar_fmin_fmax_datos_impedancia()
            self.Cgenerador.datos_impedancia=self.Cgenerador.formatear_datos_impedancia(self.Cgenerador.datos_impedancia)
        else:
            self.setEnabled(True)
            return
                                
        if self.Ccarga.datos_correcto():
            self.Ccarga.determinar_fmin_fmax_datos()
            self.Ccarga.datos=self.Ccarga.formatear_datos(self.Ccarga.datos)
        else:
            self.setEnabled(True)
            return
        
        self.fmin_permitido,self.fmax_permitido = self.rango_correcto_frecuencia()
        if (self.fmin_permitido is not None) and (self.fmax_permitido is not None):
            pass
        else:
            ad=adv('Los rangos de frecuencia no coinciden.\nVerifique la impedancia del generador\n y la impedancia de carga.')
            ad.exec_()
            self.setEnabled(True)
            return

        self.ventanaSecundariaGraficar = VentanaSecundaria(self,'graficar')
        self.ventanaSecundariaGraficar.exec_()
            
        self.setEnabled(True)
        
    def datosAventanas(self,datos):
        # .obj (3)
        #
        # .source (Nmed+2)
        #
        # .modelimp (1+n:3,4,5) / .imp (n+2)
        #
        # .line (5)
        #
        # .reqstubs (1)
        #
        # .modelimp (1+n:3,4,5,7) / .imp (n+2)
    
        obj_i=0
        obj_f=2
        self.Cobjetivo.cargar_datos(datos[obj_i : obj_f+1])
        
        fuente_i=obj_f+2
        fuente_f=fuente_i+int(datos[fuente_i][1])+1
        self.Cgenerador.cargar_datos_fuente(datos[fuente_i : fuente_f+1])
        
        imp_gen_i=fuente_f+2
        if datos[imp_gen_i][0]=='Modelo': imp_gen_f=imp_gen_i+int(datos[imp_gen_i][1])
        if datos[imp_gen_i][0]=='Archivo': imp_gen_f=imp_gen_i+int(datos[imp_gen_i][1])+1
        self.Cgenerador.cargar_datos_impedancia(datos[imp_gen_i : imp_gen_f+1])
        
        linea_i=imp_gen_f+2
        linea_f=linea_i+4
        self.Clinea.cargar_datos(datos[linea_i : linea_f+1])
        
        stubs_i=linea_f+2
        stubs_f=stubs_i
        self.CreqStubs.cargar_datos(datos[stubs_i : stubs_f+1])
        
        carga_i=stubs_f+2
        if datos[carga_i][0]=='Modelo': carga_f=carga_i+int(datos[carga_i][1])
        if datos[carga_i][0]=='Archivo': carga_f=carga_i+int(datos[carga_i][1])+1
        self.Ccarga.cargar_datos(datos[carga_i : carga_f+1])
        
        
    ### Lógica de Cómputo
        
    def crear_respaldo_datos(self):
        self.respaldo_datos=[]
        for fila in self.Cobjetivo.datos:self.respaldo_datos.append(copia_lista(fila))
        self.respaldo_datos.append([])
        for fila in self.Cgenerador.datos_fuente:self.respaldo_datos.append(copia_lista(fila))
        self.respaldo_datos.append([])
        for fila in self.Cgenerador.datos_impedancia:self.respaldo_datos.append(copia_lista(fila))
        self.respaldo_datos.append([])
        for fila in self.Clinea.datos:self.respaldo_datos.append(copia_lista(fila))
        self.respaldo_datos.append([])
        for fila in self.CreqStubs.datos:self.respaldo_datos.append(copia_lista(fila))
        self.respaldo_datos.append([])
        for fila in self.Ccarga.datos:self.respaldo_datos.append(copia_lista(fila))
               
    def interseccion(self,f1min,f1max,f2min,f2max):
        fmin=max(f1min,f2min)
        fmax=min(f1max,f2max)
        if fmin < fmax : return fmin,fmax
        else: return None,None
            
    def rango_correcto_frecuencia(self): 
        fmin1,fmax1=self.interseccion(self.Ccarga.datos[-1][0],self.Ccarga.datos[-1][1],
                                      self.Clinea.datos[-1][0],self.Clinea.datos[-1][1])
        
        if (fmin1 is not None) and (fmax1 is not None):
            fmin2,fmax2=self.interseccion(fmin1,fmax1,
                                          self.Cgenerador.datos_impedancia[-1][0],self.Cgenerador.datos_impedancia[-1][1])
        else: 
            return None,None
            
        if (fmin2 is not None) and (fmax2 is not None): return fmin2,fmax2
        else: return None,None
        
    def bw_objetivo_contenido_en_rango_de_frecuencia(self,fmin,fmax): 
        if (self.Cobjetivo.datos[-1][0] >= fmin) and (self.Cobjetivo.datos[-1][1] <= fmax): return True
        else: return False
        
        
    def calcular_vector_F(self,fmin,fmax): 
        if (fmin is not None) and (fmax is not None): self.F=linspace(fmin,fmax,self.puntos)
        else: self.F=[]
            

                        
    def calculos_previos_de_algoritmos(self):
        self.no_fallidos=[]
        for nombre in self.Cobjetivo.datos[1]:
            if not self.Buscadores[nombre].Fallido:
                self.no_fallidos.append(nombre)
        
        self.algoritmos_cumplen_req=[]
        
        for nombre in self.no_fallidos:
            self.Buscadores[nombre].Xopt_a_datos_Stubs()
            DCA=int(float(self.Clinea.datos[3][0]))
            DGA=int(float(self.Clinea.datos[3][1]))
            Pmax=float(self.Clinea.datos[1][1])
            
            self.Buscadores[nombre].vectorD = vectordistancias(self.Buscadores[nombre].datos,DCA,DGA)
            self.Buscadores[nombre].Zins_original=self.Buscadores[nombre].calcularZins(self.F,
                                                                                       self.Clinea.Alfa_original,
                                                                                       self.Clinea.Beta_original,
                                                                                       self.Clinea.Zc_original)
            self.Buscadores[nombre].Zins=copia_dic(self.Buscadores[nombre].Zins_original)
            self.Buscadores[nombre].crear_grafica('Coeficiente de reflexión','Magnitud',
                                                  self.Cgenerador.Voltaje_original,self.Cgenerador.Impedancia_original,
                                                  self.Clinea.Alfa_original,self.Clinea.Beta_original,self.Clinea.Zc_original,
                                                  self.Clinea.rlgc_vs_f_original,Pmax,DCA,DGA,self.Ccarga.Z,self.F,
                                                  self.Buscadores[nombre].posicion_entrada_adaptador)
            
            if not self.Buscadores[nombre].grafica_supera_valor(self.Buscadores[nombre].grafica,float(self.Cobjetivo.datos[0][0])):
                self.algoritmos_cumplen_req.append(nombre)
            else:
                pass
                                                                            

       
if __name__ == "__main__":
    freeze_support()
    
    app = QtWidgets.QApplication([])
    
    window = MainWindow()
    timer=QTimer()
    mensaje_inicial=MensajeInicial('')
    
    timer.singleShot(800, mensaje_inicial.mensaje_1)
    timer.singleShot(3800, mensaje_inicial.mensaje_2)
    timer.singleShot(5800, mensaje_inicial.mensaje_3)
    timer.singleShot(9800, mensaje_inicial.mensaje_4)
    timer.singleShot(10500, mensaje_inicial.close)
    
    mensaje_inicial.exec()
    
    window.show()
        
    app.exec_()
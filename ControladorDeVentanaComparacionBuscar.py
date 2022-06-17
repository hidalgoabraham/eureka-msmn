# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

from ventana_comparacion_buscar_ui import Ui_Dialog as ventanacomparacion
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
from Funciones import matriz_ordenada
import ctypes
from PyQt5.QtCore import Qt

class ControladorDeVentanaComparacionBuscar(QtWidgets.QDialog,ventanacomparacion):
    
    def __init__(self,Buscadores):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self) 
        
        self.setWindowFlags(Qt.WindowCloseButtonHint)
                
        self.setWindowTitle('Figuras de mérito')
        
        resolucion=ctypes.windll.user32
        ancho=resolucion.GetSystemMetrics(0)
        
        if ancho > 1339 :
            self.setMinimumWidth(1353)
            self.setMaximumWidth(1353)
            self.scllarea.setMinimumWidth(1331)
            self.scllarea.setMaximumWidth(1331)
            
        elif ancho < 1339 and ancho > 800:
            self.setMinimumWidth(972)
            self.setMaximumWidth(972)
            self.scllarea.setMinimumWidth(951)
            self.scllarea.setMaximumWidth(951)
            
        elif ancho <= 800:
            self.setMinimumWidth(748)
            self.setMaximumWidth(748)
            self.scllarea.setMinimumWidth(727)
            self.scllarea.setMaximumWidth(727)         
        
        self.move(0,0)
        
        
        
        
        
        self.Buscadores=Buscadores
        self.W=dict() #diccionario de widgets
        for nombre in self.Buscadores:
            self.algoritmos_a_graficar=self.Buscadores[nombre].cvp.ventanaSecundariaResultados.algoritmos_a_graficar
            break
        
        f1 = str(round(self.Buscadores[nombre].cvp.ventanaSecundariaResultados.Fvisual[0],2))
        f2 = str(round(self.Buscadores[nombre].cvp.ventanaSecundariaResultados.Fvisual[-1],2))
        self.lbl_F.setText('Cálculos basados en el rango de frecuencia:\n['+f1+' - '+f2+'] MHz.')
        
        
        if len(self.Buscadores)==1:
            self.lbl_ordenar.hide()
            self.cbx_ordenar.hide()
            self.pbtn_ordenar.hide()
        elif len(self.Buscadores)>1:
            self.lbl_ordenar.show()
            self.cbx_ordenar.show()
            self.pbtn_ordenar.show()
            
        self.dic_lists=dict()
        self.dic_lists['stubs']=[]
        self.dic_lists['longitud']=[]
        self.dic_lists['perdida_Zo_fo']=[]
        self.dic_lists['max_perdida_Zo']=[]
        self.dic_lists['perdida_conj_fo']=[]
        self.dic_lists['max_perdida_conj']=[]
        self.dic_lists['distorsion_fase']=[]
        self.dic_lists['rizado']=[]
        self.dic_lists['gamma_fo']=[]
        self.dic_lists['max_gamma']=[]
        self.dic_lists['adaptacion_gamma']=[]
        
        self.correspondencia=dict()
        self.correspondencia['Número de stubs']='stubs'
        self.correspondencia['Longitud del adaptador']='longitud'
        self.correspondencia['Pérdida por desadaptación Zo @fo']='perdida_Zo_fo'
        self.correspondencia['Máxima pérdida por desadaptación Zo']='max_perdida_Zo'
        self.correspondencia['Pérdida por desadaptación conjugada @fo']='perdida_conj_fo'
        self.correspondencia['Máxima pérdida por desadaptación conjugada']='max_perdida_conj'
        self.correspondencia['Distorsión de fase']='distorsion_fase'
        self.correspondencia['Máxima variación de |Γ|']='rizado'
        self.correspondencia['|Γ| @fo']='gamma_fo'
        self.correspondencia['Máximo |Γ|']='max_gamma'
        self.correspondencia['Adaptación |Γ|']='adaptacion_gamma'
        
        for clave in self.dic_lists:
            for nombre in self.algoritmos_a_graficar:      
                self.dic_lists[clave].append(self.Buscadores[nombre].FigurasDeMerito[clave])
            
        i=0    
        for nombre in self.algoritmos_a_graficar:
            i+=1
            self.W['lbl_nombre'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_stubs'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_longitud'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_perdida_Zo_fo'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_max_perdida_Zo'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_perdida_conj_fo'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_max_perdida_conj'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_distorsion_fase'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_rizado'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_gamma_fo'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_max_gamma'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_adaptacion_gamma'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            
            self.layout.addWidget(self.W['lbl_nombre'+str(i)],i,0,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_stubs'+str(i)],i,1,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_longitud'+str(i)],i,2,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_perdida_Zo_fo'+str(i)],i,3,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_max_perdida_Zo'+str(i)],i,4,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_perdida_conj_fo'+str(i)],i,5,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_max_perdida_conj'+str(i)],i,6,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_distorsion_fase'+str(i)],i,7,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_rizado'+str(i)],i,8,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_gamma_fo'+str(i)],i,9,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_max_gamma'+str(i)],i,10,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_adaptacion_gamma'+str(i)],i,11,alignment=Qt.AlignHCenter)
            
        for key in self.W:
            self.W[key].setStyleSheet("""
                                        QLabel{
                                        color: rgb(238, 238, 238);
                                        font: 75 10pt "MS Shell Dlg 2";
                                        }
                                        QToolTip{ 
                                        background-color: rgb(79, 93, 108); 
                                        color: rgb(238, 238, 238); 
                                        border: black solid 2px;
                                        }
                                        """)
            
        self.cbx_ordenar.setCurrentText('Adaptación |Γ|')
        self.mayor_a_menor=False
        self.accion_pbtn_ordenar()
            
        self.pbtn_ordenar.clicked.connect(self.accion_pbtn_ordenar)
        self.cbx_ordenar.currentTextChanged.connect(self.accion_cbx_ordenar)
        
    def accion_cbx_ordenar(self):
        self.ordenar()
        
    def accion_pbtn_ordenar(self):
        if self.pbtn_ordenar.text()=='Menor a mayor ↓': self.pbtn_ordenar.setText('Mayor a menor ↓')
        elif self.pbtn_ordenar.text()=='Mayor a menor ↓': self.pbtn_ordenar.setText('Menor a mayor ↓')
        self.mayor_a_menor = not self.mayor_a_menor
        self.ordenar()
        
    def ordenar(self):
        texto=self.cbx_ordenar.currentText()
        clave=self.correspondencia[texto]
        self.dic_lists[clave]=sorted(self.dic_lists[clave],reverse=self.mayor_a_menor)
        por_revisar=dict()
        for nombre in self.algoritmos_a_graficar: por_revisar[nombre]='Whatever'
        
        for i in range(len(self.dic_lists[clave])):
            for nombre in por_revisar:
                if self.Buscadores[nombre].FigurasDeMerito[clave]==self.dic_lists[clave][i]:
                    del por_revisar[nombre]
                    
                    self.W['lbl_nombre'+str(i+1)].setText(self.Buscadores[nombre].FigurasDeMerito['nombre'])
                    
                    self.W['lbl_stubs'+str(i+1)].setText(str(self.Buscadores[nombre].FigurasDeMerito['stubs']))
                    
                    self.W['lbl_longitud'+str(i+1)].setText(str(self.Buscadores[nombre].FigurasDeMerito['longitud']))
                    
                    self.W['lbl_perdida_Zo_fo'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['perdida_Zo_fo'],2)))
                    
                    self.W['lbl_max_perdida_Zo'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['max_perdida_Zo'],2)))
                    self.W['lbl_max_perdida_Zo'+str(i+1)].setToolTip('@f= '+str(round(self.Buscadores[nombre].FigurasDeMerito['f_max_perdida_Zo'],2))+' MHz')
                    
                    self.W['lbl_perdida_conj_fo'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['perdida_conj_fo'],2)))
                    
                    self.W['lbl_max_perdida_conj'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['max_perdida_conj'],2)))
                    self.W['lbl_max_perdida_conj'+str(i+1)].setToolTip('@f= '+str(round(self.Buscadores[nombre].FigurasDeMerito['f_max_perdida_conj'],2))+' MHz')
                    
                    self.W['lbl_distorsion_fase'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['distorsion_fase'],2)))
                    
                    self.W['lbl_rizado'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['rizado'],3)))
                    
                    self.W['lbl_gamma_fo'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['gamma_fo'],3)))
                    
                    self.W['lbl_max_gamma'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['max_gamma'],3)))
                    self.W['lbl_max_gamma'+str(i+1)].setToolTip('@f= '+str(round(self.Buscadores[nombre].FigurasDeMerito['f_max_gamma'],2))+' MHz')
                    
                    self.W['lbl_adaptacion_gamma'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['adaptacion_gamma'],2)))
                    
                    break
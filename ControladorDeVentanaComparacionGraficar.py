# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

from ventana_comparacion_graficar_ui import Ui_Dialog as ventanacomparacion
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt
import ctypes
from PyQt5.QtCore import Qt

class ControladorDeVentanaComparacionGraficar(QtWidgets.QDialog,ventanacomparacion):
    
    def __init__(self,FigurasDeMerito,F):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self) 
        
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        
        resolucion=ctypes.windll.user32
        ancho=resolucion.GetSystemMetrics(0)
        
        if ancho > 1339 :
            self.setMinimumWidth(1163)
            self.setMaximumWidth(1163)
            self.scllarea.setMinimumWidth(1141)
            self.scllarea.setMaximumWidth(1141)
            
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
        
        f1 = str(round(F[0],2))
        f2 = str(round(F[-1],2))
        self.lbl_F.setText('Cálculos basados en el rango de frecuencia: ['+f1+' - '+f2+'] MHz.')
        
        
        
        self.FigurasDeMerito=FigurasDeMerito
        self.W=dict() #diccionario de widgets
        
        self.W['lbl_stubs']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_longitud']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_perdida_Zo_fo']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_max_perdida_Zo']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_perdida_conj_fo']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_max_perdida_conj']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_distorsion_fase']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_rizado']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_gamma_fo']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_max_gamma']=QLabel('',alignment=Qt.AlignHCenter)
        self.W['lbl_adaptacion_gamma']=QLabel('',alignment=Qt.AlignHCenter)
        
        self.layout.addWidget(self.W['lbl_stubs'],1,0,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_longitud'],1,1,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_perdida_Zo_fo'],1,2,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_max_perdida_Zo'],1,3,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_perdida_conj_fo'],1,4,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_max_perdida_conj'],1,5,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_distorsion_fase'],1,6,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_rizado'],1,7,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_gamma_fo'],1,8,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_max_gamma'],1,9,alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.W['lbl_adaptacion_gamma'],1,10,alignment=Qt.AlignHCenter)
            
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
                                        
                    
        self.W['lbl_stubs'].setText(str(self.FigurasDeMerito['stubs']))
        
        self.W['lbl_longitud'].setText(str(self.FigurasDeMerito['longitud']))
        
        self.W['lbl_perdida_Zo_fo'].setText(str(round(self.FigurasDeMerito['perdida_Zo_fo'],2)))
        
        self.W['lbl_max_perdida_Zo'].setText(str(round(self.FigurasDeMerito['max_perdida_Zo'],2)))
        self.W['lbl_max_perdida_Zo'].setToolTip('@f= '+str(round(self.FigurasDeMerito['f_max_perdida_Zo'],2))+' MHz')
        
        self.W['lbl_perdida_conj_fo'].setText(str(round(self.FigurasDeMerito['perdida_conj_fo'],2)))
        
        self.W['lbl_max_perdida_conj'].setText(str(round(self.FigurasDeMerito['max_perdida_conj'],2)))
        self.W['lbl_max_perdida_conj'].setToolTip('@f= '+str(round(self.FigurasDeMerito['f_max_perdida_conj'],2))+' MHz')
        
        self.W['lbl_distorsion_fase'].setText(str(round(self.FigurasDeMerito['distorsion_fase'],2)))
        
        self.W['lbl_rizado'].setText(str(round(self.FigurasDeMerito['rizado'],3)))
        
        self.W['lbl_gamma_fo'].setText(str(round(self.FigurasDeMerito['gamma_fo'],3)))
        
        self.W['lbl_max_gamma'].setText(str(round(self.FigurasDeMerito['max_gamma'],3)))
        self.W['lbl_max_gamma'].setToolTip('@f= '+str(round(self.FigurasDeMerito['f_max_gamma'],2))+' MHz')
        
        self.W['lbl_adaptacion_gamma'].setText(str(round(self.FigurasDeMerito['adaptacion_gamma'],2)))
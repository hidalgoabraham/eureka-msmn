# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

from ventana_metadata_ui import Ui_Dialog as ventana_metadata
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

class ControladorDeVentanaMetadata(QtWidgets.QDialog,ventana_metadata):
    
    def __init__(self,Buscadores):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self) 
        
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        
        self.Buscadores=Buscadores
        self.W=dict() #diccionario de widgets
        if len(self.Buscadores)==1:
            self.lbl_ordenar.hide()
            self.cbx_ordenar.hide()
            self.pbtn_ordenar.hide()
        elif len(self.Buscadores)>1:
            self.lbl_ordenar.show()
            self.cbx_ordenar.show()
            self.pbtn_ordenar.show()
            
        self.dic_lists=dict()
        self.dic_lists['cpu']=[]
        self.dic_lists['ram']=[]
        self.dic_lists['tiempo']=[]
        
        self.correspondencia=dict()
        self.correspondencia['Uso de CPU']='cpu'
        self.correspondencia['Memoria máxima utilizada']='ram'
        self.correspondencia['Tiempo de búsqueda']='tiempo'
        
        for clave in self.dic_lists:
            for nombre in self.Buscadores:           
                self.dic_lists[clave].append(self.Buscadores[nombre].FigurasDeMerito[clave])
            
        i=0    
        for nombre in self.Buscadores:
            i+=1
            self.W['lbl_nombre'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_cpu'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_ram'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            self.W['lbl_tiempo'+str(i)]=QLabel('',alignment=Qt.AlignHCenter)
            
            self.layout.addWidget(self.W['lbl_nombre'+str(i)],i,0,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_cpu'+str(i)],i,1,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_ram'+str(i)],i,2,alignment=Qt.AlignHCenter)
            self.layout.addWidget(self.W['lbl_tiempo'+str(i)],i,3,alignment=Qt.AlignHCenter)
            
        for key in self.W:
            self.W[key].setStyleSheet("""
                                        color:rgb(238, 238, 238);
                                        font: 75 10pt "MS Shell Dlg 2";
                                        """)
            
        self.cbx_ordenar.setCurrentText('Uso de CPU')
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
        for nombre in self.Buscadores: por_revisar[nombre]='Whatever'
        
        for i in range(len(self.dic_lists[clave])):
            for nombre in por_revisar:
                if self.Buscadores[nombre].FigurasDeMerito[clave]==self.dic_lists[clave][i]:
                    del por_revisar[nombre]
                    self.W['lbl_nombre'+str(i+1)].setText(self.Buscadores[nombre].FigurasDeMerito['nombre'])
                    self.W['lbl_cpu'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['cpu'],2)))
                    self.W['lbl_ram'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['ram'],2)))
                    self.W['lbl_tiempo'+str(i+1)].setText(str(round(self.Buscadores[nombre].FigurasDeMerito['tiempo'],2)))
                    break
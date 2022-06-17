# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

from advertencia_salir_ui import Ui_Dialog as Advertencia_salir
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class adv_salir(QtWidgets.QDialog,Advertencia_salir):
    def __init__(self,ventana,texto):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)        
        
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        
        self.cv=ventana
        self.lbl.setText(texto)
        self.pbtn_si.clicked.connect(self.si)
        self.pbtn_no.clicked.connect(self.no)
        
    def si(self):
        self.cv.evento_salir=True
        self.close()
        
    def no(self):
        self.cv.evento_salir=False
        self.close()
        
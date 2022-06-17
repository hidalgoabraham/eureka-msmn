# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

from advertencia_ui import Ui_Dialog as Advertencia
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class adv(QtWidgets.QDialog,Advertencia):
    def __init__(self, texto):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)

        self.setWindowFlags(Qt.WindowCloseButtonHint)
        
        self.lbl.setText(texto)
        self.pbtn.clicked.connect(self.cerrar)
        
    def cerrar(self):
        self.close()
        
        
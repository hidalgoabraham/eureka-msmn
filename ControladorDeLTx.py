# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""
from PyQt5.QtGui import QDoubleValidator

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from linea_coaxial_ui import Ui_Dialog as LineaCoaxial
from linea_bifilar_ui import Ui_Dialog as LineaBifilar
from linea_plana_ui import Ui_Dialog as LineaPlana
from functools import partial
from PyQt5.QtCore import Qt

def ControladorDeLTx(Clinea):
    if Clinea.WL['cbx_ltx'].currentText()=='Coaxial': return Ventana_LineaCoaxial(Clinea)
    elif Clinea.WL['cbx_ltx'].currentText()=='Bifilar': return Ventana_LineaBifilar(Clinea)
    elif Clinea.WL['cbx_ltx'].currentText()=='Plana': return Ventana_LineaPlana(Clinea) 
    
        
class Ventana_LineaCoaxial(QtWidgets.QDialog,LineaCoaxial):
    def __init__(self,Clinea):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        
        self.linedit_dim1.setValidator(QDoubleValidator())
        self.linedit_dim2.setValidator(QDoubleValidator())
        self.linedit_urc.setValidator(QDoubleValidator())
        self.linedit_Dc.setValidator(QDoubleValidator())
        self.linedit_urd.setValidator(QDoubleValidator())
        self.linedit_erd.setValidator(QDoubleValidator())
        self.linedit_Dd.setValidator(QDoubleValidator())
                
        self.Clinea=Clinea
        self.llenar_widgets()
        self.ignorar_senhales=False
                
        #Conexiones
        self.linedit_dim1.editingFinished.connect(partial(self.editing_finished,self.linedit_dim1,2,1))
        self.linedit_dim2.editingFinished.connect(partial(self.editing_finished,self.linedit_dim2,2,2))
        self.linedit_urc.editingFinished.connect(partial(self.editing_finished,self.linedit_urc,2,3))
        self.linedit_Dc.editingFinished.connect(partial(self.editing_finished,self.linedit_Dc,2,4))
        self.linedit_urd.editingFinished.connect(partial(self.editing_finished,self.linedit_urd,2,5))
        self.linedit_erd.editingFinished.connect(partial(self.editing_finished,self.linedit_erd,2,6))
        self.linedit_Dd.editingFinished.connect(partial(self.editing_finished,self.linedit_Dd,2,7))
        
        self.linedit_dim1.textChanged.connect(partial(self.text_changed,self.linedit_dim1,2,1))
        self.linedit_dim2.textChanged.connect(partial(self.text_changed,self.linedit_dim2,2,2))
        self.linedit_urc.textChanged.connect(partial(self.text_changed,self.linedit_urc,2,3))
        self.linedit_Dc.textChanged.connect(partial(self.text_changed,self.linedit_Dc,2,4))
        self.linedit_urd.textChanged.connect(partial(self.text_changed,self.linedit_urd,2,5))
        self.linedit_erd.textChanged.connect(partial(self.text_changed,self.linedit_erd,2,6))
        self.linedit_Dd.textChanged.connect(partial(self.text_changed,self.linedit_Dd,2,7))
        
        self.cbx_dim1.currentTextChanged.connect(self.accion_cbx_dim1)
        self.cbx_dim2.currentTextChanged.connect(self.accion_cbx_dim2)
        
        self.pbtn.clicked.connect(self.cerrar)
        
        self.pbtn.setFocusPolicy(Qt.NoFocus)
        
    def llenar_widgets(self):
        self.linedit_dim1.setText(str(self.Clinea.datos[2][1]))
        self.linedit_dim2.setText(str(self.Clinea.datos[2][2]))
        self.linedit_urc.setText(str(self.Clinea.datos[2][3]))
        self.linedit_Dc.setText(str(self.Clinea.datos[2][4]))
        self.linedit_urd.setText(str(self.Clinea.datos[2][5]))
        self.linedit_erd.setText(str(self.Clinea.datos[2][6]))
        self.linedit_Dd.setText(str(self.Clinea.datos[2][7]))
        
        self.linedit_dim1.setCursorPosition(0)
        self.linedit_dim2.setCursorPosition(0)
        self.linedit_urc.setCursorPosition(0)
        self.linedit_Dc.setCursorPosition(0)
        self.linedit_urd.setCursorPosition(0)
        self.linedit_erd.setCursorPosition(0)
        self.linedit_Dd.setCursorPosition(0)
        
    def text_changed(self,linedit,fila,columna):
        self.ignorar_senhales=True
        self.Clinea.datos[fila][columna]=linedit.text()
        self.ignorar_senhales=False
        
    def editing_finished(self,linedit,fila,columna):
        if self.ignorar_senhales: return
        linedit.setCursorPosition(0)
        try: self.Clinea.datos[fila][columna]=float(linedit.text())*self.multiplicador(fila,columna)
        except: pass
    
    def multiplicador(self,fila,columna):
        if fila==2 and columna==1: #dim1
            if self.cbx_dim1.currentText()=='in': mult=25.4
            elif self.cbx_dim1.currentText()=='cm': mult=10
            elif self.cbx_dim1.currentText()=='mm': mult=1
        
        elif fila==2 and columna==2: #dim2
            if self.cbx_dim2.currentText()=='in': mult=25.4
            elif self.cbx_dim2.currentText()=='cm': mult=10
            elif self.cbx_dim2.currentText()=='mm': mult=1
            
        return mult
        
    def accion_cbx_dim1(self):
        if self.ignorar_senhales: return
        
        if self.cbx_dim1.currentText()=='in': mult=25.4
        elif self.cbx_dim1.currentText()=='cm': mult=10
        elif self.cbx_dim1.currentText()=='mm': mult=1
        
        try: self.Clinea.datos[2][1]=float(self.linedit_dim1.text())*mult
        except: pass
    
    def accion_cbx_dim2(self):
        if self.ignorar_senhales: return
        
        if self.cbx_dim1.currentText()=='in': mult=25.4
        elif self.cbx_dim1.currentText()=='cm': mult=10
        elif self.cbx_dim1.currentText()=='mm': mult=1
        
        try: self.Clinea.datos[2][2]=float(self.linedit_dim2.text())*mult
        except: pass
        
    def cerrar(self): self.close()
    

class Ventana_LineaBifilar(QtWidgets.QDialog,LineaBifilar):
    def __init__(self,Clinea):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        
        self.linedit_dim1.setValidator(QDoubleValidator())
        self.linedit_dim2.setValidator(QDoubleValidator())
        self.linedit_urc.setValidator(QDoubleValidator())
        self.linedit_Dc.setValidator(QDoubleValidator())
        self.linedit_urd.setValidator(QDoubleValidator())
        self.linedit_erd.setValidator(QDoubleValidator())
        self.linedit_Dd.setValidator(QDoubleValidator())
                
        self.Clinea=Clinea
        self.llenar_widgets()
        self.ignorar_senhales=False
                
        #Conexiones
        self.linedit_dim1.editingFinished.connect(partial(self.editing_finished,self.linedit_dim1,2,1))
        self.linedit_dim2.editingFinished.connect(partial(self.editing_finished,self.linedit_dim2,2,2))
        self.linedit_urc.editingFinished.connect(partial(self.editing_finished,self.linedit_urc,2,3))
        self.linedit_Dc.editingFinished.connect(partial(self.editing_finished,self.linedit_Dc,2,4))
        self.linedit_urd.editingFinished.connect(partial(self.editing_finished,self.linedit_urd,2,5))
        self.linedit_erd.editingFinished.connect(partial(self.editing_finished,self.linedit_erd,2,6))
        self.linedit_Dd.editingFinished.connect(partial(self.editing_finished,self.linedit_Dd,2,7))
        
        self.linedit_dim1.textChanged.connect(partial(self.text_changed,self.linedit_dim1,2,1))
        self.linedit_dim2.textChanged.connect(partial(self.text_changed,self.linedit_dim2,2,2))
        self.linedit_urc.textChanged.connect(partial(self.text_changed,self.linedit_urc,2,3))
        self.linedit_Dc.textChanged.connect(partial(self.text_changed,self.linedit_Dc,2,4))
        self.linedit_urd.textChanged.connect(partial(self.text_changed,self.linedit_urd,2,5))
        self.linedit_erd.textChanged.connect(partial(self.text_changed,self.linedit_erd,2,6))
        self.linedit_Dd.textChanged.connect(partial(self.text_changed,self.linedit_Dd,2,7))
        
        self.cbx_dim1.currentTextChanged.connect(self.accion_cbx_dim1)
        self.cbx_dim2.currentTextChanged.connect(self.accion_cbx_dim2)
        
        self.pbtn.clicked.connect(self.cerrar)
        
        self.pbtn.setFocusPolicy(Qt.NoFocus)
        
    def llenar_widgets(self):
        self.linedit_dim1.setText(str(self.Clinea.datos[2][1]))
        self.linedit_dim2.setText(str(self.Clinea.datos[2][2]))
        self.linedit_urc.setText(str(self.Clinea.datos[2][3]))
        self.linedit_Dc.setText(str(self.Clinea.datos[2][4]))
        self.linedit_urd.setText(str(self.Clinea.datos[2][5]))
        self.linedit_erd.setText(str(self.Clinea.datos[2][6]))
        self.linedit_Dd.setText(str(self.Clinea.datos[2][7]))
        
        self.linedit_dim1.setCursorPosition(0)
        self.linedit_dim2.setCursorPosition(0)
        self.linedit_urc.setCursorPosition(0)
        self.linedit_Dc.setCursorPosition(0)
        self.linedit_urd.setCursorPosition(0)
        self.linedit_erd.setCursorPosition(0)
        self.linedit_Dd.setCursorPosition(0)
        
    def text_changed(self,linedit,fila,columna):
        self.ignorar_senhales=True
        self.Clinea.datos[fila][columna]=linedit.text()
        self.ignorar_senhales=False
        
    def editing_finished(self,linedit,fila,columna):
        if self.ignorar_senhales: return
        linedit.setCursorPosition(0)
        try: self.Clinea.datos[fila][columna]=float(linedit.text())*self.multiplicador(fila,columna)
        except: pass
    
    def multiplicador(self,fila,columna):
        if fila==2 and columna==1: #dim1
            if self.cbx_dim1.currentText()=='in': mult=25.4
            elif self.cbx_dim1.currentText()=='cm': mult=10
            elif self.cbx_dim1.currentText()=='mm': mult=1
        
        elif fila==2 and columna==2: #dim2
            if self.cbx_dim2.currentText()=='in': mult=25.4
            elif self.cbx_dim2.currentText()=='cm': mult=10
            elif self.cbx_dim2.currentText()=='mm': mult=1
            
        return mult
        
    def accion_cbx_dim1(self):
        if self.ignorar_senhales: return
        
        if self.cbx_dim1.currentText()=='in': mult=25.4
        elif self.cbx_dim1.currentText()=='cm': mult=10
        elif self.cbx_dim1.currentText()=='mm': mult=1
        
        try: self.Clinea.datos[2][1]=float(self.linedit_dim1.text())*mult
        except: pass
    
    def accion_cbx_dim2(self):
        if self.ignorar_senhales: return
        
        if self.cbx_dim1.currentText()=='in': mult=25.4
        elif self.cbx_dim1.currentText()=='cm': mult=10
        elif self.cbx_dim1.currentText()=='mm': mult=1
        
        try: self.Clinea.datos[2][2]=float(self.linedit_dim2.text())*mult
        except: pass
        
    def cerrar(self): self.close()
    
    
class Ventana_LineaPlana(QtWidgets.QDialog,LineaPlana):
    def __init__(self,Clinea):
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        
        self.linedit_dim1.setValidator(QDoubleValidator())
        self.linedit_dim2.setValidator(QDoubleValidator())
        self.linedit_urc.setValidator(QDoubleValidator())
        self.linedit_Dc.setValidator(QDoubleValidator())
        self.linedit_urd.setValidator(QDoubleValidator())
        self.linedit_erd.setValidator(QDoubleValidator())
        self.linedit_Dd.setValidator(QDoubleValidator())
                
        self.Clinea=Clinea
        self.llenar_widgets()
        self.ignorar_senhales=False
                
        #Conexiones
        self.linedit_dim1.editingFinished.connect(partial(self.editing_finished,self.linedit_dim1,2,1))
        self.linedit_dim2.editingFinished.connect(partial(self.editing_finished,self.linedit_dim2,2,2))
        self.linedit_urc.editingFinished.connect(partial(self.editing_finished,self.linedit_urc,2,3))
        self.linedit_Dc.editingFinished.connect(partial(self.editing_finished,self.linedit_Dc,2,4))
        self.linedit_urd.editingFinished.connect(partial(self.editing_finished,self.linedit_urd,2,5))
        self.linedit_erd.editingFinished.connect(partial(self.editing_finished,self.linedit_erd,2,6))
        self.linedit_Dd.editingFinished.connect(partial(self.editing_finished,self.linedit_Dd,2,7))
        
        self.linedit_dim1.textChanged.connect(partial(self.text_changed,self.linedit_dim1,2,1))
        self.linedit_dim2.textChanged.connect(partial(self.text_changed,self.linedit_dim2,2,2))
        self.linedit_urc.textChanged.connect(partial(self.text_changed,self.linedit_urc,2,3))
        self.linedit_Dc.textChanged.connect(partial(self.text_changed,self.linedit_Dc,2,4))
        self.linedit_urd.textChanged.connect(partial(self.text_changed,self.linedit_urd,2,5))
        self.linedit_erd.textChanged.connect(partial(self.text_changed,self.linedit_erd,2,6))
        self.linedit_Dd.textChanged.connect(partial(self.text_changed,self.linedit_Dd,2,7))
        
        self.cbx_dim1.currentTextChanged.connect(self.accion_cbx_dim1)
        self.cbx_dim2.currentTextChanged.connect(self.accion_cbx_dim2)
        
        self.pbtn.clicked.connect(self.cerrar)
        
        self.pbtn.setFocusPolicy(Qt.NoFocus)
        
    def llenar_widgets(self):
        self.linedit_dim1.setText(str(self.Clinea.datos[2][1]))
        self.linedit_dim2.setText(str(self.Clinea.datos[2][2]))
        self.linedit_urc.setText(str(self.Clinea.datos[2][3]))
        self.linedit_Dc.setText(str(self.Clinea.datos[2][4]))
        self.linedit_urd.setText(str(self.Clinea.datos[2][5]))
        self.linedit_erd.setText(str(self.Clinea.datos[2][6]))
        self.linedit_Dd.setText(str(self.Clinea.datos[2][7]))
        
        self.linedit_dim1.setCursorPosition(0)
        self.linedit_dim2.setCursorPosition(0)
        self.linedit_urc.setCursorPosition(0)
        self.linedit_Dc.setCursorPosition(0)
        self.linedit_urd.setCursorPosition(0)
        self.linedit_erd.setCursorPosition(0)
        self.linedit_Dd.setCursorPosition(0)
        
    def text_changed(self,linedit,fila,columna):
        self.ignorar_senhales=True
        self.Clinea.datos[fila][columna]=linedit.text()
        self.ignorar_senhales=False
        
    def editing_finished(self,linedit,fila,columna):
        if self.ignorar_senhales: return
        linedit.setCursorPosition(0)
        try: self.Clinea.datos[fila][columna]=float(linedit.text())*self.multiplicador(fila,columna)
        except: pass
    
    def multiplicador(self,fila,columna):
        if fila==2 and columna==1: #dim1
            if self.cbx_dim1.currentText()=='in': mult=25.4
            elif self.cbx_dim1.currentText()=='cm': mult=10
            elif self.cbx_dim1.currentText()=='mm': mult=1
        
        elif fila==2 and columna==2: #dim2
            if self.cbx_dim2.currentText()=='in': mult=25.4
            elif self.cbx_dim2.currentText()=='cm': mult=10
            elif self.cbx_dim2.currentText()=='mm': mult=1
            
        return mult
        
    def accion_cbx_dim1(self):
        if self.ignorar_senhales: return
        
        if self.cbx_dim1.currentText()=='in': mult=25.4
        elif self.cbx_dim1.currentText()=='cm': mult=10
        elif self.cbx_dim1.currentText()=='mm': mult=1
        
        try: self.Clinea.datos[2][1]=float(self.linedit_dim1.text())*mult
        except: pass
    
    def accion_cbx_dim2(self):
        if self.ignorar_senhales: return
        
        if self.cbx_dim1.currentText()=='in': mult=25.4
        elif self.cbx_dim1.currentText()=='cm': mult=10
        elif self.cbx_dim1.currentText()=='mm': mult=1
        
        try: self.Clinea.datos[2][2]=float(self.linedit_dim2.text())*mult
        except: pass
        
    def cerrar(self): self.close()
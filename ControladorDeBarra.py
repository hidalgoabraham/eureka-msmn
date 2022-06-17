# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

class ControladorDeBarra:#Clase para darle funcionalidad al QSlider
    
    def __init__(self,ventana_secundaria):                                                                  
        self.cvs=ventana_secundaria
        self.posicion=0 #posicion actual en mm sobre el eje d
        self.indiceStub=0 #Indice del stub, si no es stub este indice es cero
        self.esStub=False
        self.supera_potencia=False
        self.cvs.slider.setMinimum(0)
        self.largo=0 #Que tan largo es el adapter
        self.configurando=False
            
        #Conexión
        self.cvs.slider.valueChanged.connect(self.actualizar)
    
    def configurar(self,D,posicion=None):
        self.configurando=True
        self.cvs.slider.blockSignals(True)
        self.D=D
        self.largo=self.D[-1].posicion
        self.cvs.slider.setMaximum(self.D[-1].posicion)
        if posicion==None:
            if self.posicion <= self.cvs.slider.maximum(): self.cvs.slider.setValue(self.posicion)
            else: self.cvs.slider.setValue(self.D[-1].posicion)
        elif posicion==-1: 
            self.cvs.slider.setValue(self.D[-1].posicion)
        else:
            self.cvs.slider.setValue(posicion)
                
        self.cvs.slider.blockSignals(False)
        self.actualizar()
        self.configurando=False
        
    def copiar_D(self,D): self.D=D
        
    def set_position(self,position=None):
        if position is None: return
        if position <= self.cvs.slider.maximum() and position >= self.cvs.slider.minimum() : 
            self.cvs.slider.setValue(position)
        elif position < self.cvs.slider.minimum():
            if position != -1 : self.cvs.slider.setValue(self.cvs.slider.minimum())
            elif position == -1 : self.cvs.slider.setValue(self.cvs.slider.maximum())
        elif position > self.cvs.slider.maximum():
            self.cvs.slider.setValue(self.cvs.slider.maximum())
            
        
    def mostrar(self):
        self.cvs.slider.show()
        self.cvs.lbl_d.show()
        self.cvs.lbl_dn.show()
        self.actualizar_lbl()
        
    def ocultar(self):
        self.cvs.slider.hide()
        self.cvs.lbl_d.hide()
        self.cvs.lbl_dn.hide()
        self.cvs.lbl_alertastub.hide()
        self.cvs.lbl_entrada_msmn.hide()
        #self.cvs.lbl_warning_potencia.hide()
        
    def actualizar(self):    
        try:
            self.posicion=self.cvs.slider.value()
            self.indiceStub=self.D[self.posicion].indiceStub
            self.esStub=self.D[self.posicion].esStub
            self.cvs.lbl_dn.setText(str(self.posicion)+' mm')   
            if self.esStub:
                self.cvs.lbl_alertastub.setText('Stub '+str(self.indiceStub))
                if self.indiceStub > 0 : self.cvs.lbl_alertastub.show()
                else: self.cvs.lbl_alertastub.hide()
            else: 
                self.cvs.lbl_alertastub.hide()
                
            if self.cvs.bandera=='buscar':
                algoritmo=self.cvs.cvp.Buscadores[self.cvs.cbx_algoritmos.currentText()]
                if self.posicion==algoritmo.posicion_entrada_adaptador: self.cvs.lbl_entrada_msmn.show()
                else: self.cvs.lbl_entrada_msmn.hide()
                
            elif self.cvs.bandera=='graficar':
                if self.posicion==self.cvs.posicion_entrada_adaptador: self.cvs.lbl_entrada_msmn.show()
                else: self.cvs.lbl_entrada_msmn.hide()
                
                
            if not self.cvs.slider.isSliderDown(): self.cvs.Cgrafica.actualizarporbarra()
        except:
            pass
        
    def actualizar_lbl(self):
        try:
            self.posicion=self.cvs.slider.value()
            self.indiceStub=self.D[self.posicion].indiceStub
            self.esStub=self.D[self.posicion].esStub
            self.cvs.lbl_dn.setText(str(self.posicion)+' mm')   
            if self.esStub:
                self.cvs.lbl_alertastub.setText('Stub '+str(self.indiceStub))
                if self.indiceStub > 0 : self.cvs.lbl_alertastub.show()
                else: self.cvs.lbl_alertastub.hide()
            else: 
                self.cvs.lbl_alertastub.hide()
                
            if self.cvs.bandera=='buscar':
                algoritmo=self.cvs.cvp.Buscadores[self.cvs.cbx_algoritmos.currentText()]
                if self.posicion==algoritmo.posicion_entrada_adaptador: self.cvs.lbl_entrada_msmn.show()
                else: self.cvs.lbl_entrada_msmn.hide()
                
            elif self.cvs.bandera=='graficar':
                if self.posicion==self.cvs.posicion_entrada_adaptador: self.cvs.lbl_entrada_msmn.show()
                else: self.cvs.lbl_entrada_msmn.hide()
                
                
        except:
            pass
        
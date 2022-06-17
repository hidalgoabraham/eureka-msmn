# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""
from numpy import linspace
from PyQt5.QtGui import QDoubleValidator
from Funciones import matrizceros
from numpy import Infinity
from Advertencia import adv
from functools import partial

class ControladorDeObjetivo:
    def __init__(self,ventana_principal):
        self.cvp=ventana_principal
        self.cvp.cbx_bw.setCurrentText('MHz')
        self.cvp.cbx_fo.setCurrentText('MHz')
        self.datos=self.plantilla_datos()
        self.funcion_objetivo=None
        self.chkbxs=dict() # diccionario para almacenar los checkbox de los algoritmos
        
        self.ignorar_senhales=False
        
        #Validators
        self.cvp.linedit_bw.setValidator(QDoubleValidator())
        self.cvp.linedit_fo.setValidator(QDoubleValidator())
        self.cvp.linedit_max.setValidator(QDoubleValidator())
        self.cvp.linedit_vswr.setValidator(QDoubleValidator())
        
        #Conexiones
        self.cvp.linedit_vswr.editingFinished.connect(self.editing_finished_vswr)
        self.cvp.linedit_max.editingFinished.connect(self.editing_finished_gmax)
        self.cvp.linedit_fo.editingFinished.connect(self.editing_finished_fo)
        self.cvp.linedit_bw.editingFinished.connect(self.editing_finished_bw)
        self.cvp.cbx_bw.currentTextChanged.connect(self.accion_cbx_bw)
        self.cvp.cbx_fo.currentTextChanged.connect(self.accion_cbx_fo)
        
        self.cvp.linedit_max.textChanged.connect(partial(self.text_changed,self.cvp.linedit_max,0,0))
        self.cvp.linedit_bw.textChanged.connect(partial(self.text_changed,self.cvp.linedit_bw,0,1))
        self.cvp.linedit_fo.textChanged.connect(partial(self.text_changed,self.cvp.linedit_fo,0,2))


        self.cvp.chkbx_NM.stateChanged.connect(partial(self.accion_chkbx,self.cvp.chkbx_NM))
        self.chkbxs['chkbx1']=self.cvp.chkbx_NM

        self.cvp.chkbx_DE.stateChanged.connect(partial(self.accion_chkbx,self.cvp.chkbx_DE))
        self.chkbxs['chkbx2']=self.cvp.chkbx_DE
        
        self.cvp.chkbx_DA.stateChanged.connect(partial(self.accion_chkbx,self.cvp.chkbx_DA))
        self.chkbxs['chkbx3']=self.cvp.chkbx_DA
        
        self.cvp.chkbx_BF.stateChanged.connect(partial(self.accion_chkbx,self.cvp.chkbx_BF))
        self.chkbxs['chkbx4']=self.cvp.chkbx_BF
        
        self.cvp.chkbx_WOA.stateChanged.connect(partial(self.accion_chkbx,self.cvp.chkbx_WOA))
        self.chkbxs['chkbx5']=self.cvp.chkbx_WOA
        
        self.cvp.chkbx_EO.stateChanged.connect(partial(self.accion_chkbx,self.cvp.chkbx_EO))
        self.chkbxs['chkbx6']=self.cvp.chkbx_EO
        
        self.cvp.chkbx_HHO.stateChanged.connect(partial(self.accion_chkbx,self.cvp.chkbx_HHO))
        self.chkbxs['chkbx7']=self.cvp.chkbx_HHO
        
        self.cvp.chkbx_VCS.stateChanged.connect(partial(self.accion_chkbx,self.cvp.chkbx_VCS))
        self.chkbxs['chkbx8']=self.cvp.chkbx_VCS
        
        self.cvp.chkbx_AEO.stateChanged.connect(partial(self.accion_chkbx,self.cvp.chkbx_AEO))
        self.chkbxs['chkbx9']=self.cvp.chkbx_AEO
        
############################################################ Agregar acá los Algoritmos nuevos
        
    ### Lógica de Interfaz Gráfica
    def plantilla_datos(self): 
        return [['','',''],[],[0,Infinity]]
    
    def formatear_datos(self,datos): 
        datos[0][0]=float(datos[0][0]) #Gamma_max
        datos[0][1]=float(datos[0][1]) #bw
        datos[0][2]=float(datos[0][2]) #fo
        datos[2][0]=float(datos[2][0]) #fmin
        datos[2][1]=float(datos[2][1]) #fmax
        return datos
    
    def cargar_datos(self,datos): 
        self.reiniciar()
        try: 
            if self.formato_correcto(datos): pass
            else: raise Exception
            
            self.datos=datos
            self.ignorar_senhales=True
            self.datosAventana()
            self.ignorar_senhales=False
            self.editing_finished_gmax()
            
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos de\nrequerimientos de adaptación de impedancias.')
            ad.exec_()
            self.ignorar_senhales=False
            self.reiniciar() 
        
    def reiniciar(self): 
        self.cvp.linedit_vswr.setText('')
        self.cvp.linedit_max.setText('')
        self.cvp.linedit_bw.setText('')
        self.cvp.linedit_fo.setText('')
        self.cvp.cbx_bw.setCurrentText('MHz')
        self.cvp.cbx_fo.setCurrentText('MHz')
        for chkbx in self.chkbxs: self.chkbxs[chkbx].setChecked(False)
        
    def accion_chkbx(self,chkbx): 
        if self.ignorar_senhales: return
        
        if chkbx.isChecked(): 
            if chkbx.text() not in self.datos[1]: self.datos[1].append(chkbx.text())
        else: self.datos[1].remove(chkbx.text())
        
    def editing_finished_gmax(self): 
        if self.ignorar_senhales: return
        
        self.cvp.linedit_max.setCursorPosition(0)
        try:
            g=float(self.cvp.linedit_max.text())
            
            swr=(1+g)/(1-g)
            self.cvp.linedit_vswr.setText(str(round(swr,17)))
            self.cvp.linedit_vswr.setCursorPosition(0)
            self.datos[0][0]=g
        except:
            pass
    
    def editing_finished_vswr(self): 
        if self.ignorar_senhales: return
        
        self.cvp.linedit_vswr.setCursorPosition(0)
        try:
            swr=float(self.cvp.linedit_vswr.text())
                        
            g=(swr-1)/(swr+1)
            self.cvp.linedit_max.setText(str(round(g,17)))
            self.cvp.linedit_max.setCursorPosition(0)
            self.datos[0][0]=g
        except:
            pass
        
    def text_changed(self,linedit,fila,columna):
        self.ignorar_senhales=True
        self.datos[fila][columna]=linedit.text()
        self.ignorar_senhales=False
     
    def editing_finished_bw(self): 
        if self.ignorar_senhales: return
        
        self.cvp.linedit_bw.setCursorPosition(0)
        self.datos[0][1]=float(self.cvp.linedit_bw.text())*self.multiplicador(self.cvp.cbx_bw)
        
    def editing_finished_fo(self): 
        if self.ignorar_senhales: return
        
        self.cvp.linedit_fo.setCursorPosition(0)
        self.datos[0][2]=float(self.cvp.linedit_fo.text())*self.multiplicador(self.cvp.cbx_fo)
        
    def accion_cbx_bw(self): 
        if self.ignorar_senhales: return
        
        if self.cvp.cbx_bw.currentText()=='GHz': mult=1e3
        elif self.cvp.cbx_bw.currentText()=='MHz': mult=1
        elif self.cvp.cbx_bw.currentText()=='kHz': mult=1e-3
        try: self.datos[0][1]=float(self.cvp.linedit_bw.text())*mult
        except: pass
    
    def accion_cbx_fo(self): 
        if self.ignorar_senhales: return
        
        if self.cvp.cbx_fo.currentText()=='GHz': mult=1e3
        elif self.cvp.cbx_fo.currentText()=='MHz': mult=1
        elif self.cvp.cbx_fo.currentText()=='kHz': mult=1e-3
        try: self.datos[0][2]=float(self.cvp.linedit_fo.text())*mult
        except: pass
        
    def multiplicador(self,cbx): 
        if cbx.currentText()=='GHz': mult=1e3
        elif cbx.currentText()=='MHz': mult=1
        elif cbx.currentText()=='kHz': mult=1e-3
        
        return mult
        
    def datosAventana(self): 
        self.cvp.linedit_max.setText(str(self.datos[0][0]))
        self.cvp.linedit_bw.setText(str(self.datos[0][1]))
        self.cvp.linedit_fo.setText(str(self.datos[0][2]))
        
        for algoritmo in self.datos[1]:
            for chkbx in self.chkbxs:
                if self.chkbxs[chkbx].text()==algoritmo:
                    self.chkbxs[chkbx].setChecked(True)
                    
                    
    def bloquear(self):
        self.cvp.linedit_vswr.setEnabled(False)
        self.cvp.linedit_max.setEnabled(False)
        self.cvp.linedit_bw.setEnabled(False)
        self.cvp.linedit_fo.setEnabled(False)
        self.cvp.cbx_bw.setEnabled(False)
        self.cvp.cbx_fo.setEnabled(False)
        for chkbx in self.chkbxs: self.chkbxs[chkbx].setEnabled(False)
        
    def desbloquear(self):
        self.cvp.linedit_vswr.setEnabled(True)
        self.cvp.linedit_max.setEnabled(True)
        self.cvp.linedit_bw.setEnabled(True)
        self.cvp.linedit_fo.setEnabled(True)
        self.cvp.cbx_bw.setEnabled(True)
        self.cvp.cbx_fo.setEnabled(True)
        for chkbx in self.chkbxs: self.chkbxs[chkbx].setEnabled(True)
    
    ### Lógica de Cómputo
                    
    def determinar_fmin_fmax_datos(self): 
        try:
            fmin=float(self.datos[0][2])-float(self.datos[0][1])/2
            fmax=float(self.datos[0][2])+float(self.datos[0][1])/2
            self.datos[2]=[fmin,fmax]
            self.fmin=fmin
            self.fmax=fmax
            
        except:
            self.datos[2]=['','']
            self.fmin=None
            self.fmax=None
    
    def datos_correcto(self, advertir=True):  #No verifica fmin,fmax
        # |gamma|max,BW,fo
        # Algoritmo1,Algoritmo2,...,Algoritmok
        # fmin,fmax
        try:
            if float(self.datos[0][0]) < 0 or float(self.datos[0][0]) >=1 : #|gamma|max
                if advertir:
                    ad=adv('El módulo del coeficiente de reflexión\nde voltaje debe ser positivo y\nmenor que uno.')
                    ad.exec()
                return False
            
            if float(self.datos[0][1]) <= 0 : #BW
                if advertir:
                    ad=adv('El ancho de banda de adaptación\ndebe ser mayor que cero.')
                    ad.exec()
                return False
            
            if float(self.datos[0][2]) <= 0 : #fo
                if advertir:
                    ad=adv('La frecuencia central de adaptación\ndebe ser mayor que cero.')
                    ad.exec()
                return False
            
            if float(self.datos[0][1])/2 >= float(self.datos[0][2]) : # bw/2 >= fo
                if advertir:
                    ad=adv('El rango de frecuencia de adapatación requerido\ndebe abarcar sólo valores positivos.')
                    ad.exec()
                return False
            
            if len(self.datos[1])==0 :
                if advertir:
                    ad=adv('Seleccione al menos un algoritmo\na implementar.')
                    ad.exec()
                return False
            
        except:
            if advertir:
                ad=adv('Ingrese correctamente los parámetros de\nrequerimientos de adaptación de impedancias.')
                ad.exec()
            return False
        
        return True
    
    def formato_correcto(self,datos): 
        if len(datos) >= 3: 
            if len(datos[0]) < 3: return False
            if len(datos[2]) < 2: return False
        else:
            return False
        
        return True
        
    def calcular_funcion_objetivo(self,F):       
        self.funcion_objetivo=[]     
        for i in range(len(F)):
            self.funcion_objetivo.append(float(self.datos[0][0])) #|gamma|max
            
    def eliminar_algoritmos_duplicados(self):
        for i in range(len(self.datos[1])):
            try: nombre=self.datos[1][i]
            except: break
                
            for j in range(len(self.datos[1])):
                if j != i:
                    try:
                        if self.datos[1][j]==nombre: del self.datos[1][j]
                    except: break
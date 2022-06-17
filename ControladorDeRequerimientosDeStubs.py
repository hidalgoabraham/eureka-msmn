# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

from PyQt5.QtGui import QIntValidator
import os.path
import csv
from PyQt5.QtWidgets import QFileDialog,QMainWindow
from Advertencia import adv       
from ventana_reqStubs_ui import Ui_MainWindow as VentanaReqStubs
from functools import partial

        
class ControladorDeRequerimientosDeStubs(QMainWindow,VentanaReqStubs):
    def __init__(self,ventana_principal):
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.setWindowTitle('Configurar MSMN')

        self.cvp=ventana_principal
        
        #Validators
        self.linedit_lmin.setValidator(QIntValidator())
        self.linedit_dmin.setValidator(QIntValidator())
        
        self.ignorar_senhales=False
        self.datos=self.plantilla_datos('Paralelo',
                                        self.cbx_cargastubs.currentText(),'','',
                                        self.cbx_Nmax.currentText(),self.spnbx_Nmax.value())
        
        #Conexiones    
        self.actionCargar.triggered.connect(self.cargar)
        self.actionGuardar.triggered.connect(self.guardar)
        self.actionReiniciar.triggered.connect(self.reiniciar)
        self.cbx_cargastubs.currentTextChanged.connect(self.accion_cbx_carga)
        self.cbx_Nmax.currentTextChanged.connect(self.accion_cbx_Nmax)
        self.spnbx_Nmax.valueChanged.connect(self.accion_spnbx_Nmax)
        self.linedit_lmin.editingFinished.connect(partial(self.editing_finished,self.linedit_lmin,0,2))
        self.linedit_dmin.editingFinished.connect(partial(self.editing_finished,self.linedit_dmin,0,3))
        
        self.linedit_lmin.textChanged.connect(partial(self.text_changed,self.linedit_lmin,0,2))
        self.linedit_dmin.textChanged.connect(partial(self.text_changed,self.linedit_dmin,0,3))
        
        self.pbtn_ok.clicked.connect(self.salir)
        
    ### Lógica de Interfaz Gráfica
        
    def plantilla_datos(self,tipodispo='Paralelo',tipocarga='Corto circuito',lmin='',dmin='',tipoNmax='Cantidad máxima de stubs:',Nmax=1): 
        # tipo disposición, tipo carga, lmin, dmin, tipo Nmax, Nmax
        return [[tipodispo,tipocarga,lmin,dmin,tipoNmax,Nmax]]
       
    def closeEvent(self, event): self.salir() 
        
    def salir(self): 
        self.hide()
        self.cvp.pbtn_configurar_reqStubs.setEnabled(True)
                        
    def cargar(self):
        try:
            carpeta='./Datos/Requerimientos de stubs'
            ruta = QFileDialog.getOpenFileName(self, 'Cargar archivo',carpeta,"*.reqstubs")[0]
            if os.path.exists(ruta):
                datos=[]
                with open(ruta) as archivo:
                    lector = csv.reader(archivo, delimiter=',', quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    for fila in lector: datos.append(fila) 
                    
                if self.formato_correcto(datos): pass
                else: raise Exception
                
                self.datos=datos
                    
                self.ignorar_senhales=True
                self.datosAventana()
                self.ignorar_senhales=False
            
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos.')
            ad.exec_()
            self.ignorar_senhales=False
            self.reiniciar()
            
    def cargar_datos(self,datos): 
        try: 
            if self.formato_correcto(datos): pass
            else: raise Exception
            
            self.datos=datos
                
            self.ignorar_senhales=True
            self.datosAventana()
            self.ignorar_senhales=False
                           
        except:
            ad=adv('Formato incompatible.\nNo se pudo cargar los datos de stubs.')
            ad.exec_()
            self.ignorar_senhales=False
            self.reiniciar()
        
    def formatear_datos(self,datos): 
        datos[0][2]=int(float(datos[0][2])) #lmin
        datos[0][3]=int(float(datos[0][3])) #dmin
        datos[0][5]=int(float(datos[0][5])) #Nmax
        return datos
        
    def guardar(self): 
        carpeta='./Datos/Requerimientos de stubs'
        ruta = QFileDialog.getSaveFileName(self,'Guardar archivo',carpeta,'*.reqstubs')[0]
        if ruta!='':
            if ruta[-9:] != '.reqstubs': ruta=ruta+'.reqstubs'
            with open(ruta,'w',newline='') as archivo:
                escritor = csv.writer(archivo)
                for fila in self.datos:
                    escritor.writerow(fila)
        
    def reiniciar(self):
        self.datos=self.plantilla_datos()
        self.cbx_dispostubs.setCurrentText('Paralelo')
        self.cbx_cargastubs.setCurrentText('Corto circuito')
        self.linedit_lmin.setText('')
        self.linedit_dmin.setText('')
        self.cbx_Nmax.setCurrentText('Cantidad máxima de stubs:')
        self.spnbx_Nmax.setValue(1)
                
    def accion_cbx_carga(self): 
        if self.ignorar_senhales: return
        self.datos[0][1]=self.cbx_cargastubs.currentText()
        
    def accion_cbx_Nmax(self): 
        if self.ignorar_senhales: return
        self.datos[0][4]=self.cbx_Nmax.currentText()
        
    def text_changed(self,linedit,fila,columna):
        if self.ignorar_senhales:
            self.datos[fila][columna]=linedit.text()
        else:
            self.ignorar_senhales=True
            self.datos[fila][columna]=linedit.text()
            self.ignorar_senhales=False
        
    def editing_finished(self,linedit,fila,columna): 
        if self.ignorar_senhales: return
        linedit.setCursorPosition(0)
        try: self.datos[fila][columna]=int(linedit.text())
        except: pass
    
    def accion_spnbx_Nmax(self): 
        if self.ignorar_senhales: return
        self.datos[0][5]=self.spnbx_Nmax.value()
    
    def datosAventana(self): 
        self.cbx_dispostubs.setCurrentText('Paralelo')
        self.cbx_cargastubs.setCurrentText(self.datos[0][1])
        self.linedit_lmin.setText(str(self.datos[0][2]))
        self.linedit_lmin.setCursorPosition(0)
        self.linedit_dmin.setText(str(self.datos[0][3]))
        self.linedit_dmin.setCursorPosition(0)
        self.cbx_Nmax.setCurrentText(self.datos[0][4])
        self.spnbx_Nmax.setValue(int(self.datos[0][5]))
        
    def bloquear(self):
        self.cvp.pbtn_configurar_reqStubs.setEnabled(False)
        self.hide()
        
    def desbloquear(self):
        self.cvp.pbtn_configurar_reqStubs.setEnabled(True)
        
    ### Lógica de Cómputo
        
    def datos_correcto(self, advertir=True): 
        try:
            if int(float(self.datos[0][2])) <= 0: #lmin
                if advertir:
                    ad=adv('La longitud mínima de los stubs\ndebe ser mayor que cero.')
                    ad.exec()
                return False
            
            if int(float(self.datos[0][3])) <= 0: #dmin
                if advertir:
                    ad=adv('La distancia mínima de los stubs\ndebe ser mayor que cero.')
                    ad.exec()
                return False
            
            if int(float(self.datos[0][5])) <= 0: #Nmax
                if advertir:
                    ad=adv('La cantidad de stubs\ndebe ser mayor que cero.')
                    ad.exec()
                return False

        except:
            if advertir:
                ad=adv('Ingrese correctamente los parámetros\nde los stubs.')
                ad.exec()
            return False
        
        return True
            
    def formato_correcto(self,datos): 
        if len(datos) == 1: 
            if len(datos[0]) != 6 : return False
            
            if datos[0][0]=='Paralelo': pass
            else: return False
            
            if datos[0][1]=='Corto circuito' or datos[0][1]=='Circuito abierto': pass
            else: return False
            
            if datos[0][4]=='Cantidad máxima de stubs:' or datos[0][4]=='Cantidad fija de stubs:': pass
            else: return False

        else: 
            return False
        
        return True
# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QGridLayout
import matplotlib.pyplot as plt
import matplotlib
from Funciones import circunferencia
from Funciones import elemento_central
from skrf.plotting import smith
import mplcursors
from PyQt5 import QtGui, QtCore
from numpy import Infinity
        
class ControladorDeGrafica:
            
    def __init__(self,ventana_secundaria):
        self.cvs=ventana_secundaria
        self.layout_grafica = QGridLayout()
        self.cvs.gpbx_grafica.figure = plt.figure()
        self.cvs.gpbx_grafica.canvas = FigureCanvas(self.cvs.gpbx_grafica.figure)
        self.cvs.gpbx_grafica.canvas.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.cvs.gpbx_grafica.setLayout(self.layout_grafica)
        self.layout_grafica.addWidget(self.cvs.gpbx_grafica.canvas)
        self.cvs.gpbx_grafica.figure.clear()
        self.cvs.gpbx_grafica.canvas.draw()
        self.graf = self.cvs.gpbx_grafica.figure.add_subplot(111)
        self.graf.clear()
        
        
        self.etiquetas=[]
        self.legend_location='upper left'
        
        if self.cvs.bandera=='buscar':
            self.xcir, self.ycir_n, self.ycir_p = circunferencia(self.cvs.cvp.Cobjetivo.datos[0][0],200)
        
        #Conexion Slider
        self.cvs.slider.sliderReleased.connect(self.actualizarporbarra)
        
    def Hz(self,F): #F en MHz
        out=[]
        for elemento in F: out.append(elemento*1e6)
        return out
    
    def Maximo_de_Lista(self,Lista):
        maximo=-1*Infinity
        for elemento in Lista:
            if elemento > maximo: maximo=elemento
            
        return maximo
        
    
    def ocultar(self): 
        self.cvs.gpbx_grafica.hide()
        
    def borrar(self):
        self.cvs.gpbx_grafica.figure.clear()
            
    def mostrar(self):
        self.cvs.gpbx_grafica.show()
        
    def graficar_linea_gamma(self):
        gmax=float(self.cvs.cvp.Cobjetivo.datos[0][0])
        GMAX=[]
        for f in self.cvs.Fvisual: GMAX.append(gmax)
        self.linea_gamma=self.graf.plot(self.Hz(self.cvs.Fvisual),GMAX,color='r')
        self.cvs.gpbx_grafica.canvas.draw()
        
    def quitar_linea_gamma(self):
        try:
            linea=self.linea_gamma.pop(0)
            linea.remove()
            self.cvs.gpbx_grafica.canvas.draw()
        except:
            pass
        
    def graficar_linea_potencia(self):
        Pmax=float(self.cvs.Clinea.datos[1][1])
        PMAX=[]
        for f in self.cvs.Fvisual: PMAX.append(Pmax)
        self.linea_potencia=self.graf.plot(self.Hz(self.cvs.Fvisual),PMAX,color='r')
        self.cvs.gpbx_grafica.canvas.draw()
        
    def quitar_linea_potencia(self):
        linea=self.linea_potencia.pop(0)
        linea.remove()
        self.cvs.gpbx_grafica.canvas.draw()
        
    
    def graficar(self,posicion=None):
        
        self.cvs.gpbx_grafica.show()
        self.cvs.gpbx_grafica.figure.clear()
        self.cvs.gpbx_grafica.canvas.draw()
        self.graf = self.cvs.gpbx_grafica.figure.add_subplot(111)
         
        if self.cvs.bandera=='buscar':        
            if self.cvs.cbx_algoritmos.currentText()=='Todos (comparación)':
        ### Todos
                etiquetas=[]
                
                for nombre in self.cvs.algoritmos_a_graficar:
                    Nstubs=self.cvs.cvp.Buscadores[nombre].datos[0][2]
                    if Nstubs>1: word=' stubs'
                    elif Nstubs==1: word=' stub'
                    etiquetas.append(nombre + ' - ' +str(Nstubs) + word)
                    
                a=self.cvs.cbx_tipografica.currentText()
                b=self.cvs.cbx_presentaciongrafica.currentText()
                palabra=a+' - '+b
                if b=='Fase': palabra = palabra +' (°)'
                if a=='Impedancia vista' and b!='Fase': palabra = palabra +' (Ω)'
                if a=='ROEV':palabra=a
                if a=='Potencia activa promedio': palabra=a+' - (W)'
                
                if a == 'Coeficiente de reflexión':
                    if b == 'Magnitud': 
                        tag_y='|Γ|'
                        unidad_y=''
                    elif b == 'Fase': 
                        tag_y='∠Γ'
                        unidad_y='°'
                    elif b == 'Parte real': 
                        tag_y='Real(Γ)'
                        unidad_y=''
                    elif b == 'Parte imaginaria': 
                        tag_y='Imag(Γ)'
                        unidad_y=''
                    
                elif a == 'Impedancia vista':
                    if b == 'Magnitud': 
                        tag_y='|Zin|'
                        unidad_y='Ω'
                    elif b == 'Fase': 
                        tag_y='∠Zin'
                        unidad_y='°'
                    elif b == 'Parte real': 
                        tag_y='Real(Zin)'
                        unidad_y='Ω'
                    elif b == 'Parte imaginaria': 
                        tag_y='Imag(Zin)'
                        unidad_y='Ω'
                    
                elif a == 'ROEV':
                    tag_y='ROEV'
                    unidad_y=''
                    
                elif a == 'Potencia activa promedio':
                    tag_y='P'
                    unidad_y='W'
                    
                elif a == 'Respuesta en frecuencia':
                    if b == 'Magnitud': 
                        tag_y='|H|'
                        unidad_y=''
                    elif b == 'Fase': 
                        tag_y='∠H'
                        unidad_y='°'
                    elif b == 'Parte real': 
                        tag_y='Real(H)'
                        unidad_y=''
                    elif b == 'Parte imaginaria': 
                        tag_y='Imag(H)'
                        unidad_y=''
                    
                
                self.graf.clear()
                self.cvs.gpbx_grafica.canvas.draw()
                self.graf.set_ylabel(palabra)
                self.graf.set_xlabel("Frecuencia (Hz)")
                self.graf.set_title(" ")
                
                self.cvs.gpbx_grafica.canvas.setCursor(QtGui.QCursor())
                labels=dict()
                for algoritmo in self.cvs.algoritmos_a_graficar: 
                    self.graf.margins(x=0)
                    ax=self.graf.plot(self.Hz(self.cvs.Fvisual),self.cvs.cvp.Buscadores[algoritmo].grafica,label=algoritmo,color=self.cvs.cvp.Buscadores[algoritmo].color)
                    #self.cvs.cvp.Buscadores[algoritmo].color = ax[-1].get_color()
                    
                    labels[algoritmo]=[]
                    for i in range(len(self.cvs.Fvisual)): labels[algoritmo].append(tag_y+'='+str(round(self.cvs.cvp.Buscadores[algoritmo].grafica[i],3))+' '+unidad_y+'\nf='+str(round(self.cvs.Fvisual[i],3))+' MHz')
                plt.tight_layout()
                self.graf.ticklabel_format(axis="both", style="sci", scilimits=(0,0), useMathText=True)
                mpl_cursors = mplcursors.cursor(self.graf,hover=2)#.connect("add", lambda sel,algoritmo: sel.annotation.set_text(labels[algoritmo][int(sel.target.index)]))
                
                @mpl_cursors.connect("add")
                def add(sel):
                    nombre=sel.artist.get_label()
                    sel.annotation.set_text(labels[nombre][int(sel.target.index)])    
                
                self.graf.legend(etiquetas, loc = self.legend_location)
                self.graf.grid()
                self.cvs.gpbx_grafica.canvas.draw()
                
                
            else:
        #### Un algoritmo
                algoritmo=self.cvs.cbx_algoritmos.currentText()
                etiquetas=[]
                
                etiquetas.append(algoritmo)
                
                a=self.cvs.cbx_tipografica.currentText()
                b=self.cvs.cbx_presentaciongrafica.currentText()
                palabra=a+' - '+b
                
                if b=='Fase': palabra=palabra +' (°)'
                if a=='Impedancia vista' and b!='Fase': palabra=palabra +' (Ω)'
                if a=='ROEV':palabra=a
                if a=='Potencia activa promedio': palabra=a+' - (W)'
               
                self.graf.clear()
                self.cvs.gpbx_grafica.canvas.draw()
                
                if a=='Carta de Smith':
                    Pmax=float(self.cvs.Clinea.datos[1][1])
                    DGA=int(float(self.cvs.Clinea.datos[3][1]))
                    DCA=int(float(self.cvs.Clinea.datos[3][0]))
                    self.cvs.cvp.Buscadores[algoritmo].crear_grafica('Coeficiente de reflexión',
                                                                     'Parte real',
                                                                     self.cvs.cvp.Cgenerador.Voltaje,
                                                                     self.cvs.cvp.Cgenerador.Impedancia,
                                                                     self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                                                     self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                                     self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                                     self.cvs.Cbarra.posicion)
                    Real=self.cvs.cvp.Buscadores[algoritmo].grafica
                    self.cvs.cvp.Buscadores[algoritmo].crear_grafica('Coeficiente de reflexión',
                                                                     'Parte imaginaria',
                                                                     self.cvs.cvp.Cgenerador.Voltaje,
                                                                     self.cvs.cvp.Cgenerador.Impedancia,
                                                                     self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                                                     self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                                     self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                                     self.cvs.Cbarra.posicion)                                        
                    Imaginaria=self.cvs.cvp.Buscadores[algoritmo].grafica                    
                    self.cvs.cvp.Buscadores[algoritmo].crear_grafica('Coeficiente de reflexión',
                                                                     'Magnitud',
                                                                     self.cvs.cvp.Cgenerador.Voltaje,
                                                                     self.cvs.cvp.Cgenerador.Impedancia,
                                                                     self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                                                     self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                                     self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                                     self.cvs.Cbarra.posicion)                    
                    Modulo=self.cvs.cvp.Buscadores[algoritmo].grafica
                    
                    r=self.Maximo_de_Lista(Modulo) 
                    if r<1 : r=1

                    ax0=self.graf.plot(elemento_central(Real),elemento_central(Imaginaria),color=self.cvs.cvp.Buscadores[algoritmo].color,marker='o')
                    self.ax1=self.graf.plot(Real,Imaginaria,color=self.cvs.cvp.Buscadores[algoritmo].color,linestyle='None',marker='.',markersize=2)
                    ax2=self.graf.plot(self.xcir, self.ycir_n,'r,-')
                    ax3=self.graf.plot(self.xcir, self.ycir_p,'r,-')
                    self.graf.set_xlabel('Parte Real')
                    self.graf.set_ylabel('Parte Imaginaria')   
                    self.graf.set_title("Coeficiente de Reflexión")  
                    smith(smithR=r,chart_type='z',draw_labels=False,border=True,ax=self.graf,ref_imm=1.0,draw_vswr=False)
                    self.cvs.gpbx_grafica.canvas.setCursor(QtGui.QCursor())
                    labels=[]
                    for i in range(len(self.cvs.Fvisual)): labels.append('Real(Γ)='+str(round(Real[i],3))+'\nImag(Γ)='+str(round(Imaginaria[i],3))+'\nf='+str(round(self.cvs.Fvisual[i],3))+' MHz')
                    self.mpl_cursor = mplcursors.cursor(self.ax1,hover=2).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.target.index)]))
                    
                    self.graf.legend(etiquetas, loc = self.legend_location)
                    self.graf.grid()
                    self.cvs.gpbx_grafica.canvas.draw()
                    return

                self.graf.set_ylabel(palabra)
                self.graf.set_xlabel("Frecuencia (Hz)")
                self.graf.set_title(" ")
                self.graf.margins(x=0)
                if a == 'Coeficiente de reflexión':
                    if b == 'Magnitud': 
                        tag_y='|Γ|'
                        unidad_y=''
                    elif b == 'Fase': 
                        tag_y='∠Γ'
                        unidad_y='°'
                    elif b == 'Parte real': 
                        tag_y='Real(Γ)'
                        unidad_y=''
                    elif b == 'Parte imaginaria': 
                        tag_y='Imag(Γ)'
                        unidad_y=''
                    
                elif a == 'Impedancia vista':
                    if b == 'Magnitud': 
                        tag_y='|Zin|'
                        unidad_y='Ω'
                    elif b == 'Fase': 
                        tag_y='∠Zin'
                        unidad_y='°'
                    elif b == 'Parte real': 
                        tag_y='Real(Zin)'
                        unidad_y='Ω'
                    elif b == 'Parte imaginaria': 
                        tag_y='Imag(Zin)'
                        unidad_y='Ω'
                    
                elif a == 'ROEV':
                    tag_y='ROEV'
                    unidad_y=''
                    
                elif a == 'Potencia activa promedio':
                    tag_y='P'
                    unidad_y='W'
                    
                elif a == 'Respuesta en frecuencia':
                    if b == 'Magnitud': 
                        tag_y='|H|'
                        unidad_y=''
                    elif b == 'Fase': 
                        tag_y='∠H'
                        unidad_y='°'
                    elif b == 'Parte real': 
                        tag_y='Real(H)'
                        unidad_y=''
                    elif b == 'Parte imaginaria': 
                        tag_y='Imag(H)'
                        unidad_y=''
                
                self.graf.plot(self.Hz(self.cvs.Fvisual),self.cvs.cvp.Buscadores[algoritmo].grafica,self.cvs.cvp.Buscadores[algoritmo].color)
                plt.tight_layout()
                self.graf.ticklabel_format(axis="both", style="sci", scilimits=(0,0), useMathText=True)
                self.cvs.gpbx_grafica.canvas.setCursor(QtGui.QCursor())
                labels=[]
                for i in range(len(self.cvs.Fvisual)): labels.append(tag_y+'='+str(round(self.cvs.cvp.Buscadores[algoritmo].grafica[i],3))+' '+unidad_y+'\nf='+str(round(self.cvs.Fvisual[i],3))+' MHz')
                self.mpl_cursor = mplcursors.cursor(self.cvs.gpbx_grafica.canvas.figure.axes,hover=2).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.target.index)]))
                self.graf.legend(etiquetas, loc = self.legend_location)
                self.graf.grid()
                self.cvs.gpbx_grafica.canvas.draw()
                
            if self.cvs.cbx_tipografica.currentText()=='Coeficiente de reflexión' and self.cvs.cbx_presentaciongrafica.currentText()=='Magnitud': self.graficar_linea_gamma()
            else: self.quitar_linea_gamma()
                
        else:
        ### Graficar
            
            a=self.cvs.cbx_tipografica.currentText()
            b=self.cvs.cbx_presentaciongrafica.currentText()
            palabra=a+' - '+b
            
            if b=='Fase': palabra=palabra +' (°)'
            if a=='Impedancia vista' and b!='Fase': palabra=palabra +' (Ω)'
            if a=='ROEV':palabra=a
            if a=='Potencia activa promedio': palabra=a+' - (W)'
           
            self.graf.clear()
            self.cvs.gpbx_grafica.canvas.draw()
            
            if a=='Carta de Smith':
                
                Pmax=float(self.cvs.Clinea.datos[1][1])
                DGA=int(float(self.cvs.Clinea.datos[3][1]))
                DCA=int(float(self.cvs.Clinea.datos[3][0]))
                self.cvs.crear_grafica('Coeficiente de reflexión',
                                       'Parte real',
                                       self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                       self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                       self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                       self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                       self.cvs.Cbarra.posicion)
                Real=self.cvs.grafica
                self.cvs.crear_grafica('Coeficiente de reflexión',
                                       'Parte imaginaria',
                                       self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                       self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                       self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                       self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                       self.cvs.Cbarra.posicion)
                Imaginaria=self.cvs.grafica 
                self.cvs.crear_grafica('Coeficiente de reflexión',
                                       'Magnitud',
                                       self.cvs.cvp.Cgenerador.Voltaje,
                                       self.cvs.cvp.Cgenerador.Impedancia,
                                       self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                       self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                       self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                       self.cvs.Cbarra.posicion)
                Modulo=self.cvs.grafica
                    
                r=self.Maximo_de_Lista(Modulo)
                if r<1 : r=1
                
                ax0=self.graf.plot(elemento_central(Real),elemento_central(Imaginaria),color=self.cvs.color,marker='o')
                self.ax1=self.graf.plot(Real,Imaginaria,linestyle='None',marker='.',color=self.cvs.color,markersize=2)
                self.graf.set_xlabel('Parte Real')
                self.graf.set_ylabel('Parte Imaginaria')   
                self.graf.set_title("Coeficiente de Reflexión")                       
                smith(smithR=r,chart_type='z',draw_labels=False,border=True,ax=self.graf,ref_imm=1.0,draw_vswr=False)
                self.cvs.gpbx_grafica.canvas.setCursor(QtGui.QCursor())
                labels=[]
                for i in range(len(self.cvs.Fvisual)): labels.append('Real(Γ)='+str(round(Real[i],3))+'\nImag(Γ)='+str(round(Imaginaria[i],3))+'\nf='+str(round(self.cvs.Fvisual[i],3))+' MHz')
                self.mpl_cursor = mplcursors.cursor(self.ax1,hover=2).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.target.index)]))
                
                self.graf.grid()
                self.cvs.gpbx_grafica.canvas.draw()
                return

            self.graf.set_ylabel(palabra)
            self.graf.set_xlabel("Frecuencia (Hz)")
            self.graf.set_title(" ")
            self.graf.margins(x=0)
            if a == 'Coeficiente de reflexión':
                if b == 'Magnitud': 
                    tag_y='|Γ|'
                    unidad_y=''
                elif b == 'Fase': 
                    tag_y='∠Γ'
                    unidad_y='°'
                elif b == 'Parte real': 
                    tag_y='Real(Γ)'
                    unidad_y=''
                elif b == 'Parte imaginaria': 
                    tag_y='Imag(Γ)'
                    unidad_y=''
                
            elif a == 'Impedancia vista':
                if b == 'Magnitud': 
                    tag_y='|Zin|'
                    unidad_y='Ω'
                elif b == 'Fase': 
                    tag_y='∠Zin'
                    unidad_y='°'
                elif b == 'Parte real': 
                    tag_y='Real(Zin)'
                    unidad_y='Ω'
                elif b == 'Parte imaginaria': 
                    tag_y='Imag(Zin)'
                    unidad_y='Ω'
                
            elif a == 'ROEV':
                tag_y='ROEV'
                unidad_y=''
                
            elif a == 'Potencia activa promedio':
                    tag_y='P'
                    unidad_y='W'
                    
            elif a == 'Respuesta en frecuencia':
                if b == 'Magnitud': 
                    tag_y='|H|'
                    unidad_y=''
                elif b == 'Fase': 
                    tag_y='∠H'
                    unidad_y='°'
                elif b == 'Parte real': 
                    tag_y='Real(H)'
                    unidad_y=''
                elif b == 'Parte imaginaria': 
                    tag_y='Imag(H)'
                    unidad_y=''
                 
            ax=self.graf.plot(self.Hz(self.cvs.Fvisual),self.cvs.grafica,self.cvs.color)
            plt.tight_layout()
            self.graf.ticklabel_format(axis="both", style="sci", scilimits=(0,0), useMathText=True)
            self.cvs.gpbx_grafica.canvas.setCursor(QtGui.QCursor())
            labels=[]
            for i in range(len(self.cvs.Fvisual)): labels.append(tag_y+'='+str(round(self.cvs.grafica[i],3))+' '+unidad_y+'\nf='+str(round(self.cvs.Fvisual[i],3))+' MHz')
            self.mpl_cursor = mplcursors.cursor(self.cvs.gpbx_grafica.canvas.figure.axes,hover=2).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.target.index)]))
            self.graf.grid()
            self.cvs.gpbx_grafica.canvas.draw()
            
            
        if self.cvs.cbx_tipografica.currentText()=='Potencia activa promedio' and self.cvs.chkbx_Pmax.isChecked(): self.graficar_linea_potencia()
            
    def actualizarporbarra(self):
        if self.cvs.Cbarra.configurando : return
        
        if self.cvs.bandera=='buscar':
        ### Un algoritmo
            algoritmo=self.cvs.cbx_algoritmos.currentText()
            self.cvs.cvp.Buscadores[algoritmo].posicion=self.cvs.Cbarra.posicion
            etiquetas=[]
            
            etiquetas.append(algoritmo)
                        
            a=self.cvs.cbx_tipografica.currentText()
            b=self.cvs.cbx_presentaciongrafica.currentText()
            
            palabra=a+' - '+b
            if b=='Fase': palabra=palabra +' (°)'
            if a=='Impedancia vista' and b!='Fase': palabra=palabra +' (Ω)'
            if a=='ROEV':palabra=a
            if a=='Potencia activa promedio': palabra=a+' - (W)'
            
            self.graf.clear()
            self.cvs.gpbx_grafica.canvas.draw()
            
            if a=='Carta de Smith':
                Pmax=float(self.cvs.Clinea.datos[1][1])
                DGA=int(float(self.cvs.Clinea.datos[3][1]))
                DCA=int(float(self.cvs.Clinea.datos[3][0]))
                self.cvs.cvp.Buscadores[algoritmo].crear_grafica('Coeficiente de reflexión',
                                                                 'Parte real',
                                                                 self.cvs.cvp.Cgenerador.Voltaje,
                                                                 self.cvs.cvp.Cgenerador.Impedancia,
                                                                 self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                                                 self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                                 self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                                 self.cvs.Cbarra.posicion)
                Real=self.cvs.cvp.Buscadores[algoritmo].grafica
                self.cvs.cvp.Buscadores[algoritmo].crear_grafica('Coeficiente de reflexión',
                                                                 'Parte imaginaria',
                                                                 self.cvs.cvp.Cgenerador.Voltaje,
                                                                 self.cvs.cvp.Cgenerador.Impedancia,
                                                                 self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                                                 self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                                 self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                                 self.cvs.Cbarra.posicion)
                Imaginaria=self.cvs.cvp.Buscadores[algoritmo].grafica                
                self.cvs.cvp.Buscadores[algoritmo].crear_grafica('Coeficiente de reflexión',
                                                                 'Magnitud',
                                                                 self.cvs.cvp.Cgenerador.Voltaje,
                                                                 self.cvs.cvp.Cgenerador.Impedancia,
                                                                 self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                                                 self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                                 self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                                 self.cvs.Cbarra.posicion)                    
                Modulo=self.cvs.cvp.Buscadores[algoritmo].grafica
                    
                r=self.Maximo_de_Lista(Modulo)
                if r<1 : r=1
                
                ax0=self.graf.plot(elemento_central(Real),elemento_central(Imaginaria),color=self.cvs.cvp.Buscadores[algoritmo].color,marker='o')
                self.ax1=self.graf.plot(Real,Imaginaria,self.cvs.cvp.Buscadores[algoritmo].color,linestyle='None',marker='.',markersize=2)
                ax2=self.graf.plot(self.xcir, self.ycir_n,'r,-')
                ax3=self.graf.plot(self.xcir, self.ycir_p,'r,-')  
                self.graf.set_xlabel('Parte Real')
                self.graf.set_ylabel('Parte Imaginaria')   
                self.graf.set_title("Coeficiente de Reflexión")                       
                smith(smithR=r,chart_type='z',draw_labels=False,border=True,ax=self.graf,ref_imm=1.0,draw_vswr=False)
                self.cvs.gpbx_grafica.canvas.setCursor(QtGui.QCursor())
                labels=[]
                for i in range(len(self.cvs.Fvisual)): labels.append('Real(Γ)='+str(round(Real[i],3))+'\nImag(Γ)='+str(round(Imaginaria[i],3))+'\nf='+str(round(self.cvs.Fvisual[i],3))+' MHz')
                self.mpl_cursor = mplcursors.cursor(self.ax1,hover=2).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.target.index)]))
                
                self.graf.legend(etiquetas, loc = self.legend_location)
                self.graf.grid()
                self.cvs.gpbx_grafica.canvas.draw()
                return
            
            Pmax=float(self.cvs.Clinea.datos[1][1])
            DGA=int(float(self.cvs.Clinea.datos[3][1]))
            DCA=int(float(self.cvs.Clinea.datos[3][0]))
            self.cvs.cvp.Buscadores[algoritmo].crear_grafica(self.cvs.cbx_tipografica.currentText(),
                                                             self.cvs.cbx_presentaciongrafica.currentText(),
                                                             self.cvs.cvp.Cgenerador.Voltaje,
                                                             self.cvs.cvp.Cgenerador.Impedancia,
                                                             self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                                             self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                                             self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                                             self.cvs.Cbarra.posicion)
            
            #Crear Nueva Grafica
            self.graf.set_ylabel(palabra)
            self.graf.set_xlabel("Frecuencia (Hz)")
            self.graf.set_title(" ")
            self.graf.margins(x=0)
            if a == 'Coeficiente de reflexión':
                if b == 'Magnitud': 
                    tag_y='|Γ|'
                    unidad_y=''
                elif b == 'Fase': 
                    tag_y='∠Γ'
                    unidad_y='°'
                elif b == 'Parte real': 
                    tag_y='Real(Γ)'
                    unidad_y=''
                elif b == 'Parte imaginaria': 
                    tag_y='Imag(Γ)'
                    unidad_y=''
                
            elif a == 'Impedancia vista':
                if b == 'Magnitud': 
                    tag_y='|Zin|'
                    unidad_y='Ω'
                elif b == 'Fase': 
                    tag_y='∠Zin'
                    unidad_y='°'
                elif b == 'Parte real': 
                    tag_y='Real(Zin)'
                    unidad_y='Ω'
                elif b == 'Parte imaginaria': 
                    tag_y='Imag(Zin)'
                    unidad_y='Ω'
                
            elif a == 'ROEV':
                tag_y='ROEV'
                unidad_y=''
                
            elif a == 'Potencia activa promedio':
                    tag_y='P'
                    unidad_y='W'
                    
            elif a == 'Respuesta en frecuencia':
                if b == 'Magnitud': 
                    tag_y='|H|'
                    unidad_y=''
                elif b == 'Fase': 
                    tag_y='∠H'
                    unidad_y='°'
                elif b == 'Parte real': 
                    tag_y='Real(H)'
                    unidad_y=''
                elif b == 'Parte imaginaria': 
                    tag_y='Imag(H)'
                    unidad_y=''
            
            self.graf.plot(self.Hz(self.cvs.Fvisual),self.cvs.cvp.Buscadores[algoritmo].grafica,self.cvs.cvp.Buscadores[algoritmo].color)
            plt.tight_layout()
            self.graf.ticklabel_format(axis="both", style="sci", scilimits=(0,0), useMathText=True)
            self.cvs.gpbx_grafica.canvas.setCursor(QtGui.QCursor())
            labels=[]
            for i in range(len(self.cvs.Fvisual)): labels.append(tag_y+'='+str(round(self.cvs.cvp.Buscadores[algoritmo].grafica[i],3))+' '+unidad_y+'\nf='+str(round(self.cvs.Fvisual[i],3))+' MHz')
            self.mpl_cursor = mplcursors.cursor(self.cvs.gpbx_grafica.canvas.figure.axes,hover=2).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.target.index)]))
            self.graf.legend(etiquetas, loc = self.legend_location)
            self.graf.grid()
            self.cvs.gpbx_grafica.canvas.draw()
            
            if self.cvs.cbx_tipografica.currentText()=='Coeficiente de reflexión' and self.cvs.cbx_presentaciongrafica.currentText()=='Magnitud': self.graficar_linea_gamma()
            else: self.quitar_linea_gamma()
        
        else:
        ### Graficar
            self.cvs.posicion=self.cvs.Cbarra.posicion
            a=self.cvs.cbx_tipografica.currentText()
            b=self.cvs.cbx_presentaciongrafica.currentText()
            palabra=a+' - '+b
            
            if b=='Fase': palabra=palabra +' (°)'
            if a=='Impedancia vista' and b!='Fase': palabra=palabra +' (Ω)'
            if a=='ROEV':palabra=a
            if a=='Potencia activa promedio': palabra=a+' - (W)'
           
            self.graf.clear()
            self.cvs.gpbx_grafica.canvas.draw()
            
            if a=='Carta de Smith':
                Pmax=float(self.cvs.Clinea.datos[1][1])
                DGA=int(float(self.cvs.Clinea.datos[3][1]))
                DCA=int(float(self.cvs.Clinea.datos[3][0]))
                self.cvs.crear_grafica('Coeficiente de reflexión',
                                       'Parte real',
                                       self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                       self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                       self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                       self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                       self.cvs.Cbarra.posicion)
                Real=self.cvs.grafica
                self.cvs.crear_grafica('Coeficiente de reflexión',
                                       'Parte imaginaria',
                                       self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                       self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                       self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                       self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                       self.cvs.Cbarra.posicion)
                Imaginaria=self.cvs.grafica                 
                self.cvs.crear_grafica('Coeficiente de reflexión',
                                       'Magnitud',
                                       self.cvs.cvp.Cgenerador.Voltaje,
                                       self.cvs.cvp.Cgenerador.Impedancia,
                                       self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                       self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                       self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                       self.cvs.Cbarra.posicion)                
                Modulo=self.cvs.grafica
                
                r=self.Maximo_de_Lista(Modulo)
                if r<1 : r=1
    
                ax0=self.graf.plot(elemento_central(Real),elemento_central(Imaginaria),color=self.cvs.color,marker='o')
                self.ax1=self.graf.plot(Real,Imaginaria,linestyle='None',marker='.',color=self.cvs.color,markersize=2)
                self.graf.set_xlabel('Parte Real')
                self.graf.set_ylabel('Parte Imaginaria')   
                self.graf.set_title("Coeficiente de Reflexión")                       
                smith(smithR=r,chart_type='z',draw_labels=False,border=True,ax=self.graf,ref_imm=1.0,draw_vswr=False)
                self.cvs.gpbx_grafica.canvas.setCursor(QtGui.QCursor())
                labels=[]
                for i in range(len(self.cvs.Fvisual)): labels.append('Real(Γ)='+str(round(Real[i],3))+'\nImag(Γ)='+str(round(Imaginaria[i],3))+'\nf='+str(round(self.cvs.Fvisual[i],3))+' MHz')
                self.mpl_cursor = mplcursors.cursor(self.ax1,hover=2).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.target.index)]))
                
                self.graf.grid()
                self.cvs.gpbx_grafica.canvas.draw()
                return
            
            
            Pmax=float(self.cvs.Clinea.datos[1][1])
            DGA=int(float(self.cvs.Clinea.datos[3][1]))
            DCA=int(float(self.cvs.Clinea.datos[3][0]))
            
            self.cvs.crear_grafica(self.cvs.cbx_tipografica.currentText(),
                                   self.cvs.cbx_presentaciongrafica.currentText(),
                                   self.cvs.cvp.Cgenerador.Voltaje,self.cvs.cvp.Cgenerador.Impedancia,
                                   self.cvs.Clinea.Alfa,self.cvs.Clinea.Beta,self.cvs.Clinea.Zc,
                                   self.cvs.Clinea.rlgc_vs_f,Pmax,DCA,DGA,
                                   self.cvs.cvp.Ccarga.Z,self.cvs.Fvisual,
                                   self.cvs.Cbarra.posicion)

            self.graf.set_ylabel(palabra)
            self.graf.set_xlabel("Frecuencia (Hz)")
            self.graf.set_title(" ")
            self.graf.margins(x=0)
            if a == 'Coeficiente de reflexión':
                if b == 'Magnitud': 
                    tag_y='|Γ|'
                    unidad_y=''
                elif b == 'Fase': 
                    tag_y='∠Γ'
                    unidad_y='°'
                elif b == 'Parte real': 
                    tag_y='Real(Γ)'
                    unidad_y=''
                elif b == 'Parte imaginaria': 
                    tag_y='Imag(Γ)'
                    unidad_y=''
                
            elif a == 'Impedancia vista':
                if b == 'Magnitud': 
                    tag_y='|Zin|'
                    unidad_y='Ω'
                elif b == 'Fase': 
                    tag_y='∠Zin'
                    unidad_y='°'
                elif b == 'Parte real': 
                    tag_y='Real(Zin)'
                    unidad_y='Ω'
                elif b == 'Parte imaginaria': 
                    tag_y='Imag(Zin)'
                    unidad_y='Ω'
                
            elif a == 'ROEV':
                tag_y='ROEV'
                unidad_y=''
                
            elif a == 'Potencia activa promedio':
                    tag_y='P'
                    unidad_y='W'
                    
            elif a == 'Respuesta en frecuencia':
                if b == 'Magnitud': 
                    tag_y='|H|'
                    unidad_y=''
                elif b == 'Fase': 
                    tag_y='∠H'
                    unidad_y='°'
                elif b == 'Parte real': 
                    tag_y='Real(H)'
                    unidad_y=''
                elif b == 'Parte imaginaria': 
                    tag_y='Imag(H)'
                    unidad_y=''
            
            self.graf.plot(self.Hz(self.cvs.Fvisual),self.cvs.grafica,self.cvs.color)
            plt.tight_layout()
            self.graf.ticklabel_format(axis="both", style="sci", scilimits=(0,0), useMathText=True)
            self.cvs.gpbx_grafica.canvas.setCursor(QtGui.QCursor())
            labels=[]
            for i in range(len(self.cvs.Fvisual)): labels.append(tag_y+'='+str(round(self.cvs.grafica[i],3))+' '+unidad_y+'\nf='+str(round(self.cvs.Fvisual[i],3))+' MHz')
            self.mpl_cursor = mplcursors.cursor(self.cvs.gpbx_grafica.canvas.figure.axes,hover=2).connect("add", lambda sel: sel.annotation.set_text(labels[int(sel.target.index)]))
            self.graf.grid()
            self.cvs.gpbx_grafica.canvas.draw()  
            
            
        if self.cvs.cbx_tipografica.currentText()=='Potencia activa promedio' and self.cvs.chkbx_Pmax.isChecked(): self.graficar_linea_potencia()
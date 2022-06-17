# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""

from cmath import tanh as complextanh
from math import sqrt


class ControladorDeFuncionAminimizar: 
    def __init__(self,ventana_principal,Buscador):
        
        #Inicializar
        self.cvp=ventana_principal
        self.Buscador=Buscador
        self.PIRA=1010 
        self.PrimerStub=True


    def Cumple(self,A,Min,Max):
        if (A>=Min)and(A<=Max):return True
        else: return False
                       
    def EnteroPar(self,n):
        N=int(n)
        if ((N/2)-int(N/2))==0.0: return True
        else: return False

    def XoCumple(self,Xo):
        lmin=self.Buscador.lmin
        lmax=self.Buscador.lmax
        dmin=self.Buscador.dmin
        dmax=self.Buscador.dmax
        
        if self.EnteroPar(self.Buscador.dim):
            for n in range(0,int(self.Buscador.dim/2)):
                if self.Cumple(Xo[2*n],dmin,dmax) and self.Cumple(Xo[2*n+1],lmin,lmax): pass
                else: return False
            
        else: #Impar
            if self.Buscador.dim==1:
                if self.Cumple(Xo[0],lmin,lmax): pass
                else: return False
            elif self.Buscador.dim>1:
                if self.Cumple(Xo[0],lmin,lmax): pass
                else: return False
                for n in range(1,int((self.Buscador.dim-1)/2)+1):
                    if self.Cumple(Xo[2*n-1],dmin,dmax) and self.Cumple(Xo[2*n],lmin,lmax): pass
                    else: return False
        
        return True
    
    def X_redondeado(self,X):
        copia=[]
        for elemento in X: 
            copia.append(round(elemento))
        return copia
    
    def FAM(self,X):
        
        #X=self.X_redondeado(x) # Esto es opcional. Cuidado, puede afectar el rendimiento de los algoritmos, porque cambia la FAM

        if self.XoCumple(X)==False:
            self.PIRA=1010
            self.Buscador.mediciones_cpu.append(self.Buscador.process.cpu_percent(interval=None))
            return self.PIRA
        elif self.XoCumple(X)==True: 
            Xo=[]
            for j in range(0,len(X)): Xo.append(float(X[j]))
            
            #21 puntos de muestra en frecuencia
            muestras=int(((self.cvp.puntos-1)/10)+1) #10%
            if muestras>1: self.stepF=int((len(self.cvp.F)-1)/(muestras-1))
            else: self.stepF=1
            
            acum=0
            indf=0
            actualZin=[]
            
            DGA=int(float(self.cvp.Clinea.datos[3][1]))
            if DGA==0: Zback=self.cvp.Cgenerador.Impedancia
            else: Zback=self.cvp.Clinea.Zc
            
            while indf < len(self.cvp.F):

                zin=self.Zin(indf,Xo)
                zback=Zback[indf]
                
                modulo=abs((zin-zback)/(zin+zback))
                maximo=self.cvp.Cobjetivo.funcion_objetivo[indf]
                if modulo>maximo: acum+=(modulo-maximo)**2
                actualZin.append(zin)
                indf+=self.stepF
                
            self.PIRA=100*sqrt(acum/muestras)
            
            if (self.PIRA < self.Buscador.PIRAmejor): self.PastZin=actualZin
            
            self.Buscador.mediciones_cpu.append(self.Buscador.process.cpu_percent(interval=None))
            return self.PIRA
        
    def Zin(self,i,Xo):
        j=complex(0+1j)
        Zc=self.cvp.Clinea.Zc[i]
        Alfa=self.cvp.Clinea.Alfa[i]
        Beta=self.cvp.Clinea.Beta[i]
                
        if self.cvp.CreqStubs.datos[0][4]=='Cantidad fija de stubs:':
            zcarga=self.cvp.Ccarga.Zprima[i]
            for n in range(1,self.cvp.CreqStubs.datos[0][5]+1):
                dn=Xo[(n-1)*2]*10**(-3) #Ahora está en m
                ln=Xo[(n-1)*2+1]*10**(-3) #Ahora está en m                            
                # Z vista sin stub
                zvss=Zc*((zcarga+Zc*complextanh((Alfa+j*Beta)*dn))/(Zc+zcarga*complextanh((Alfa+j*Beta)*dn)))
                if self.cvp.CreqStubs.datos[0][1]=='Corto circuito': zins=Zc*complextanh((Alfa+j*Beta)*ln) #Impedancia de entrada al stub
                elif self.cvp.CreqStubs.datos[0][1]=='Circuito abierto': zins=Zc/complextanh((Alfa+j*Beta)*ln) #Impedancia de entrada al stub                     
                if self.cvp.CreqStubs.datos[0][0]=='Serie': zcarga= (zvss + zins)
                elif self.cvp.CreqStubs.datos[0][0]=='Paralelo': zcarga= 1/((1/zvss)+(1/zins))
         
        elif self.cvp.CreqStubs.datos[0][4]=='Cantidad máxima de stubs:':
            if self.PrimerStub: zcarga=self.cvp.Ccarga.Zprima[i]
            else: zcarga=self.PastZin[int(i/self.stepF)]
            dn=Xo[0]*10**(-3) #Ahora está en m
            ln=Xo[1]*10**(-3) #Ahora está en m                            
            # Z vista sin stub
            zvss=Zc*((zcarga+Zc*complextanh((Alfa+j*Beta)*dn))/(Zc+zcarga*complextanh((Alfa+j*Beta)*dn)))
            if self.cvp.CreqStubs.datos[0][1]=='Corto circuito': zins=Zc*complextanh((Alfa+j*Beta)*ln) #Impedancia de entrada al stub
            elif self.cvp.CreqStubs.datos[0][1]=='Circuito abierto': zins=Zc/complextanh((Alfa+j*Beta)*ln) #Impedancia de entrada al stub                     
            if self.cvp.CreqStubs.datos[0][0]=='Serie': zcarga= (zvss + zins)
            elif self.cvp.CreqStubs.datos[0][0]=='Paralelo': zcarga= 1/((1/zvss)+(1/zins))
            
        return zcarga        
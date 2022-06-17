# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""
from Funciones import Zvista,SWR,Gamma,MatrixModulo,MatrixFase,MatrixReal,MatrixImag

class Coleccion:
    def __init__(self,VoltajeGenerador=False,ImpedanciaGenerador=False,
                 Alfa=None,Beta=None,Zc=None,Pmax=None,
                 datosStubs=None,Zins=None,
                 ZL=None,F=None,D=None):
        
        if(datosStubs is None):
            self.Zin=[[]]
            self.DIC=dict()
            self.R=[[]]
            return
        
        self.Zin,self.Zvss=Zvista(datosStubs,Zins,Alfa,Beta,Zc,ZL,F,D)
        self.DIC=dict()
        self.R=Gamma(self.Zin,Zc)
        
        self.DIC['ROEV']=SWR(self.R)
        self.DIC['Coeficiente de reflexión - Magnitud']=MatrixModulo(self.R)
        self.DIC['Coeficiente de reflexión - Fase (°)']=MatrixFase(self.R)
        self.DIC['Coeficiente de reflexión - Parte real']=MatrixReal(self.R)
        self.DIC['Coeficiente de reflexión - Parte imaginaria']=MatrixImag(self.R)
        self.DIC['Impedancia vista - Magnitud (Ohm)']=MatrixModulo(self.Zin)
        self.DIC['Impedancia vista - Fase (°)']=MatrixFase(self.Zin)
        self.DIC['Impedancia vista - Parte real (Ohm)']=MatrixReal(self.Zin)
        self.DIC['Impedancia vista - Parte imaginaria (Ohm)']=MatrixImag(self.Zin) 
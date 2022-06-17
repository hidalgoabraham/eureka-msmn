# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""
from memory_profiler import  memory_usage
from psutil import Process

from time import time
from numpy import Infinity
from PyQt5.QtCore import QObject,pyqtSignal
from ControladorDeFuncionAminimizar import ControladorDeFuncionAminimizar
from Funciones import funcion_vista_d

from Funciones import perdida_Zo_fo, max_perdida_Zo, perdida_conj_fo, max_perdida_conj
from Funciones import distorsion_fase, rizado, gamma_fo ,max_gamma, adaptacion_gamma

import threading 
import ctypes
import traceback

#Global
Imprimir=False # Imprimir por consola los resultados de las búsquedas

""""
En este contexto, PIRA significa Porcentaje de Incumplimiento del Requerimiento de Adaptacion. Expresa (en porcentaje) qué
tan excedida está la respuesta respecto a lo exigido en el apartado de requerimientos de adaptación de impedancias.
Una PIRA=0% quiere decir que se cumplió completamente con el requerimiento de adaptación, es decir, |gamma| está por
debajo del máximo establecido, en todo el ancho de banda establecido.
"""

tolerancia=4 # En unidades de Porcentaje de Incumplimiento de los Requerimientos de Adaptación, tolerancia=0 es detenerse si no mejora
# En Nmax, si PIRA empeora pero dentro de la tolerancia, se aumenta N y se continúa buscando
# Si PIRA < (PIRAmejor + tolerancia) : Seguir buscando
# Si PIRA >= (PIRAmejor + tolerancia): Dejar de buscar


def NuevoAlgoritmo(Buscador):
    if Buscador.nombre=='Nelder-Mead': return NelderMead(Buscador)
    if Buscador.nombre=='Differential Evolution': return DifferentialEvolution(Buscador)
    if Buscador.nombre=='Dual Annealing': return DualAnnealing(Buscador)
    if Buscador.nombre=='Brute Force': return BruteForce(Buscador)
    if Buscador.nombre=='Whale Optimization Algorithm': return WhaleOptimizationAlgorithm(Buscador)
    if Buscador.nombre=='Equilibrium Optimizer': return EquilibriumOptimizer(Buscador)
    if Buscador.nombre=='Harris Hawks Optimization': return HarrisHawksOptimization(Buscador)
    if Buscador.nombre=='Virus Colony Search': return VirusColonySearch(Buscador)
    if Buscador.nombre=='Artificial Ecosystem-Based Optimization': return ArtificialEcosystemBasedOptimization(Buscador)

################################################################################## Agregar acá los Algoritmos que se necesiten

                
class Buscador(QObject,threading.Thread):
    BuscadorIniciado=pyqtSignal()
    BuscadorFinalizado=pyqtSignal()
    
    def __init__(self,nombre,ventana_principal):
        threading.Thread.__init__(self)
        QObject.__init__(self)
        
        self.name='Buscador ' + nombre # Thread.name
        self.nombre=nombre
        self.cvp=ventana_principal
        self.Nstubs=0
        self.color=None
        self.ControladorDeFuncionAminimizar=ControladorDeFuncionAminimizar(ventana_principal,self)
        self.Algoritmo=NuevoAlgoritmo(self)
        self.Inicio=False # para controlar que ejecutarFijo o ejecutarMax no se inicien más de una vez por Buscador
        
        self.Xopt=[]
        self.PIRAmin=self.cvp.PIRAmin
        self.datos=[]
        self.vectorD=None
        self.coleccion_original=None
        self.coleccion=None
        self.Zins=dict()
        self.Zins_original=dict()
        
        self.grafica=None
        self.posicion=0
        self.posicion_entrada_adaptador=0
        
        self.FigurasDeMerito=dict()
        self.FigurasDeMerito['nombre']=self.nombre
        
        self.FigurasDeMerito['cpu']=0.0
        self.FigurasDeMerito['ram']=0.0
        self.FigurasDeMerito['tiempo']=0.0
        
        self.FigurasDeMerito['stubs']=0
        self.FigurasDeMerito['longitud']=0.0
        self.FigurasDeMerito['perdida_Zo_fo']=0.0
        self.FigurasDeMerito['max_perdida_Zo'], self.FigurasDeMerito['f_max_perdida_Zo']=0.0, 0.0
        self.FigurasDeMerito['perdida_conj_fo']=0.0
        self.FigurasDeMerito['max_perdida_conj'], self.FigurasDeMerito['f_max_perdida_conj']=0.0, 0.0
        self.FigurasDeMerito['distorsion_fase']=0.0
        self.FigurasDeMerito['rizado']=0.0
        self.FigurasDeMerito['gamma_fo']=0.0
        self.FigurasDeMerito['max_gamma'], self.FigurasDeMerito['f_max_gamma']=0.0, 0.0
        self.FigurasDeMerito['adaptacion_gamma']=0.0
        
        self.cvg=None
        self.cancelado=False
        self.Fallido=False
        self.cumple_requerimiento=False
        
        self.process=Process()
        self.mediciones_cpu=[]
        
        self.lmin=self.cvp.CreqStubs.datos[0][2]
        self.dmin=self.cvp.CreqStubs.datos[0][3]
        fi=float(self.cvp.Cobjetivo.datos[-1][0]) # Se asume que las frecuencias vienen en MHz
        lambda_mayor=(3e8/(fi*1e6))*1e3 # está en mm

        self.lmax=self.lmin+lambda_mayor/2 # probar con lmax=lmin+lambda_mayor
        self.dmax=self.dmin+lambda_mayor/2 # probar con dmax=dmin+lambda_mayor
        
    def EnteroPar(self,n):
        N=int(n)
        if ((N/2)-int(N/2))==0.0: return True
        else: return False
        
    def XoBounds(self,dim):
        if dim==1:
            bounds=((self.lmin,self.lmax),)
        elif dim==2:
            bounds=((self.dmin,self.dmax),(self.lmin,self.lmax))
        elif (not self.EnteroPar(dim)) and (dim>1):
            bounds=((self.lmin,self.lmax),)
            for i in range(1,int((dim-1)/2)+1):
                bounds=bounds+((self.dmin,self.dmax),(self.lmin,self.lmax),)
        elif (self.EnteroPar(dim)) and (dim>2):
            bounds=((self.dmin,self.dmax),(self.lmin,self.lmax))
            bounds=bounds*int(dim/2)
                
        return bounds
    
    def XoSeed(self,dim):
        if dim==1:
            respuesta=[self.lmin]
        elif dim==2:
            respuesta=[self.dmin,self.lmin]
        elif (not self.EnteroPar(dim)) and (dim>1):
            respuesta=[self.lmin]
            for i in range(1,int((dim-1)/2)+1):
                respuesta.append(self.dmin)
                respuesta.append(self.lmin)
        elif (self.EnteroPar(dim)) and (dim>2):
            respuesta=[]
            for i in range(1,int(dim/2)+1):
                respuesta.append(self.dmin)
                respuesta.append(self.lmin)
                
        return respuesta
    
    def ejecutarFijo(self):
        if self.Inicio: return
        else: self.Inicio=True
        
        
        
        global Imprimir
        self.BuscadorIniciado.emit()
        inicio=time()
        self.Nstubs=self.cvp.CreqStubs.datos[0][5]
        self.Xopt=[]
        self.ControladorDeFuncionAminimizar.PIRA=1010
        self.PIRAmejor=1010
        
        self.dim=int(2*self.Nstubs)
        
        
        try:
            
            self.Algoritmo.ejecutarFijo()
            
        except:
            #traceback.print_exc()
            self.Fallido=True
            if Imprimir: print('Error en ejecución del algoritmo '+self.nombre)
            final=time()
            self.FigurasDeMerito['tiempo']=final-inicio
            self.BuscadorFinalizado.emit()
            return
            
        final=time()
        self.FigurasDeMerito['tiempo']=final-inicio
        
        if self.ControladorDeFuncionAminimizar.PIRA==1010:
            self.Fallido=True
            if Imprimir:
                print('('+self.nombre+') Falló en la búsqueda - Transcurrido: '+str(round(self.FigurasDeMerito['tiempo'],3))+' s')
        else:
            self.Fallido=False
            self.Xopt=self.Algoritmo.Xout
            if Imprimir:
                pcra=100-self.ControladorDeFuncionAminimizar.PIRA
                print('('+self.nombre+') - Transcurrido: '+str(round(self.FigurasDeMerito['tiempo'],3))+' s - PCRA:'+str(round(pcra,5)))
                
        self.BuscadorFinalizado.emit()

        
    def ejecutarMax(self):
        if self.Inicio: return
        else: self.Inicio=True
        
        global Imprimir
        global tolerancia
        self.BuscadorIniciado.emit()
        inicio=time()
        self.Nstubs=0
        self.Xopt=[]
        self.PIRAmejor=1010
        
        while (self.Nstubs < self.cvp.CreqStubs.datos[0][5]):
            self.Nstubs+=1
            if self.Nstubs==1: self.ControladorDeFuncionAminimizar.PrimerStub=True
            else: self.ControladorDeFuncionAminimizar.PrimerStub=False
            
            self.dim=2
                
            self.ControladorDeFuncionAminimizar.PIRA=1010
            
            try:
    
                self.Algoritmo.ejecutarMax()
                
            except:
                #traceback.print_exc()
                if self.Nstubs==1:
                    self.Fallido=True
                    if Imprimir: print('Error en ejecución del algoritmo '+self.nombre)
                    final=time()
                    self.FigurasDeMerito['tiempo']=final-inicio
                    self.BuscadorFinalizado.emit()
                    return
                else:
                    self.Nstubs-=1
                    break
                
                
            if self.ControladorDeFuncionAminimizar.PIRA!=1010:
                self.Fallido=False
                if (self.ControladorDeFuncionAminimizar.PIRA - self.PIRAmejor) < tolerancia:
                    self.PIRAmejor=self.ControladorDeFuncionAminimizar.PIRA
                    self.Xopt=self.Xopt+self.Algoritmo.Xout
                    if self.ControladorDeFuncionAminimizar.PIRA <= self.PIRAmin: break
                    else: pass
                else:
                    self.Nstubs-=1
                    break
            elif self.ControladorDeFuncionAminimizar.PIRA==1010:
                if self.Nstubs==1:
                    self.Fallido=True
                    if Imprimir: print('('+self.nombre+') Falló en la búsqueda')
                    break
                else:
                    self.Nstubs-=1
                    break
        
        final=time()
        self.FigurasDeMerito['tiempo']=final-inicio
        if Imprimir:
            pcra=100-self.PIRAmejor
            print('('+self.nombre+') '+ str(self.Nstubs) +' Stubs - Transcurrido: '+str(round(self.FigurasDeMerito['tiempo'],3))+' s - PCRA:'+str(round(pcra,5)))
        
        self.BuscadorFinalizado.emit()
        
    def run(self):
        try:
            self.FigurasDeMerito['cpu']=self.process.cpu_percent(interval=1)
            if self.cvp.CreqStubs.datos[0][4]=='Cantidad fija de stubs:' :
                self.FigurasDeMerito['ram']=memory_usage(self.ejecutarFijo,interval=.001, timeout=False, timestamps=False, #interval=0.5
                                      include_children=True, multiprocess=True, max_usage=True,
                                      retval=False, stream=None, backend=None, max_iterations=None)
    
            elif self.cvp.CreqStubs.datos[0][4]=='Cantidad máxima de stubs:' :
                self.FigurasDeMerito['ram']=memory_usage(self.ejecutarMax,interval=.001, timeout=False, timestamps=False,
                                      include_children=True, multiprocess=True, max_usage=True,
                                      retval=False, stream=None, backend=None, max_iterations=None)
             
            self.FigurasDeMerito['stubs']=self.Nstubs
            suma=0
            for usage in self.mediciones_cpu: suma+=usage
            if len(self.mediciones_cpu)!=0: self.FigurasDeMerito['cpu']=suma/len(self.mediciones_cpu)
            
            acum=int(float(self.cvp.Clinea.datos[3][0]))
            for n in range(self.FigurasDeMerito['stubs']):
                acum+=self.Xopt[2*n]
            self.posicion_entrada_adaptador=acum
            
            self.posicion=acum
            
        except:
            return

    def get_id(self): # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        
        for id, thread in threading._active.items():
            if thread is self:
                return id
    
    def detener(self): 
        self.raise_exception()
        while self.is_alive(): pass
    
    
    def raise_exception(self): #Esto detiene la ejecución de este Thread
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
                
    def Xopt_a_datos_Stubs(self):
        # disposicion,carga,Nstubs
        # d1,l1
        # d2,l2
        # ...
        # dN,lN
        
        self.datos=[[self.cvp.CreqStubs.datos[0][0],self.cvp.CreqStubs.datos[0][1],self.Nstubs]]
        for n in range(0,self.Nstubs):
            dn=int(self.Xopt[(n)*2])
            ln=int(self.Xopt[(n)*2+1])
            self.datos.append([dn,ln])
            
    def calcularZins(self,F,Alfa,Beta,Zc):

        from cmath import tanh as complextanh
        j=complex(0+1j)
        Zins=dict()
        for i in range(1,self.datos[0][2]+1):
            Zins['stub'+str(i)]=[]
            for indf in range(0,len(F)):
                if self.datos[0][1]=='Corto circuito':
                    Zins['stub'+str(i)].append(Zc[indf]*complextanh((Alfa[indf]+j*Beta[indf])*self.datos[i][1]*10**(-3)))
                elif self.datos[0][1]=='Circuito abierto':
                    Zins['stub'+str(i)].append(Zc[indf]/complextanh((Alfa[indf]+j*Beta[indf])*self.datos[i][1]*10**(-3)))
        return Zins
                
    def calcular_pcra(self):
        from math import sqrt
        modulo_gamma=self.coleccion_original.DIC['Coeficiente de reflexión - Magnitud'][-1]
        Funcion_objetivo=self.cvp.objetivo.FuncionObjetivo
        desviaciones=0       
        for i in range(0,len(Funcion_objetivo)): 
            if modulo_gamma[i] > Funcion_objetivo[i]:
                desviaciones += (modulo_gamma[i]-Funcion_objetivo[i])**2
        
        pira = sqrt(desviaciones/len(Funcion_objetivo))*100
        
        return (100-pira)
    
    def calcular_rizado(self):
        #return 404
        modulo_gamma=self.coleccion_original.DIC['Coeficiente de reflexión - Magnitud'][-1]
        menor=Infinity
        mayor=-1
        for valor in modulo_gamma:
            if valor > mayor: mayor=valor
            if valor < menor: menor=valor
        return (mayor-menor)
                
    def calcular_gamma_fo(self):
        modulo_gamma=self.coleccion_original.DIC['Coeficiente de reflexión - Magnitud'][-1]
        from Funciones import elemento_central
        return elemento_central(modulo_gamma)
    
    def calcular_zin(self,zc):
        zin=self.coleccion_original.Zin[-1] # A la entrada del adaptador
        desviaciones=0
        exc=0
        for i in range(len(zin)):
            if abs(zc[i])!=0: 
                desv=abs(zin[i]-zc[i])/abs(zc[i])
                desviaciones+=desv
            else:
                exc+=1
                
        return 100*desviaciones/(len(zin)-exc)
    
    def calcular_longitud(self):
        longitud=0
        N=int(float(self.datos[0][2]))
        for n in range(1,N+1): longitud+=int(float(self.datos[n][0]))
        return longitud

    def calcularFigurasDeMerito(self,ImpedanciaGenerador,Gamma_adp,Zdin,H_rad,F): #debe haberse actualizado self. datos y coleccion_original        
        self.FigurasDeMerito['stubs']=int(self.datos[0][2])
        self.Nstubs=int(self.datos[0][2])
        self.FigurasDeMerito['longitud']=self.calcular_longitud()
        
        self.FigurasDeMerito['perdida_Zo_fo']=perdida_Zo_fo(ImpedanciaGenerador,Zdin,F)
        self.FigurasDeMerito['max_perdida_Zo'],self.FigurasDeMerito['f_max_perdida_Zo']=max_perdida_Zo(ImpedanciaGenerador,Zdin,F)
        self.FigurasDeMerito['perdida_conj_fo']=perdida_conj_fo(ImpedanciaGenerador,Zdin,F)
        self.FigurasDeMerito['max_perdida_conj'],self.FigurasDeMerito['f_max_perdida_conj']=max_perdida_conj(ImpedanciaGenerador,Zdin,F)
        self.FigurasDeMerito['distorsion_fase']=distorsion_fase(H_rad,F)
        self.FigurasDeMerito['rizado']=rizado(Gamma_adp,F)
        self.FigurasDeMerito['gamma_fo']=gamma_fo(Gamma_adp,F)
        self.FigurasDeMerito['max_gamma'],self.FigurasDeMerito['f_max_gamma']=max_gamma(Gamma_adp,F)
        self.FigurasDeMerito['adaptacion_gamma']=adaptacion_gamma(Gamma_adp,F)
        
    def grafica_supera_valor(self,grafica,valor): 
        respuesta=False
        for item in grafica:
            if item <= valor:
                pass
            else:
                respuesta=True
                break
        
        return respuesta
    
    def entrada_adaptador(self,datos):
        acum=int(float(self.cvp.Clinea.datos[3][0]))
        for i in range(1,len(datos)):
            acum+=int(float(datos[i][0]))
            
        return acum
    
    def determinar_posicion_entrada_adaptador(self):
        self.posicion_entrada_adaptador=self.entrada_adaptador(self.datos)
        
        
    def crear_grafica(self,tipo,presentacion,VoltajeGenerador,ImpedanciaGenerador,
                      Alfa,Beta,Zc,rlgc_vs_f,Pmax,
                      DCA,DGA,
                      ZL,F,d=None): 
        # asume que Zins ya está calculado
        
        if d is None: self.posicion=self.posicion_entrada_adaptador
        else: self.posicion=d
        self.grafica=None
        
        if self.cvp.ventanaSecundariaResultados is None:
            from Eureka import M
        else:
            M=self.cvp.ventanaSecundariaResultados.M
        
        if tipo=='Potencia activa promedio': 
            self.grafica=funcion_vista_d(tipo,presentacion,VoltajeGenerador,ImpedanciaGenerador,
                                         Alfa,Beta,Zc,rlgc_vs_f,Pmax,
                                         self.datos,self.Zins,DCA,DGA,
                                         ZL,F,self.vectorD,self.posicion,M)#[self.posicion]
            
        elif tipo=='Respuesta en frecuencia':
            self.grafica=funcion_vista_d(tipo,presentacion,VoltajeGenerador,ImpedanciaGenerador,
                                         Alfa,Beta,Zc,rlgc_vs_f,Pmax,
                                         self.datos,self.Zins,DCA,DGA,
                                         ZL,F,self.vectorD,self.posicion,M)
        
        else:
            self.grafica=funcion_vista_d(tipo,presentacion,VoltajeGenerador,ImpedanciaGenerador,
                                         Alfa,Beta,Zc,rlgc_vs_f,Pmax,
                                         self.datos,self.Zins,DCA,DGA,
                                         ZL,F,self.vectorD,self.posicion,M)
            
            
            
        
class NelderMead():
    def __init__(self,Buscador):
        from scipy.optimize import minimize
        self.minimize=minimize
        self.Buscador=Buscador
        self.Buscador.color='b'
    
    def ejecutarFijo(self):
        Xi=self.Buscador.XoSeed(self.Buscador.dim)
        self.respuesta=self.minimize(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,method='Nelder-Mead',options={'maxiter':None,'maxfev':None,
                                                                                            'disp':False,'return_all':False,
                                                                                            'initial_simplex':None,'xatol':0.2,
                                                                                            'fatol':0.01,'adaptive':True})
        # Original
        # self.respuesta=self.minimize(self..BuscadorControladorDeFuncionAminimizar.FAM,self.Xi,method='Nelder-Mead',options={'maxiter':None,'maxfev':None,
        #                                                                                     'disp':False,'return_all':False,
        #                                                                                     'initial_simplex':None,'xatol':0.0001,
        #                                                                                     'fatol':0.0001,'adaptive':False}) 
        
        self.Xout=self.respuesta.x
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
    
    def ejecutarMax(self):
        Xi=self.Buscador.XoSeed(self.Buscador.dim)
        self.respuesta=self.minimize(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,method='Nelder-Mead',options={'maxiter':None,'maxfev':None,
                                                                                        'disp':False,'return_all':False,
                                                                                        'initial_simplex':None,'xatol':0.2,
                                                                                        'fatol':0.01,'adaptive':True})
        # Original
        # self.respuesta=self.minimize(self.ControladorDeFuncionAminimizar.FAM,Xi,method='Nelder-Mead',options={'maxiter':None,'maxfev':None,
        #                                                                                     'disp':False,'return_all':False,
        #                                                                                     'initial_simplex':None,'xatol':0.0001,
        #                                                                                     'fatol':0.0001,'adaptive':False})
        self.Xout=self.respuesta.x
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
        

class DifferentialEvolution():
    def __init__(self,Buscador):
        from scipy.optimize import differential_evolution
        self.differential_evolution=differential_evolution
        self.Buscador=Buscador
        self.Buscador.color='g'
    
    def ejecutarFijo(self):
        Xi=self.Buscador.XoBounds(self.Buscador.dim)
        self.respuesta=self.differential_evolution(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),strategy='best1bin',maxiter=1000,popsize=15,
                                              tol=0.01,mutation=(0.5,1),recombination=0.7,seed=None,callback=None,disp=False,
                                              polish=True,init='latinhypercube',atol=0,updating='immediate',workers=1,constraints=())
        # Original
        # self.respuesta=self.differential_evolution(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),strategy='best1bin',maxiter=1000,popsize=15,
        #                                       tol=0.01,mutation=(0.5,1),recombination=0.7,seed=None,callback=None,disp=False,
        #                                       polish=True,init='latinhypercube',atol=0,updating='immediate',workers=1,constraints=())
        self.Xout=self.respuesta.x
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
    
    def ejecutarMax(self):
        Xi=self.Buscador.XoBounds(self.Buscador.dim)            
        self.respuesta=self.differential_evolution(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),strategy='best1bin',maxiter=100,popsize=15,
                                              tol=0.01,mutation=(0.5,1),recombination=0.7,seed=None,callback=None,disp=False,
                                              polish=True,init='latinhypercube',atol=0,updating='immediate',workers=1,constraints=())
        # Original
        # self.respuesta=self.differential_evolution(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),strategy='best1bin',maxiter=1000,popsize=15,
        #                                       tol=0.01,mutation=(0.5,1),recombination=0.7,seed=None,callback=None,disp=False,
        #                                       polish=True,init='latinhypercube',atol=0,updating='immediate',workers=1,constraints=())
        self.Xout=self.respuesta.x
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
        
        
class DualAnnealing():
    def __init__(self,Buscador):
        from scipy.optimize import dual_annealing
        self.dual_annealing = dual_annealing
        self.Buscador=Buscador
        self.Buscador.color='y'
    
    def ejecutarFijo(self):
        Xi=self.Buscador.XoBounds(self.Buscador.dim)
        self.respuesta=self.dual_annealing(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),maxiter=1000,local_search_options={},initial_temp=5230.0,
                                      restart_temp_ratio=2e-05,visit=2.62,accept=-5.0,maxfun=10000000.0,seed=None,
                                      no_local_search=False,callback=None,x0=None)
        # Original
        # self.respuesta=self.dual_annealing(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),maxiter=1000,local_search_options={},initial_temp=5230.0,
        #                               restart_temp_ratio=2e-05,visit=2.62,accept=-5.0,maxfun=10000000.0,seed=None,
        #                               no_local_search=False,callback=None,x0=None)
        self.Xout=self.respuesta.x
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
    
    def ejecutarMax(self):
        Xi=self.Buscador.XoBounds(self.Buscador.dim)            
        self.respuesta=self.dual_annealing(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),maxiter=1000,local_search_options={},initial_temp=5230.0,
                                      restart_temp_ratio=2e-05,visit=2.62,accept=-5.0,maxfun=10000000.0,seed=None,
                                      no_local_search=False,callback=None,x0=None)
        # Original
        # self.respuesta=self.dual_annealing(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),maxiter=1000,local_search_options={},initial_temp=5230.0,
        #                               restart_temp_ratio=2e-05,visit=2.62,accept=-5.0,maxfun=10000000.0,seed=None,
        #                               no_local_search=False,callback=None,x0=None)
        self.Xout=self.respuesta.x
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
        
        
class BruteForce():
    def __init__(self,Buscador):
        from scipy.optimize import brute,fmin
        self.brute = brute
        self.fmin=fmin
        self.Buscador=Buscador
        self.Buscador.color='c'
    
    def ejecutarFijo(self):
        Xi=self.Buscador.XoBounds(self.Buscador.dim)
        self.respuesta=self.brute(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),Ns=2,full_output=0,finish=self.fmin,disp=False,workers=1)
        # Original
        # self.respuesta=self.brute(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),Ns=20,full_output=0,finish=None,disp=False,workers=1)
        self.Xout=self.respuesta
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
    
    def ejecutarMax(self):
        Xi=self.Buscador.XoBounds(self.Buscador.dim)            
        self.respuesta=self.brute(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),Ns=20,full_output=0,finish=self.fmin,disp=False,workers=1)
        # Original
        # self.respuesta=self.brute(self.Buscador.ControladorDeFuncionAminimizar.FAM,Xi,args=(),Ns=20,full_output=0,finish=None,disp=False,workers=1)
        self.Xout=self.respuesta
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
        
class WhaleOptimizationAlgorithm():
    def __init__(self,Buscador):
        from mealpy.swarm_based.WOA import BaseWOA
        self.BaseWOA = BaseWOA
        self.Buscador=Buscador
        self.Buscador.color='C5'
    
    def ejecutarFijo(self):
        ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=700
        # pop_size=50
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
            
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 100
        
        self.respuesta = self.BaseWOA(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
    
    def ejecutarMax(self):
        ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=700
        # pop_size=50
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 10
        
        self.respuesta = self.BaseWOA(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
        
class EquilibriumOptimizer():
    def __init__(self,Buscador):
        from mealpy.physics_based.EO import BaseEO
        self.BaseEO = BaseEO
        self.Buscador=Buscador
        self.Buscador.color='C1'
    
    def ejecutarFijo(self):
        ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=750
        # pop_size=100
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
            
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 100
        
        self.respuesta = self.BaseEO(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
    
    def ejecutarMax(self):
        ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=750
        # pop_size=100
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
            
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 10
        
        self.respuesta = self.BaseEO(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
        
class HarrisHawksOptimization():
    def __init__(self,Buscador):
        from mealpy.swarm_based.HHO import BaseHHO
        self.BaseHHO = BaseHHO
        self.Buscador=Buscador
        self.Buscador.color='C7'
    
    def ejecutarFijo(self):
        ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=750
        # pop_size=100
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
            
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 100
        
        self.respuesta = self.BaseHHO(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
    
    def ejecutarMax(self):
         ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=750
        # pop_size=100
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
            
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 10
        
        self.respuesta = self.BaseHHO(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
               
class VirusColonySearch():
    def __init__(self,Buscador):
        from mealpy.bio_based.VCS import BaseVCS
        self.BaseVCS = BaseVCS
        self.Buscador=Buscador
        self.Buscador.color='m'
        
    def ejecutarFijo(self):
        ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=750
        # pop_size=100
        # lamda=0.5 # Weight factor
        # xichma=0.3 # Number of the best will keep
        
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
            
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 100
        lamda=0.5
        xichma=0.3
        
        self.respuesta = self.BaseVCS(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size,lamda,xichma)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
    
    def ejecutarMax(self):
        ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=750
        # pop_size=100
        # lamda=0.5 # Weight factor
        # xichma=0.3 # Number of the best will keep
        
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
            
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 10
        lamda=0.5
        xichma=0.3
        
        self.respuesta = self.BaseVCS(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size,lamda,xichma)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
        
class ArtificialEcosystemBasedOptimization():
    def __init__(self,Buscador):
        from mealpy.system_based.AEO import BaseAEO
        self.BaseAEO = BaseAEO
        self.Buscador=Buscador
        self.Buscador.color='C4'
    
    def ejecutarFijo(self):
        ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=750
        # pop_size=100
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
            
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 100
        
        self.respuesta = self.BaseAEO(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
    
    def ejecutarMax(self):
        ## Parametros Originales
        # objective_func=None
        # lb=None
        # ub=None
        # problem_size=50 
        # batch_size=10
        # verbose=True
        # epoch=750
        # pop_size=100
        objective_func = self.Buscador.ControladorDeFuncionAminimizar.FAM
        if self.Buscador.EnteroPar(self.Buscador.dim):
            lb = [self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
        else:
            lb = [self.Buscador.lmin]+[self.Buscador.dmin,self.Buscador.lmin]*int(self.Buscador.dim/2)
            ub = [self.Buscador.lmax]+[self.Buscador.dmax,self.Buscador.lmax]*int(self.Buscador.dim/2)
            
        problem_size = self.Buscador.dim
        batch_size = 10
        verbose = False
        epoch = 100
        pop_size = 10
        
        self.respuesta = self.BaseAEO(objective_func,lb,ub,problem_size,batch_size,verbose,epoch,pop_size)
        best_position, best_fit, list_loss = self.respuesta.train()
        
        self.Xout=best_position
        aux=[]
        for elemento in self.Xout: aux.append(round(float(elemento)))
        self.Xout=aux
        self.PIRA=self.Buscador.ControladorDeFuncionAminimizar.PIRA
        

#    
######################################################### Agregar acá los Algoritmos que se necesiten, en formato de clases
#        
        
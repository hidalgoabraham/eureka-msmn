
# -*- coding: utf-8 -*-
"""
@author: Abraham Hidalgo

Universidad de Carabobo
Ingeniero de Telecomunicaciones

correo: ahidalgo3@uc.edu.ve

"""
from math import pi
from math import tan
from math import sqrt
from cmath import phase
from cmath import sqrt as complexsqrt
from cmath import tanh as complextanh
from cmath import e
from math import log10
from cmath import polar

from math import acosh
from math import log
from numpy import linspace

from numpy import Infinity
from scipy.interpolate import interp1d
from numpy import polyfit
import threading

from time import time

#Globales
e_o=8.854 #Permitividad eléctrica del vacío [pF/m]
u_o=1256.637 #Permeabilidad magnética del vacío [nH/m]


def ZCARGA(F,datos,z_vs_f): # R en Ohm, L en nH, C en pF, f en MHz
    j=complex(0+1j)
    p=pi
    m=[]
    
    if datos[0][0]=='Modelo':
        if datos[1][0]=='R':
            R=datos[2][0]
            for f in F: m.append(R)
            
        elif datos[1][0]=='L':
            L=datos[2][0]*1e-9
            for f in F:
                wi=2*p*f*1e6
                m.append(j*wi*L)
                
        elif datos[1][0]=='C':
            C=datos[2][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                m.append(1/(j*wi*C))
                
        elif datos[1][0]=='R-s-L':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            for f in F:
                wi=2*p*f*1e6
                m.append(R+j*wi*L)
            
        elif datos[1][0]=='R-s-C':
            R=datos[2][0]
            C=datos[3][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                m.append(R+1/(j*wi*C))
                
        elif datos[1][0]=='L-s-C':
            L=datos[2][0]*1e-9
            C=datos[3][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                m.append(j*wi*L+1/(j*wi*C))
            
        elif datos[1][0]=='R-p-L':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                m.append((R*zl)/(R+zl))
            
        elif datos[1][0]=='R-p-C':
            R=datos[2][0]
            C=datos[3][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zc=1/(j*wi*C)
                m.append((R*zc)/(R+zc))
            
        elif datos[1][0]=='L-p-C':
            L=datos[2][0]*1e-9
            C=datos[3][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                zc=1/(j*wi*C)
                m.append((zl*zc)/(zl+zc))
            
        elif datos[1][0]=='R-s-L-s-C':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            C=datos[4][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                zc=1/(j*wi*C)
                m.append(R+zl+zc)
            
        elif datos[1][0]=='R-p-L-p-C':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            C=datos[4][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                zc=1/(j*wi*C)
                zp=(zl*zc)/(zl+zc)
                m.append((R*zp)/(R+zp))
                
        elif datos[1][0]=='R-s-(L-p-C)':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            C=datos[4][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                zc=1/(j*wi*C)
                zp=(zl*zc)/(zl+zc)
                m.append(R+zp)
            
        elif datos[1][0]=='R-p-(L-s-C)':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            C=datos[4][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                zc=1/(j*wi*C)
                zs=zl+zc
                m.append((R*zs)/(R+zs))
            
        elif datos[1][0]=='L-s-(R-p-C)':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            C=datos[4][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                zc=1/(j*wi*C)
                zp=(R*zc)/(R+zc)
                m.append(zl+zp)
            
        elif datos[1][0]=='L-p-(R-s-C)':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            C=datos[4][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                zc=1/(j*wi*C)
                zs=R+zc
                m.append((zl*zs)/(zl+zs))
            
        elif datos[1][0]=='C-s-(R-p-L)':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            C=datos[4][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                zc=1/(j*wi*C)
                zp=(R*zl)/(R+zl)
                m.append(zc+zp)
                
        elif datos[1][0]=='C-p-(R-s-L)':
            R=datos[2][0]
            L=datos[3][0]*1e-9
            C=datos[4][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl=j*wi*L
                zc=1/(j*wi*C)
                zs=R+zl
                m.append((zc*zs)/(zc+zs))
                
        elif datos[1][0]=='Antena Microstrip':
            L1=datos[2][0]*1e-9
            C1=datos[3][0]*1e-12
            R=datos[4][0]
            L=datos[5][0]*1e-9
            C=datos[6][0]*1e-12
            for f in F:
                wi=2*p*f*1e6
                zl1=j*wi*L1
                zc1=1/(j*wi*C1)
                zs=zl1+zc1
                zl=j*wi*L
                zc=1/(j*wi*C)
                zp1=(zl*zc)/(zl+zc)
                zp=(R*zp1)/(R+zp1)
                m.append(zs+zp)
            
    elif datos[0][0]=='Archivo':
        funcion = interp1d(z_vs_f[1],z_vs_f[0],kind='linear',fill_value='extrapolate')
        Z = funcion(F)    
        for z in Z: m.append(z)
    
    return m

def FUENTE(F,s_vs_f):
    m=[]
    funcion = interp1d(s_vs_f[1],s_vs_f[0],kind='linear',fill_value='extrapolate')
    S = funcion(F)   
    
    for indf in range(len(F)):
        if F[indf] < s_vs_f[1][0] or F[indf] > s_vs_f[1][-1] :
            s=0
        else:
            if S[indf] >=0 : s=S[indf]
            else: s=0
    
        m.append(s)      
    return m
    
    
   

def matrizceros(filas,columnas):
    M=[[]]
    for i in range(0,filas):
        for j in range(0,columnas):
            M[i].append(0)
        M.append([])
    del M[-1]
    return M

def listaceros(columnas):
    M=[]
    if columnas==0: return M
    for j in range(columnas):
        M[j].append(0)
    return M

 
def Zvista(datosStubs,Zins,Alfa,Beta,Zc,ZL,F,D):
    M=matrizceros(len(D),len(F))
        
    for indf in range(0,len(F)):
        zv(indf,D,ZL,Zc[indf],Alfa[indf],Beta[indf],datosStubs,Zins,M)
    return M

def zv(indf,D,ZL,ZcL,AlfaL,BetaL,datosStubs,Zins,M):#esta no es recursiva
    j=complex(0+1j)
    
    for i in range(0,len(D)):
        if i==0: #Plano de carga
            M[i][indf]=ZL[indf]
        else:
            L=D[i].posicion-D[i-1].posicion
            L=L*10**(-3)#Ahora está en m
            # z vista sin stub
            zvss=ZcL*((M[i-1][indf]+ZcL*complextanh((AlfaL+j*BetaL)*L))/(ZcL+M[i-1][indf]*complextanh((AlfaL+j*BetaL)*L)))
            if(D[i].esStub):
                M[i][indf]=SumaconStub(zvss,indf,datosStubs,Zins,D[i].indiceStub)
            else:
                M[i][indf]=zvss   
                
def SumaconStub(zvss,indf,datosStubs,Zins,i): 
    if (datosStubs[0][0]=='Serie'):
        return (zvss + Zins['stub'+str(i)][indf])
    elif (datosStubs[0][0]=='Paralelo'):
        return 1/((1/zvss)+(1/Zins['stub'+str(i)][indf]))

def Zcsinperdidas(F,Ro): 
    m=[]
    for i in range(0,len(F)):m.append(Ro)
    return m #en Ohm

def Alfasinperdidas(F): 
    m=[]
    for i in range(0,len(F)):m.append(0.0)
    return m # en Np/m
    
def Betasinperdidas(F,tipocoero,coero,Ro): 
    m=[]
    c=0.0
    if tipocoero=='Constante dieléctrica relativa':
        c=(sqrt(coero)*10**(4))/(Ro*2.998)
    elif tipocoero=='Velocidad de propagación (%)':
        c=(10**(6))/(Ro*2.998*coero)
    elif tipocoero=='Capacitancia distribuida (pF/m)' or tipocoero=='Capacitancia distribuida del stub (pF/m)':
        c=coero

    for i in range(0,len(F)):
        b=2*pi*F[i]*c*Ro*10**(-6) #Ahora está en rad/m
        m.append(b) 
    return m

def rlgc_ABZ_sinPerdidas(F,tipocoero,coero,Ro):
    
    rvf=[]
    lvf=[]
    gvf=[]
    cvf=[]
    coero=float(coero)
    Ro=float(Ro) # [Ohm]
    if tipocoero=='Constante dieléctrica relativa': c=(sqrt(coero)*10**(4))/(Ro*2.998) # [pF/m]
    elif tipocoero=='Velocidad de propagación (%)': c=(10**(6))/(Ro*2.998*coero) # [pF/m]
    elif tipocoero=='Capacitancia distribuida (pF/m)': c=coero # [pF/m]
    g=0
    l=(Ro**2)*c*1e-3 # [nH/m]
    r=0
    
    Alfa=[]
    Beta=[]
    Zc=[]
    
    for f in F:
        rvf.append(r)
        lvf.append(l)
        gvf.append(g)
        cvf.append(c)
        
        Alfa.append(0)
        Beta.append(2*pi*f*c*Ro*1e-6) #Ahora está en rad/m
        Zc.append(Ro)
        
    return rvf,lvf,gvf,cvf,Alfa,Beta,Zc



def Alfabajasperdidas(F,Nmedidas,Medidas): 
    x=[]
    y=[]
    Alfa=[]
    for i in range(0,Nmedidas):
        y.append(Medidas[i*2]/868.6) # Ahora está en Np/m
        x.append(Medidas[i*2+1])

    A = interp1d(x,y,kind='linear',fill_value='extrapolate')
    Alf = A(F)
    

    for a in Alf: Alfa.append(a) #está en Np/m
    return Alfa
        
def Alfaperdidasgenerales(F,r,l,g,c): 
    j=complex(0+1j)
    Alfa=[]
    for f in F:
        Alfa.append(complexsqrt((r+j*2*pi*f*10**(-3)*l)*(g+j*2*pi*f*10**(-6)*c)).real) #está en Np/m
    return Alfa

def Betaperdidasgenerales(F,r,l,g,c): 
    j=complex(0+1j)
    Beta=[]
    for f in F:
        Beta.append(complexsqrt((r+j*2*pi*f*10**(-3)*l)*(g+j*2*pi*f*10**(-6)*c)).imag) #está en rad/m
    return Beta

def Zcperdidasgenerales(F,r,l,g,c): 
    j=complex(0+1j)
    Zc=[]
    for f in F:
        Zc.append(complexsqrt((r+j*2*pi*f*10**(-3)*l)/(g+j*2*pi*f*10**(-6)*c))) #está en Ohm
    return Zc

def rlgc_ABZ_perdidasGenerales(F,r,l,g,c):
    j=complex(0+1j)
    
    rvf=[]
    lvf=[]
    gvf=[]
    cvf=[]

    r=float(r)    
    l=float(l)
    g=float(g)
    c=float(c)
    
    Alfa=[]
    Beta=[]
    Zc=[]
    
    for f in F:
        rvf.append(r)
        lvf.append(l)
        gvf.append(g)
        cvf.append(c)
        
        Alfa.append(complexsqrt((r+j*2*pi*f*10**(-3)*l)*(g+j*2*pi*f*10**(-6)*c)).real) #está en Np/m
        Beta.append(complexsqrt((r+j*2*pi*f*10**(-3)*l)*(g+j*2*pi*f*10**(-6)*c)).imag) #está en rad/m
        Zc.append(complexsqrt((r+j*2*pi*f*10**(-3)*l)/(g+j*2*pi*f*10**(-6)*c))) #está en Ohm
        
    return rvf,lvf,gvf,cvf,Alfa,Beta,Zc



def AlfaLtx(F,tipoltx,a,b,urc,Dc,urd,erd,Dd): 
    global e_o,u_o
    j=complex(0+1j)
    Alfa=[]
    if tipoltx=='Coaxial':
        if a>=b : raise ValueError
        for f in F:
            r=((sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(2*pi*Dc*10**(6)))*(1/(a*10**(-3))+1/(b*10**(-3))) #está en Ohm/m
            l=((urd*u_o*10**(-9))/(2*pi))*log((b)/(a)) #está en H/m
            g=(2*pi*Dd*10**(-12))/(log((b)/(a))) #está en S/m
            c=(2*pi*erd*e_o*10**(-12))/(log((b)/(a))) #está en f/m
            Alfa.append(complexsqrt((r+j*2*pi*f*10**(6)*l)*(g+j*2*pi*f*10**(6)*c)).real)
    
        return Alfa #está en Np/m

    elif tipoltx=='Bifilar':
        if a>=b/2 : raise ValueError
        for f in F:
            r=(sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(pi*a*10**(-3)*Dc*10**(6)) #está en Ohm/m
            l=((urd*u_o*10**(-9))/(pi))*acosh((b)/(2*a)) #está en H/m
            g=(pi*Dd*10**(-12))/(acosh((b)/(2*a))) #está en S/m
            c=(pi*erd*e_o*10**(-12))/(acosh((b)/(2*a)))
            Alfa.append(complexsqrt((r+j*2*pi*f*10**(6)*l)*(g+j*2*pi*f*10**(6)*c)).real)
    
        return Alfa #está en Np/m

    elif tipoltx=='Plana':
        for f in F:
            r=(2*sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(b*10**(-3)*Dc*10**(6)) #está en Ohm/m
            l=(urd*u_o*10**(-9)*a)/(b) #está en H/m
            g=(Dd*10**(-12)*b)/(a)
            c=(erd*e_o*10**(-12)*b)/(a)
            Alfa.append(complexsqrt((r+j*2*pi*f*10**(6)*l)*(g+j*2*pi*f*10**(6)*c)).real)
    
        return Alfa #está en Np/m

def BetaLtx(F,tipoltx,a,b,urc,Dc,urd,erd,Dd): 
    global e_o,u_o
    j=complex(0+1j)
    Beta=[]
    if tipoltx=='Coaxial':
        if a>=b : raise ValueError
        for f in F:
            r=((sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(2*pi*Dc*10**(6)))*(1/(a*10**(-3))+1/(b*10**(-3))) #está en Ohm/m
            l=((urd*u_o*10**(-9))/(2*pi))*log((b)/(a)) #está en H/m
            g=(2*pi*Dd*10**(-12))/(log((b)/(a))) #está en S/m
            c=(2*pi*erd*e_o*10**(-12))/(log((b)/(a))) #está en f/m
            Beta.append(complexsqrt((r+j*2*pi*f*10**(6)*l)*(g+j*2*pi*f*10**(6)*c)).imag)
    
        return Beta #está en rad/m

    elif tipoltx=='Bifilar':
        if a>=b/2 : raise ValueError
        for f in F:
            r=(sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(pi*a*10**(-3)*Dc*10**(6)) #está en Ohm/m
            l=((urd*u_o*10**(-9))/(pi))*acosh((b)/(2*a)) #está en H/m
            g=(pi*Dd*10**(-12))/(acosh((b)/(2*a))) #está en S/m
            c=(pi*erd*e_o*10**(-12))/(acosh((b)/(2*a)))
            Beta.append(complexsqrt((r+j*2*pi*f*10**(6)*l)*(g+j*2*pi*f*10**(6)*c)).imag)
    
        return Beta #está en rad/m

    elif tipoltx=='Plana':
        for f in F:
            r=(2*sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(b*10**(-3)*Dc*10**(6)) #está en Ohm/m
            l=(urd*u_o*10**(-9)*a)/(b) #está en H/m
            g=(Dd*10**(-12)*b)/(a)
            c=(erd*e_o*10**(-12)*b)/(a)
            Beta.append(complexsqrt((r+j*2*pi*f*10**(6)*l)*(g+j*2*pi*f*10**(6)*c)).imag)
    
        return Beta #está en rad/m

def ZcLtx(F,tipoltx,a,b,urc,Dc,urd,erd,Dd): 
    global e_o,u_o
    j=complex(0+1j)
    Zc=[]
    if tipoltx=='Coaxial':
        if a>=b : raise ValueError
        for f in F:
            r=((sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(2*pi*Dc*10**(6)))*(1/(a*10**(-3))+1/(b*10**(-3))) #está en Ohm/m
            l=((urd*u_o*10**(-9))/(2*pi))*log((b)/(a)) #está en H/m
            g=(2*pi*Dd*10**(-12))/(log((b)/(a))) #está en S/m
            c=(2*pi*erd*e_o*10**(-12))/(log((b)/(a))) #está en f/m
            Zc.append(complexsqrt((r+j*2*pi*f*10**(6)*l)/(g+j*2*pi*f*10**(6)*c)))
    
        return Zc #está en Ohm

    elif tipoltx=='Bifilar':
        if a>=b/2 : raise ValueError
        for f in F:
            r=(sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(pi*a*10**(-3)*Dc*10**(6)) #está en Ohm/m
            l=((urd*u_o*10**(-9))/(pi))*acosh((b)/(2*a)) #está en H/m
            g=(pi*Dd*10**(-12))/(acosh((b)/(2*a))) #está en S/m
            c=(pi*erd*e_o*10**(-12))/(acosh((b)/(2*a)))
            Zc.append(complexsqrt((r+j*2*pi*f*10**(6)*l)/(g+j*2*pi*f*10**(6)*c)))
    
        return Zc #está en Ohm

    elif tipoltx=='Plana':
        for f in F:
            r=(2*sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(b*10**(-3)*Dc*10**(6)) #está en Ohm/m
            l=(urd*u_o*10**(-9)*a)/(b) #está en H/m
            g=(Dd*10**(-12)*b)/(a)
            c=(erd*e_o*10**(-12)*b)/(a)
            Zc.append(complexsqrt((r+j*2*pi*f*10**(6)*l)/(g+j*2*pi*f*10**(6)*c)))
    
        return Zc #está en Ohm

def rlgc_ABZ_Ltx(F,tipoltx,a,b,urc,Dc,urd,erd,Dd):
    j=complex(0+1j)
    global e_o,u_o
    
    a=float(a)
    b=float(b)
    urc=float(urc)
    Dc=float(Dc)
    urd=float(urd)
    erd=float(erd)
    Dd=float(Dd)
    
    rvf=[]
    lvf=[]
    gvf=[]
    cvf=[]
    
    Alfa=[]
    Beta=[]
    Zc=[]
    
    if tipoltx=='Coaxial':
        if a>=b : raise ValueError
        for f in F:
            r=((sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(2*pi*Dc*10**(6)))*(1/(a*10**(-3))+1/(b*10**(-3))) #está en Ohm/m
            l=((urd*u_o)/(2*pi))*log((b)/(a)) #está en nH/m
            g=(2*pi*Dd*10**(-12))/(log((b)/(a))) #está en S/m
            c=(2*pi*erd*e_o)/(log((b)/(a))) #está en pF/m
            rvf.append(r)
            lvf.append(l)
            gvf.append(g)
            cvf.append(c)
            Alfa.append(complexsqrt((r+j*2*pi*f*10**(6)*l*10**(-9))*(g+j*2*pi*f*10**(6)*c*10**(-12))).real) #está en Np/m
            Beta.append(complexsqrt((r+j*2*pi*f*10**(6)*l*10**(-9))*(g+j*2*pi*f*10**(6)*c*10**(-12))).imag) #está en rad/m
            Zc.append(complexsqrt((r+j*2*pi*f*10**(6)*l*10**(-9))/(g+j*2*pi*f*10**(6)*c*10**(-12)))) #está en Ohm
    
    elif tipoltx=='Bifilar':
        if a>=b/2 : raise ValueError
        for f in F:
            r=(sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(pi*a*10**(-3)*Dc*10**(6)) #está en Ohm/m
            l=((urd*u_o)/(pi))*acosh((b)/(2*a)) #está en nH/m
            g=(pi*Dd*10**(-12))/(acosh((b)/(2*a))) #está en S/m
            c=(pi*erd*e_o)/(acosh((b)/(2*a))) #está en pF/m
            rvf.append(r)
            lvf.append(l)
            gvf.append(g)
            cvf.append(c)
            Alfa.append(complexsqrt((r+j*2*pi*f*10**(6)*l*10**(-9))*(g+j*2*pi*f*10**(6)*c*10**(-12))).real) #está en Np/m
            Beta.append(complexsqrt((r+j*2*pi*f*10**(6)*l*10**(-9))*(g+j*2*pi*f*10**(6)*c*10**(-12))).imag) #está en rad/m
            Zc.append(complexsqrt((r+j*2*pi*f*10**(6)*l*10**(-9))/(g+j*2*pi*f*10**(6)*c*10**(-12)))) #está en Ohm

    elif tipoltx=='Plana':
        for f in F:
            r=(2*sqrt(pi*f*10**(6)*urc*u_o*10**(-9)*Dc*10**(6)))/(b*10**(-3)*Dc*10**(6)) #está en Ohm/m
            l=(urd*u_o*a)/(b) #está en nH/m
            g=(Dd*10**(-12)*b)/(a) #está en S/m
            c=(erd*e_o*b)/(a) #está en pF/m
            rvf.append(r)
            lvf.append(l)
            gvf.append(g)
            cvf.append(c)
            Alfa.append(complexsqrt((r+j*2*pi*f*10**(6)*l*10**(-9))*(g+j*2*pi*f*10**(6)*c*10**(-12))).real) #está en Np/m
            Beta.append(complexsqrt((r+j*2*pi*f*10**(6)*l*10**(-9))*(g+j*2*pi*f*10**(6)*c*10**(-12))).imag) #está en rad/m
            Zc.append(complexsqrt((r+j*2*pi*f*10**(6)*l*10**(-9))/(g+j*2*pi*f*10**(6)*c*10**(-12)))) #está en Ohm
            
    return rvf,lvf,gvf,cvf,Alfa,Beta,Zc

    
def MatrixReal(m):
    mm=matrizceros(len(m),len(m[0]))
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            mm[i][j]=m[i][j].real
    return mm

def MatrixImag(m):
    mm=matrizceros(len(m),len(m[0]))
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            mm[i][j]=m[i][j].imag
    return mm

def MatrixModulo(m):
    mm=matrizceros(len(m),len(m[0]))
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            mm[i][j]=abs(m[i][j])
    return mm

def MatrixFase(m):
    mm=matrizceros(len(m),len(m[0]))
    for i in range(0,len(m)):
        for j in range(0,len(m[0])):
            mm[i][j]=phase(m[i][j])*(180/pi)
    return mm

def Gamma(Z,Zc):
    g=matrizceros(len(Z),len(Z[0]))
    for i in range(0,len(Z)):
        for j in range(0,len(Z[0])):
            valor=Z[i][j]+Zc[j]
            if valor==0: valor=1e-16
            g[i][j]=(Z[i][j]-Zc[j])/(valor)
    return g

def Tau(R):
    t=matrizceros(len(R),len(R[0]))
    for i in range(0,len(R)):
        for j in range(0,len(R[0])):
            t[i][j]=1+R[i][j]
    return t

def SWR(G): 
    swr=matrizceros(len(G),len(G[0]))
    for i in range(0,len(G)):
        for j in range(0,len(G[0])):
            valor = abs(G[i][j])
            if valor==1.0: valor = 1-1e-16 #0.00000000000000001 es la mayor precisión para el coeficiente de reflexión
            
            swr[i][j]=(1+valor/(1-valor))
    return swr

def decibel(matriz):
    res=matrizceros(len(matriz),len(matriz[0]))
    
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[0])):
            valor=matriz[i][j]
            if valor==0: valor=1e-16
            res[i][j]=20*log10(valor)   
    return res
            
def Nsteps(di,ds,st):
    n=[0,0]
    cdi=di
    while (cdi+st)<=ds :
        cdi+=st
        n[0]+=1
    if (cdi+st)>ds:
        n[1]=ds-cdi#paso especial
    return n
    
class Punto:
    def __init__(self,pos=0,es=False,inds=0,supera_potencia=False):
        self.posicion=pos
        self.esStub=es
        self.indiceStub=inds
        self.supera_potencia=supera_potencia
        
def vectordistancias(datos,DCA,DGA):
    # disposicion,carga,Nstubs
    # D1,L1
    # D2,L2
    # ...
    # DN,LN
    
    posicion=0
    D=[]
    D.append(Punto())
    posiciones_stubs=[] # [DCA+D1, DCA+D1+D2, DCA+D1+D2+D3, ...]
    dtotal=int(float(DCA)) # la distancia desde la carga hasta la salida del adaptador
    N=int(float(datos[0][2]))
    for n in range(1,N+1):
        dtotal+=int(float(datos[n][0]))
        posiciones_stubs.append(dtotal)
        
    dtotal+=int(float(DGA)) # la distancia desde la entrada del adaptador hasta el generador
    
    for posicion in range(1,dtotal+1):
        
        if posicion in posiciones_stubs:
            inds=posiciones_stubs.index(posicion)
            D.append(Punto(posicion,True,inds+1))
        else:
            D.append(Punto(posicion))

    return D

def descubrir_puntos_supera_Pmax(vectorD,P_d_f,Pmax):
    for d in range(len(vectorD)):
        for indf in range(len(P_d_f[d])):
            if P_d_f[d][indf] > Pmax: 
                vectorD[d].supera_potencia=True
                break
    
    return vectorD

def existe(buscado,lista):
    for elemento in lista:
        if elemento==buscado: return True
    return False
    
def mayor2vectores(vector1,vector2):
    vector=vector1+vector2
    m=vector[0]
    for v in vector:
        if v>m: m=v
    return m

def mayor2floats(f1,f2):
    if f1>=f2:return f1
    else: return f2
    
def ZetaNorm(Zin,Zo):
    m=[]
    for d in range(0,len(Zin)):
        m.append([])
        for f in range(0,len(Zin[0])): m[d].append(Zin[d][f]/Zo[f])
    return m
        
def circunferencia(radio,mitad_puntos):
    x=linspace(-radio,radio,mitad_puntos)
    y_p=[]
    y_n=[]
            
    for item in x:
        num=sqrt(radio**2-(item**2))
        y_p.append(num)
        num=(-1)*sqrt(radio**2-(item**2))
        y_n.append(num)             
    return x, y_n, y_p

def elemento_central(lista):
    posicion=int((len(lista)-1)/2)
    return lista[posicion]

def lista_arreglada(lista,pos):
    respuesta=lista
    aux=respuesta[-1]
    for i in range(0,len(lista)-1-pos):
        posicion_actual=len(respuesta)-1-i
        respuesta[posicion_actual]=respuesta[posicion_actual-1]
    respuesta[pos]=aux
    return respuesta

def matriz_ordenada(diccionario,mayor_a_menor):
    copia_dic=diccionario
    valores=[]
    for nombre in diccionario: valores.append(diccionario[nombre])
    valores_ordenados=sorted(valores,reverse=mayor_a_menor)
    m=[]
    for valor in valores_ordenados:
        for nombre in copia_dic:
            if copia_dic[nombre] == valor:
                m.append([nombre,valor])
                del copia_dic[nombre]
                break
    return m

def lista_de_ints(lista):
    res=[]
    for elemento in lista: res.append(int(elemento))
    return res

def copia_matriz(m):
    copia=[]
    for fila in m: copia.append(copia_lista(fila))
    return copia

def copia_lista(l):
    copia=[]
    for elemento in l: copia.append(elemento)
    return copia

def copia_dic(d):
    copia=dict()
    for nombre in d:
        copia[nombre]=d[nombre]
    return copia

    
def z_back(alfa,beta,zc,Zins,indf,vectorD,zgen,dfinal): #todas las distancias,etc. en mm
    #el step se establece a 1 mm
    zl_p=zgen
    dref=vectorD[-1].posicion
    Ksteps=dref-dfinal
    dactual=dref
    dref_act=dref
    j=complex(0+1j)
    gamma=alfa+j*beta
    
    for s in range(1,Ksteps+1):
        dactual-=1
        if vectorD[dactual].esStub: 
            delta_d=dref_act-dactual
            zl_p=zc*((zl_p+zc*complextanh((gamma)*delta_d*1e-3))/(zc+zl_p*complextanh((gamma)*delta_d*1e-3)))
            if dactual != dfinal: 
                zl_p = 1/((1/zl_p)+(1/Zins['stub'+str(vectorD[dactual].indiceStub)][indf]))
                
            dref_act=dactual
        else:
            pass
        
    if dactual < dref_act:
        delta_d=dref_act-dactual
        zl_p=zc*((zl_p+zc*complextanh((gamma)*delta_d*1e-3))/(zc+zl_p*complextanh((gamma)*delta_d*1e-3)))
        
    return zl_p

def z_front(alfa,beta,zc,Zins,indf,vectorD,zload,dfinal): #todas las distancias,etc. en mm
    #el step se establece a 1 mm
    zl_p=zload
    dref=vectorD[0].posicion
    Ksteps=dfinal-dref
    dactual=dref
    dref_act=dref
    j=complex(0+1j)
    gamma=alfa+j*beta
    
    for s in range(1,Ksteps+1):
        dactual+=1
        if vectorD[dactual].esStub: 
            delta_d=dactual-dref_act
            zl_p=zc*((zl_p+zc*complextanh((gamma)*delta_d*1e-3))/(zc+zl_p*complextanh((gamma)*delta_d*1e-3)))
            zl_p = 1/((1/zl_p)+(1/Zins['stub'+str(vectorD[dactual].indiceStub)][indf]))
            dref_act=dactual
        else:
            pass
        
    if dactual > dref_act:
        delta_d=dactual-dref_act
        zl_p=zc*((zl_p+zc*complextanh((gamma)*delta_d*1e-3))/(zc+zl_p*complextanh((gamma)*delta_d*1e-3)))
        
    return zl_p
    
def step_correcto(lamda,M): #en mm
    step=lamda/M
    while step > 1:
        M+=1
        step=lamda/M
        
    # a partir de aquí, step es <= 1mm
    a=0
    step_p=1/(2**a)
    
    while step_p > step:
        a+=1
        n=2**a
        step_p=1/n
        
    # a partir de aquí, step_p <= step y caben n celdas enteras en 1mm
        
    return step_p # en mm

def esEntero(numero):
    if (numero-int(numero))==0: return True
    else: return False
        
    
def zl_prima(alfa,beta,zc,Zins,indf,vectorD,zl_ref,dref,dfinal,step): #todas las distancias,step,etc. en mm
    #el step ya viene calculado para que Ksteps sea entero.
    #es decir, que entre dfinal y dref quepan Ksteps celdas.
    zl_p=zl_ref
    Ksteps=int((dfinal-dref)/step)
    dactual=dref
    dref_act=dref
    j=complex(0+1j)
    gamma=alfa+j*beta
    
    for s in range(1,Ksteps+1):
        dactual+=step
        if esEntero(dactual):
            dactual=int(dactual)
            if vectorD[dactual].esStub: 
                delta_d=dactual-dref_act
                zl_p=zc*((zl_p+zc*complextanh((gamma)*delta_d*1e-3))/(zc+zl_p*complextanh((gamma)*delta_d*1e-3)))
                zl_p = 1/((1/zl_p)+(1/Zins['stub'+str(vectorD[dactual].indiceStub)][indf]))
                dref_act=dactual
            else:
                pass
        else:
            pass
        
    if dactual > dref_act:
        delta_d=dactual-dref_act
        zl_p=zc*((zl_p+zc*complextanh((gamma)*delta_d*1e-3))/(zc+zl_p*complextanh((gamma)*delta_d*1e-3)))
        
    return zl_p

def ZL_prima(Alfa,Beta,Zc,Zins,F,vectorD,ZL_ref,dref,dfinal,step): #todas las distancias,step,etc. en mm
    ZL_p=[]
    for indf in range(len(F)):
        alfa=Alfa[indf]
        beta=Beta[indf]
        zc=Zc[indf]
        zl_ref=ZL_ref[indf]
        zl_p=zl_prima(alfa,beta,zc,Zins,indf,vectorD,zl_ref,dref,dfinal,step)
        ZL_p.append(zl_p)
        
    return ZL_p

def ZD(Alfa,Beta,Zc,Zins,F,vectorD,ZL,d,step):
    #el step ya viene calculado para que Ksteps sea entero.
    #es decir, que entre dfinal y dref quepan exactamente Ksteps celdas.
    ZV=[]
    Ksteps=int((vectorD[-1].posicion-d)/step)
    
    zv=ZL_prima(Alfa,Beta,Zc,Zins,F,vectorD,ZL,0,d,step)
    ZV.insert(0,zv)
    
    dref=d
    
    for s in range(1,Ksteps+1):
        zv=ZL_prima(Alfa,Beta,Zc,Zins,F,vectorD,zv,dref,dref+step,step)
        ZV.insert(0,zv)
        dref+=step
        
    return ZV

def voltaje(vi,ZDER,indf,F,step,Ksteps,rvf,lvf,gvf,cvf):
    if vi==0: return 0
    
    j=complex(0+1j)
    w=2*pi*F[indf]*1e6 # en rad/s
            
    acum=vi
    
    R=rvf[indf]*step*1e-3 # en Ohm
    L=lvf[indf]*1e-9*step*1e-3 # en  H
    G=gvf[indf]*step*1e-3 # en S
    C=cvf[indf]*1e-12*step*1e-3 # en F
    
    for k in range(1,Ksteps+1):
        aporte=(1/(1+(G+j*w*C+1/ZDER[k-1][indf])*(R+j*w*L)))
        acum*=aporte
        
    return acum



def Voltaje_e_Impedancia(VoltajeGenerador,ImpedanciaGenerador,Alfa,Beta,Zc,rlgc_vs_f,Zins,ZL,F,vectorD,d,step):
    #el step ya viene calculado para que Ksteps sea entero.
    #es decir, que entre dfinal y dref quepan exactamente Ksteps celdas.
    Ksteps=int((vectorD[-1].posicion-d)/step)
    
    rvf=rlgc_vs_f['r']
    lvf=rlgc_vs_f['l']
    gvf=rlgc_vs_f['g']
    cvf=rlgc_vs_f['c']
    
    ZDER=ZD(Alfa,Beta,Zc,Zins,F,vectorD,ZL,d,step)
    Zin=ZL_prima(Alfa,Beta,Zc,Zins,F,vectorD,ZDER[0],vectorD[-1].posicion-step,vectorD[-1].posicion,step)
    
    Vin=[]
    
    Voltaje=[]
    Impedancia=ZDER[-1]
    
    for indf in range(len(F)): 
        vin=(Zin[indf]*VoltajeGenerador[indf])/(Zin[indf]+ImpedanciaGenerador[indf])
        Vin.append(vin)
        v=voltaje(vin,ZDER,indf,F,step,Ksteps,rvf,lvf,gvf,cvf)
        Voltaje.append(v)
    
    
    return Voltaje,Impedancia

def Respuesta_en_Frecuencia(Alfa,Beta,Zc,rlgc_vs_f,Zins,ZL,F,vectorD,step):
    #el step ya viene calculado para que Ksteps sea entero.
    #es decir, que entre dfinal y dref quepan exactamente Ksteps celdas.
    Ksteps=int((vectorD[-1].posicion)/step)
    
    rvf=rlgc_vs_f['r']
    lvf=rlgc_vs_f['l']
    gvf=rlgc_vs_f['g']
    cvf=rlgc_vs_f['c']
    
    ZDER=ZD(Alfa,Beta,Zc,Zins,F,vectorD,ZL,vectorD[0].posicion,step)
    
    H=[]
    
    for indf in range(len(F)): 
        vin=complex(1)
        h=voltaje(vin,ZDER,indf,F,step,Ksteps,rvf,lvf,gvf,cvf)
        H.append(h)
    
    return H
        
        
def generar_step(Beta,M):
    lambda_min=2*pi*1e3/Beta[-1] # en mm
    step=step_correcto(lambda_min,M)

    return step

        
def fase(z): return phase(z)*180/pi

            
def funcion_vista_d(tipo,presentacion,VoltajeGenerador,ImpedanciaGenerador,
                    Alfa,Beta,Zc,rlgc_vs_f,Pmax,
                    datosStubs,Zins,DCA,DGA,
                    ZL,F,vectorD,d,M):
        
    step=generar_step(Beta,M)
    
    ### Respuesta en Frecuencia
    if tipo=='Respuesta en frecuencia':
        resp=[]
        H=Respuesta_en_Frecuencia(Alfa,Beta,Zc,rlgc_vs_f,Zins,ZL,F,vectorD,step)
        
        for i in range(len(F)): 
            if presentacion=='Magnitud': 
                resp.append(abs(H[i]))
                
            elif presentacion=='Fase': 
                resp.append(fase(H[i]))
                
            elif presentacion=='Parte real': 
                resp.append(H[i].real)
                
            elif presentacion=='Parte imaginaria': 
                resp.append(H[i].imag)
                
        return resp
    
    ### Potencia
    elif tipo=='Potencia activa promedio':
        
        V,Z = Voltaje_e_Impedancia(VoltajeGenerador,ImpedanciaGenerador,Alfa,Beta,Zc,rlgc_vs_f,Zins,ZL,F,vectorD,d,step)
        P=[]

        for i in range(len(F)):
            z=complex(Z[i])
            P.append((1/2)*(abs(V[i])**2)*(1/(z.conjugate())).real)
        return P
        
    ### Coeficiente de Reflexión
    elif tipo=='Coeficiente de reflexión':
        
        if d==vectorD[-1].posicion: Zback=ImpedanciaGenerador
        else: Zback=Zc
        
        G=[]
        for i in range(len(F)):
            alfa=Alfa[i]
            beta=Beta[i]
            zc=Zc[i]
            zl=ZL[i]
            zback=Zback[i]
            
            zfront=z_front(alfa,beta,zc,Zins,i,vectorD,zl,d)
        
            num=zfront-zback
            den=zfront+zback
            if den==0: den=1e-16 #0.00000000000000001 es la mayor precisión para el coeficiente de reflexión
            gamma=num/den
            
            if presentacion=='Magnitud': 
                G.append(abs(gamma))
                
            elif presentacion=='Fase':
                G.append(fase(gamma))
                
            elif presentacion=='Parte real': 
                G.append(gamma.real)
                
            elif presentacion=='Parte imaginaria': 
                G.append(gamma.imag)
                
        return G
                
    ### VSWR
    elif tipo=='ROEV':
        
        if d==vectorD[-1].posicion: Zback=ImpedanciaGenerador
        else: Zback=Zc
        
        VSWR=[]
        for i in range(len(F)):
            alfa=Alfa[i]
            beta=Beta[i]
            zc=Zc[i]
            zl=ZL[i]
            zback=Zback[i]
            
            zfront=z_front(alfa,beta,zc,Zins,i,vectorD,zl,d)
        
            num=zfront-zback
            den=zfront+zback
            if den==0: den=1e-16 #0.00000000000000001 es la mayor precisión para el coeficiente de reflexión
            g=abs(num/den)
            if g==1.0: g = 1-1e-16 #0.00000000000000001 es la mayor precisión para el coeficiente de reflexión
        
            swr=(1+g)/(1-g)
            VSWR.append(swr)
            
        return VSWR
    
    ### Impedancia Vista
    elif tipo=='Impedancia vista':
        
        Z=[]
        for i in range(len(F)):
            alfa=Alfa[i]
            beta=Beta[i]
            zc=Zc[i]
            zl=ZL[i]
        
            z=z_front(alfa,beta,zc,Zins,i,vectorD,zl,d)
                    
            if presentacion=='Magnitud': 
                Z.append(abs(z))
                
            elif presentacion=='Fase': 
                Z.append(fase(z))
                
            elif presentacion=='Parte real': 
                Z.append(z.real)
                
            elif presentacion=='Parte imaginaria': 
                Z.append(z.imag)
                
        return Z
        
    
def perdida_Zo(zg,zin): 
    A=(1/(zg.conjugate())).real
    B=abs((zin)/(zg+zin))**2
    C=(1/(zin.conjugate())).real
    
    return 10*log10((A)/(4*B*C))

def perdida_conj(zg,zin): 
    A=(abs(zg)**2)/((zg.real)**2)
    B=(1/(zg)).real
    C=abs((zin)/(zg+zin))**2
    D=(1/(zin.conjugate())).real
    
    return 10*log10((A*B)/(4*C*D))

def mod_Gamma(ImpedanciaGenerador,Alfa,Beta,Zc,Zins,vectorD,ZL,F,d):
    
    if d==vectorD[-1].posicion: Zback=ImpedanciaGenerador
    else: Zback=Zc
    
    G=[]
    for i in range(len(F)):
        alfa=Alfa[i]
        beta=Beta[i]
        zc=Zc[i]
        zl=ZL[i]
        zback=Zback[i]
        
        zfront=z_front(alfa,beta,zc,Zins,i,vectorD,zl,d)
    
        num=zfront-zback
        den=zfront+zback
        if den==0: den=1e-16 #0.00000000000000001 es la mayor precisión para el coeficiente de reflexión
        gamma=num/den
        
        G.append(abs(gamma))
                        
    return G

def complex_Z(Alfa,Beta,Zc,Zins,vectorD,ZL,F,d):
    Z=[]
    for i in range(len(F)):
        alfa=Alfa[i]
        beta=Beta[i]
        zc=Zc[i]
        zl=ZL[i]

        z=z_front(alfa,beta,zc,Zins,i,vectorD,zl,d)
        Z.append(z)
        
    return Z

def fase_H_rad(Alfa,Beta,Zc,rlgc_vs_f,Zins,ZL,F,vectorD,M):
        
    step=generar_step(Beta,M)
    
    resp=[]
    H=Respuesta_en_Frecuencia(Alfa,Beta,Zc,rlgc_vs_f,Zins,ZL,F,vectorD,step)
    
    for i in range(len(F)): resp.append(phase(H[i]))
            
    return resp

def esSalto(g_ant,g):
    factor=0.9 #porcentaje de 360° para considerar que ocurre un salto.
    # idealmente un salto es de 360° exactos.
    if abs(g-g_ant)>=2*pi*factor: return True
    else: return False

def GroupDelay(Fase,F):
    resp=[]
    for indf in range(len(F)):
        if indf==0:
            if esSalto(Fase[indf],Fase[indf+1]):
                resp.append(None)
            else:
                t=-1*(Fase[indf+1]-Fase[indf])/((F[indf+1]-F[indf])*1e6*2*pi) # en s
                resp.append(t)
        
        elif indf>0 and indf<(len(F)-1):
            if esSalto(Fase[indf-1],Fase[indf]) or esSalto(Fase[indf],Fase[indf+1]):
                resp.append(None)
            else:
                t=-1*(Fase[indf+1]-Fase[indf-1])/((F[indf+1]-F[indf-1])*1e6*2*pi) # en s
                resp.append(t)
            
        elif indf==(len(F)-1):
            if esSalto(Fase[indf-1],Fase[indf]):
                resp.append(None)
            else:
                t=-1*(Fase[indf]-Fase[indf-1])/((F[indf]-F[indf-1])*1e6*2*pi) # en s
                resp.append(t)
                
    return resp

def PhaseDistortion(Group_Delay,F):
    Group_Delay_beta=[]
    F_beta=[]
    #muestreo

    for i in range(len(F)):
        if Group_Delay[i] is not None: 
            Group_Delay_beta.append(Group_Delay[i])
            F_beta.append(F[i])
            
    T=polyfit(F_beta,Group_Delay_beta,0)[0]
    acum=0
    for i in range(len(F_beta)): acum+=abs((Group_Delay_beta[i]-T)/(T))
    
    return (acum/len(F_beta))*100


def perdida_Zo_fo(ImpedanciaGenerador,Zdin,F):
    indfo=int((len(F)-1)/2)
    zg=complex(ImpedanciaGenerador[indfo])
    zin=complex(Zdin[indfo])

    return perdida_Zo(zg,zin)

def max_perdida_Zo(ImpedanciaGenerador,Zdin,F):
    max_loss=-1*Infinity
    ind_max=0
    
    for indf in range(len(F)):
        zg=complex(ImpedanciaGenerador[indf])
        zin=complex(Zdin[indf])
        loss=perdida_Zo(zg,zin)
        
        if loss > max_loss: 
            max_loss=loss
            ind_max=indf
    
    return max_loss, F[ind_max]

def perdida_conj_fo(ImpedanciaGenerador,Zdin,F):
    indfo=int((len(F)-1)/2)
    zg=complex(ImpedanciaGenerador[indfo])
    zin=complex(Zdin[indfo])

    return perdida_conj(zg,zin)

def max_perdida_conj(ImpedanciaGenerador,Zdin,F):
    max_loss=-1*Infinity
    ind_max=0
    
    for indf in range(len(F)):
        zg=complex(ImpedanciaGenerador[indf])
        zin=complex(Zdin[indf])
        loss=perdida_conj(zg,zin)
        
        if loss > max_loss: 
            max_loss=loss
            ind_max=indf
        
    return max_loss, F[ind_max]

def distorsion_fase(H_rad,F):
    Retardo_Grupo=GroupDelay(H_rad,F)
    dist=PhaseDistortion(Retardo_Grupo,F)
    return dist

def rizado(Gamma_adp,F):
    maximo=-1*Infinity
    minimo=Infinity
    
    for indf in range(len(F)):
        if Gamma_adp[indf]>maximo: maximo=Gamma_adp[indf]
        if Gamma_adp[indf]<minimo: minimo=Gamma_adp[indf]
        
    return maximo-minimo

def gamma_fo(Gamma_adp,F):
    indfo=int((len(F)-1)/2)
    return Gamma_adp[indfo]

def max_gamma(Gamma_adp,F):
    maximo=-1*Infinity
    indf_max=0
    for indf in range(len(F)):
        if Gamma_adp[indf]>maximo: 
            maximo=Gamma_adp[indf]
            indf_max=indf
            
    return maximo, F[indf_max]

def adaptacion_gamma(Gamma_adp,F):
    acum=0
    N=len(F)
    for indf in range(N): acum+=Gamma_adp[indf]
    
    return (1-(acum)/(N))*100

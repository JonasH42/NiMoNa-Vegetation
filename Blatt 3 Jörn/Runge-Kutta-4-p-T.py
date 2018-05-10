#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 18:08:47 2018

@author: jsieveneck
"""
import numpy as np
import matplotlib.pyplot as plt


#Definiere Funktion
def f(population,t):
    p1,p2=population
    epsilon1 = 2.
    epsilon2 = 0.8
    gamma1 = 0.2
    gamma2 = 0.0002
    return np.array([ p1*(epsilon1-gamma1*p2) , -p2*(epsilon2 - gamma2*p1) ]) 

#Definiere RK4
def rk4(f,Tende,p_0):
    x = p_0 
    h=0.025 
    t=0
    plt.plot(t,x[0],'b.')
    plt.plot(t,x[1],'r.')
    while t<=Tende:              
        k1 = f( x, t )
        k2 = f( x + 0.5 * h * k1, t + 0.5 * h ) 
        k3 = f( x + 0.5 * h * k2, t + 0.5 * h )  
        k4 = f( x + h * k3, t + h  )
        x = x + h * ( ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0 )
        t=t+h
        plt.plot(t,x[0],'b.')
        plt.plot(t,x[1],'r.')
        
    
#Anfangspopulation
p1_0 = 200
p2_0 = 20
p_0=[p1_0,p2_0]
#Zeitraum
T=20
#Schrittweite
h=0.025

plt.xlabel('Zeit')
rk4(f,T,p_0)
plt.ylabel('Populationsgröße')
plt.legend(('p1 (Beute)','p2 (Räuber)'),loc=2)
plt.show()

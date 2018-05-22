#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 18:11:51 2018

@author: jsieveneck
"""

import numpy as np
import matplotlib.pyplot as plt

 #Definiere Funktion als array
def f(population,t):
    p1,p2=population
    epsilon1 = 2.
    epsilon2 = 0.8
    gamma1 = 0.02
    gamma2 = 0.0002
    return np.array([ p1*(epsilon1-gamma1*p2) , -p2*(epsilon2 - gamma2*p1) ]) 

#Definiere Runge-Kuta 4 Verfahren 
def rk4(Tende,p_0):
    x = p_0 
    h=0.025 
    t=0
    plt.plot(x[0],x[1],'b.')
    while t<=Tende:              
        k1 = f( x, t )
        k2 = f( x + 0.5 *  k1, t + 0.5 * h ) 
        k3 = f( x + 0.5 *  k2, t + 0.5 * h )  
        k4 = f( x + k3, t + h  )
        x = x + h * ( ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0 )
        t=t+h
        plt.plot(x[0],x[1],'b.')
        
    
#Anfangspopulation
p1_0 = 200.
p2_0 = 20.
p_0=[p1_0,p2_0]
#Zeitspanne in Jahren
T=20
#Schrittweite
h=0.025
plt.xlabel('Population Beute')
rk4(20,p_0)
plt.ylabel('Population Räuber')
plt.show()

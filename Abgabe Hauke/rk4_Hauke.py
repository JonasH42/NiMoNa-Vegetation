# -*- coding: utf-8 -*-
"""
Created on Wed May 16 17:09:11 2018

@author: hauke
"""
# Das Programm hat noch einen Mathematischen Fehler in der Umsetzung, sodass die Loesungen
# nicht die erwartete Oszillation wiedergeben. ich sehe mir das ueber Pfingsten nochmal an. 
import numpy as np
import matplotlib.pyplot as plt

#def Anfangswerte
t0=0
tend=1
#parameter
e1=2.9
e2=0.8
y1=0.02
y2=2e-4
h=0.025
p1=9
p2=9
t=t0
#butcher
c1=1/6
c2=1/3
c3=1/3
c4=1/6
#def Funktionen
p=[p1,p2]

def f(t,p,E1=e1,E2=e2,Y1=y1,Y2=y2):
    return np.array([p[0]*(E1-Y1*p2),-p[1]*(E2-Y2*p2)])



#berechne kj
while(t<tend):
    k1=f(t,p)
    k2=f(t+h/2,p+h/2*k1)
    k3=f(t+h/2,p+h/2*k2)
    k4=f(t*h,p+h*k3)
    k=[k1,k2,k3,k4]
    #nächster numerischer schritt
    p=p+h*(c1*k1+c2*k2+c3*k3+c4*k4)
    plt.plot(t,p[0],'k.')
    plt.plot(t,p[1],'r.')
    print(t,p[0],p[1])#zur kontrolle 
    t=t+h
plt.savefig('Räuber-Beute.pdf')
plt.show()

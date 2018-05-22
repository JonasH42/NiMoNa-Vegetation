
# coding: utf-8

# In[15]:


import numpy as np
import matplotlib.pyplot as plt

#Angaben
Tend=50
h=0.025

#Anfangswerte
p10 = 1000
p20 = 20
p0=[p10,p20]

def rb(bestände,t):
    p1,p2=bestände
    return np.array([ p1*(2.0-0.02*p2) , -p2*(0.8 - 0.0002*p1) ]) 

def rungekutta(rb,Tend,p0):
    p = p0  
    t=0
    plt.plot(p[0],p[1],'b.') 
    while t<=Tend:              
        k1 = rb(p,t)
        k2 = rb(p+0.5*h*k1,t+0.5*h) 
        k3 = rb(p+0.5*h*k2,t+0.5*h)  
        k4 = rb(p+h*k3,t+h)
        p = p+h/6*((k1+2*(k2+k3)+k4))
        t=t+h
        plt.plot(p[0],p[1],'b.')

#Plot Befehle
plt.xlabel('Räuber')
rungekutta(rb,Tend,p0)
plt.ylabel('Beute')
plt.show()
    


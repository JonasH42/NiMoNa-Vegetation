import numpy as np
import matplotlib.pyplot as plt

def fP1(p1,p2,a,b):
    return (p1*(a - b*p2))

def fP2(p1,p2,c,d):
    return (-p2*(c - d*p1)) #return bedeutet sowas wie das er es wieder zurückschmeißt
                            #mit return kann ich mit der Funktion weiter rechnen
#Definiere Größen
N_t = 4860
h = 0.025
a = 2
b = 0.02
c = 0.8
d = 0.0002

p1=np.zeros(N_t)
p2=np.zeros(N_t)
t =np.zeros(N_t)

#Es ist nötig beide Anfangswerte p1 und p2 vor zu geben
p1[0] = 200
p2[0] = 20
t[0] = 0

for i in range(1,N_t):#läuft von 1 bis obere Rekursionszahl
    k1 = fP1(p1[i-1] , p2[i-1] , a , b)
    k11 = fP2(p1[i-1] , p2[i-1] , c , d)
    
    
    k2 = fP1(p1[i-1] + h/2.0*k1 , p2[i-1] +h/2*k11, a , b)
    k22 = fP2(p1[i-1] +h/2*k1, p2[i-1] + h/2.0*k11 , c , d)
    
    
    k3 = fP1(p1[i-1] + h/2.0*k2 , p2[i-1]+h/2*k22 , a , b)
    k33 = fP2(p1[i-1]+h/2*k2 , p2[i-1] + h/2.0*k22 , c , d)
    
    
    k4 = fP1(p1[i-1] + h*k3 , p2[i-1]+h*k33 , a , b)
    k44 = fP2(p1[i-1]+h*k3 , p2[i-1] + h*k33 , c , d)
    
    
    p1[i] = p1[i-1] + h/6.0*(k1 + 2.0*k2 + 2.0*k3 + k4)
    p2[i] = p2[i-1] + h/6.0*(k11 + 2.0*k22 + 2.0*k33 + k44)
    t[i] = t[i-1] + h

plt.plot(p1,p2)
plt.plot(t,p1)
plt.plot(t,p2)
plt.show()

#plt.savefig("Räuber + Beute.png")

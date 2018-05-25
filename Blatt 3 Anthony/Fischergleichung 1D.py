#Fischer Gleichung in 1D
import numpy as np
import matplotlib.pyplot as plt



#Definitionen
def rk4(nk,k,gammar,sigma,mu,h):
    k_1 = DGL(nk,k,gammar,sigma,mu)
    k_2 = DGL(nk + h/2*k_1,k,gammar,sigma,mu)
    k_3 = DGL(nk + h/2*k_2,k,gammar,sigma,mu)
    k_4 = DGL(nk + h*k_3,k,gammar,sigma,mu)
    nk = nk + h/6*(k_1 + 2*(k_2 + k_3) + k_4)
    return nk

#Benötigen unsere DGL mit nk ist n im k-Raum
def DGL(nk,k,gammar,sigma,mu):
    return (gammar/sigma - mu)*nk - np.fft.fft(np.fft.ifft(nk)*np.fft.ifft(nk)) - k**2*nk

#Anfangsbedingungen
def n_0(x,L_x):
    return 0.2*np.exp(-(x-L_x/2)**2/0.5)



#Parameter
N_t = 2000
N_x = 256
h = 0.005
L_x = 4*np.pi
mu = 0.01
gammar = 1
sigma = 1

#Funktionen in denen Werte reingeschrieben werden
T = np.arange(N_t)*h
nk = np.zeros((N_t,N_x))

#Räume und deren Gestalt
x = np.arange(N_x)*L_x/N_x
k = np.fft.fftfreq(N_x,L_x/(N_x*2*np.pi))

#Bezug auf Anfansdaten
nk[0] = n_0(x,L_x)



#Berechnen/ Prinzip des Pseudospektralverfahrens
for i in range(1,N_t):
    n = np.fft.fft(nk[i-1])
    nk_new = rk4(n,k,gammar,sigma,mu,h)
    nk[i] = np.fft.ifft(nk_new)



#Plotten
plt.ion() 
for i in range(N_t):
    #if i%10 == 0:#Modulo somit Bewegung
        plt.cla()
        plt.plot(x,nk[i])#Ortsbewegung
        plt.draw()
        plt.pause(1)
        
        
#Ende

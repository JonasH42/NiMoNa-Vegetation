import numpy as np
import matplotlib.pyplot as plt
#import time

#Anfangsbedingungen
gamma_sigma = 1.
mu = 0.01
h = 0.005
L = np.array([4 * np.pi, 4 * np.pi])
N = np.array([256,256])
Tend = 100
D_n=0.01

def rk4(n,k,h):
    k1 = f(n,k)
    k2 = f(n+h/2*k1,k)
    k3 = f(n+h/2*k2,k)
    k4 = f(n+h*k3,k)
    return n + h/6*(k1+2.*k2+2.*k3+k4)

def f(n,k):
    return -D_n*k**2*n+(gamma_sigma - mu)*n- np.fft.fft(np.fft.ifft(dealiasing(n))**2)

def n_init(x,L):
    return 0.2*np.exp( ((x[0]-L[0]/2.0)**2 + (x[1]-L[1]/2.0)**2)/-0.5)

def dealiasing(n):
    kmax = max(k)
    for i in range(len(n)):
        if k[i] > 2./3.*kmax :
            n[i] = 0
    return n


N_t = int(Tend/h)
    
k = np.fft.fftfreq(N[0],L[0]/(N[0]*2*np.pi))
T = np.arange(N_t)*h
    
x = np.arange(N[0])*L[0]/N[0]
y = np.zeros(N[1]) + L[1]/2.
n = np.zeros((N_t,N[0]))
n[0] = n_init([x,y],L)
    
for i in range(1,N_t):
    nk = np.fft.fft(n[i-1])
    nk_new = rk4(nk,k,h)
    n[i] = np.fft.ifft(nk_new).real
        

plt.ion()
plt.show()
for i in range(100):
    #if i%10 == 0:
        plt.cla()
        plt.plot(x,n[i])
        plt.draw()
        plt.pause(0.1)
        
plt.ioff

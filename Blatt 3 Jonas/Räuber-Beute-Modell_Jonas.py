import numpy as np
import matplotlib.pyplot as plt

class RBM:
    
    def __init__(self):
        NaN = np.NaN
        self.h = 0.025
        self.N_t = 4900
        self.eps1 = 2.
        self.eps2 = 0.8
        self.gamma1 = 0.02
        self.gamma2 = 0.0002 
        self.s = 4
        self.a = [0.0,0.5,0.5,1.0]
        self.b = [1/6.,1/3.,1/3.,1/6.]
        self.c  = [[NaN,NaN,NaN,NaN],
                   [1/2.,NaN,NaN,NaN],
                   [0.0,1/2.,NaN,NaN], 
                   [0.0,0.0,1.,NaN]]



    def P1(self,p1,p2):
        return(p1*(self.eps1-self.gamma1*p2))

    def P2(self,p2,p1):
        return(-p2*(self.eps2-self.gamma2*p1))

    def kj(self,f,x,x2,j,k):
        summe = 0.
        for i in range(0,j):
            summe = summe + self.h*self.c[j][i]*k[i] 
    
        return f(x + summe,x2) 
    
    
    def run(self):
        p1 = [200.]
        p2 = [20.]
        t = [0.]
        for i in range(0,self.N_t):
            k1 = []
            k2 = []
            t.append(t[len(t)-1]+self.h)
            for j in range(0,self.s):
                k1.append(self.kj(self.P1,p1[i],p2[i],j,k1))
                k2.append(self.kj(self.P2,p2[i],p1[i],j,k2))
            
            p1_temp = p1[i]
            p2_temp = p2[i]
            for m in range(0,len(k1)):
                p1_temp = p1_temp + self.h*self.b[m]*k1[m]
                p2_temp = p2_temp + self.h*self.b[m]*k2[m]
            
            p1.append(p1_temp)
            p2.append(p2_temp)
        return p1,p2,t
#Schrittweite




rbm = RBM()
p1,p2,t = rbm.run()
#plt.plot(p1,p2)
plt.plot(t,p1)
#plt.plot(t,p2)
plt.show()
    

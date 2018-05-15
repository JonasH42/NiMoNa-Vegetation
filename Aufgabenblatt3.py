#   (d/dt)*p1 = p1*(E1-g1*p2)      (d/dt)*p2 = -p2*(E2-g2*p1)
#   p1 und p2 sind die Raeuber bzw. Beute Population
#   g1 und g2 sind Faktoren, wie sehr eine Population von der jew. anderen beeinflusst wird. So kann zB beschrieben werden, dass sich Woelfe zu 60% von Schafen ernaehren.
#   E1 und E2 sind andere Faktoren, die das Wachstum einer Pop. beeinflussen

#   x(t+h) = x(t) + h* Sum^s_i=1 (c_i * k_i)
#   k_j = f(x + h*sum^j-1_i=1(b_ji * k_i) , t + a_i * h)

import matplotlib.pyplot as plt
import numpy as np

E1 = 2.0
E2 = 0.8
g1 = 0.02
g2 = 0.0002
h = 0.025

data=np.array([[100], [100]])      #Populationsize 1 and 2
timeline = [0]     #for storing time data, the first value is the starting time t0

def k1(f, t, x):
    return f(t, x)


def k2(f, t, x):
    return f(t + h/2, x + h/2 * k1(f, t, x))


def k3(f, t, x):
    return f(t + h/2, x + h/2 * k2(f, t, x))

def k4(f, t, x):
    return f(t + h, x + h * k3(f, t, x))


def rk4(f, t, x):
    return x + h * (k1(f, t, x)/6 + k2(f, t, x)/3 + k3(f, t, x)/3 + k4(f, t, x)/6)


def popGrowth(t, x):
    return np.array([[   x[0][-1] *(E1-g1*x[1][-1])    ],
                    [   -x[1][-1]*(E2-g2*x[0][-1])   ]])


for n in range(0, 1500):
    timeline.append(timeline[-1]+h)
    data = np.append(data, rk4(popGrowth, timeline[-1], [[data[0][-1]], [data[1][-1]]]), axis=1)

plt.subplot(211)
plt.ylabel('population sizes')
plt.xlabel('t')
plt.plot(data[0])
plt.plot(data[1])
plt.subplot(212)
plt.ylabel('Beutetiere')
plt.xlabel('Raubtiere')
plt.plot(data[1], data[0])

plt.show()

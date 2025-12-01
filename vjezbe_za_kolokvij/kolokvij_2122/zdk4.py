import numpy as np  
import matplotlib.pyplot as plt             
import math as mt
#import polint as polint
from scipy . interpolate import CubicSpline
H = [0,50,100,150,200,250,300]
B=[0,0.2,0.75,1.2,1.4,1.48,1.5]
n=len(H)
Pl=[]
X=np.linspace(0,300,100)
for x in X:
    s=0
    for i in range(n):
        L=1
        for j in range(n):
            if j!=i:
                L*=(x - H[j])/(H[i]-H[j])
        s+=B[i]*L 
    Pl.append(s)
cs=CubicSpline(H, B,bc_type='natural')
Y_cs=cs(X)
plt.figure()
plt.plot(X, Pl, color='red',markersize=2, label='Lagrange')
plt.plot(X, Y_cs, color='blue',markersize=2, label='CubicSpline')
plt.plot(H, B,linestyle='none', marker='o', markerfacecolor='none', markeredgecolor='black', markeredgewidth=1, label='(H_{i},B_{i})', alpha=1)
plt.xlabel('H/[A/m]')
plt.ylabel('B/[T]')
plt.legend()
plt.title('Magnetizacija feromagneta')
plt.grid(True)
plt.show()

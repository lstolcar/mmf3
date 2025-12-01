import numpy as np  
import matplotlib.pyplot as plt             
import math as mt
from scipy . interpolate import CubicSpline
def f():
    y_lista=[]
    x_lista=np.linspace(-5,0,100)
    x_inter=[-5,-4.7,-1.25,-0.01]
    for x in x_inter:
        funk=1/(mt.sqrt(1-x))
        y_lista.append(funk)
    cs=CubicSpline(x_inter,y_lista,bc_type='natural')
    Y_cs=cs(x_lista)
    plt.figure()
    plt.plot(x_lista, Y_cs, color='red',markersize=8, label='CubicSpline')
    plt.scatter(x_inter, y_lista, color='green',marker='o', label='točke interpolacije',s=50)
    plt.xlabel('x') 
    plt.ylabel('f(x)')
    plt.legend()  
    plt.title('Interpolacija funkcije f(x)=1/sqrt(1-x)')
    plt.grid(True)  
    plt.show()  
f()
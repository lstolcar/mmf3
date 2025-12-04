import numpy as np
import math as mt
import matplotlib.pyplot as plt
import polint as polint
from scipy . interpolate import CubicSpline


def f():
    y_lista=[]
    for i in np.linspace(0,1.5,100):
        y_lista.append(i*(i+5)+np.sin(10*i))
    plt.figure()
    plt.plot(np.linspace(0,1.5,100), y_lista, color='red',markersize=8, label='f')
    plt.xlabel('x') 
    plt.ylabel('f')
    plt.legend()  
    plt.title('f')
    plt.grid(True)  
    plt.show() 
def cubic():
    iks=np.linspace(0,1.5,11)
    y_lista=[]
    for i in np.linspace(0,1.5,11):
        y_lista.append(i*(i+5)+np.sin(10*i))

    cs=CubicSpline(iks,y_lista,bc_type="natural")
    X_cs=np.linspace(0,1.5,61)
    Y_cs=cs(X_cs)
    Y=[]
    dY=[]
    dYabs=[] 
    iks=np.linspace(0,1.5,11)
    y_lista=[]
    x=np.linspace(0,1.5,61)

    for i in np.linspace(0,1.5,11):
        y_lista.append(i*(i+5)+np.sin(10*i))

    for x_ in x:
        yN, dy = polint.polint(iks, y_lista, len(iks),x_)
        Y.append(yN)
        dY.append(dy)
        dYabs.append(abs(dy))
    plt.figure()
    plt.plot(x,Y,color='red')
    plt.errorbar(x, Y, yerr=dYabs, fmt='o', markerfacecolor='red', markeredgecolor='blue', ecolor='blue',markersize=3, capsize=0.5, label='Neville')
    plt.plot(X_cs, Y_cs, color='yellow',markersize=3, label='CubicSpline')    
    plt.legend() 
    plt.grid(True)
    plt.show()


cubic()

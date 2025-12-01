import numpy as np
import math as mt       
import matplotlib.pyplot as plt
def bessel(n):
    lista_bessel=[]
    for x in np.arange(4,8,0.01):
        J0=np.sin(x)/x
        J1=(np.sin(x)/x**2)-(np.cos(x)/x)
        for i in range(2,n+1):
            J=((2*(i-1)+1)/x)*J1 - J0
            J0=J1
            J1=J
        lista_bessel.append(J)
    print(len(lista_bessel))
    print(len(np.arange(4,8,0.01)))
    plt.plot(np.arange(4,8,0.01),lista_bessel)
    plt.title("Besselova funkcija prvog reda")  
    plt.xlabel("x")
    plt.ylabel("J_n(x)")
    plt.grid(True)
    plt.show()

bessel(10)
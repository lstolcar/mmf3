import numpy as np
import math as mt   
import matplotlib.pyplot as plt

def hermit(x=10,n=10):
    H0=1
    H1=2*x
    lista_hermit=[H0,H1]
    for i in range(2,n+1):
        H=2*x*lista_hermit[i-1]-2*(i-1)*lista_hermit[i-2]
        lista_hermit.append(H)
    return(H)
def derivacijacentralna(f,x,n=10,h1=0.1,h2=0.001):
     print("Centralna za h=0.1,={}".format( (f(x + h1) - f(x - h1)) / (2 * h1) ))
     print("Centralna za h=0.001,={}".format( (f(x + h2) - f(x - h2)) / (2 * h2) ))  

def derivacijaunaprijed(f,x,n=10,h1=0.1,h2=0.001):
     print("Unaprijed za h=0.1,={}".format( (f(x + h1) - f(x)) / h1))
     print("Unaprijed za h=0.001,={}".format( (f(x + h2) - f(x)) / h2))  




#hermit()
derivacijacentralna(hermit,10)
derivacijaunaprijed(hermit,10)
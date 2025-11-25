import numpy as np  
import matplotlib.pyplot as plt             
import math as mt
def maxwell(N=50,interval=25,m=3.37e-26,T=300,vm=559.4,):
    k=1.38064852e-23
    c=m/(2*k*T)
    a=vm-interval
    b=vm+interval
    h=(b-a)/N
    integral=0
    for v in np.arange(a,b+h,h):
        f=(4*mt.pi*(c/mt.pi)**(3/2))*v**2*mt.exp(-c*v**2)
        if v==a or v==b:
            integral+=f*h/2
        else:
            integral+=f*h
    print('Preko trapeza:',integral*100,'%')
maxwell()
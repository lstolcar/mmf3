import numpy as np  
import matplotlib.pyplot as plt             
import math as mt
import gl
def maxwell(N,interval=50,m=3.37e-26,T=300,vm=559.4,):
    k=1.38064852e-23
    c=m/(2*k*T)
    a=0
    b=vm
    h=(b-a)/N
    integral=0
    
    for v in np.arange(a,b+h,h):
        f=(4*mt.pi*(c/mt.pi)**(3/2))*v**2*mt.exp(-c*v**2)
        if v==a or v==b:
            integral+=f*h/2
        else:
            integral+=f*h
    print('Preko trapeza:',integral*100,'%, sa N=',N)

    integral1=0
    count=0
    for p in np.arange(a,b+h,h):
        funkcija=(4*mt.pi*(c/mt.pi)**(3/2))*p**2*mt.exp(-c*p**2)
        if p==a or p==b:
            integral1+=funkcija
            count=count+1
        else:
            if count%2==0:
                integral1+=2*funkcija
            elif count%2!=0:
                integral1+=4*funkcija
            count=count+1
    integral_ = (integral1) * (h/3)
    print('Preko Simpsona:',integral_*100,'%, sa N=',N)

    f = lambda v: (4 * mt.pi * (c / mt.pi)**(3/2)) * v**2 * np.exp(-c * v**2)
    x, w = gl.gauleg(a, b, N)
    integral2_ = sum(w * f(x))
    print("Preko Gauss-Legendre", integral2_*100,'%, sa N=',N )
    
maxwell(10)
maxwell(50)
maxwell(100)
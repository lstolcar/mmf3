import numpy as np  
import matplotlib.pyplot as plt             
def maxwell(N,m=3.37e-26,T=300,vm=559.4,):
    a=-0.5
    b=2
    h=(b-a)/N
    integral=0

    
    for x in np.arange(a,b+h,h):
        f=np.exp(x)+x**5
        if x==a or x==b:
            integral+=f*h/2
        else:
            integral+=f*h
    print('Preko trapeza:',integral,'kg, sa N=',N)

    integral1=0
    count=0
    for p in np.arange(a,b+h,h):
        funkcija=f=np.exp(p)+p**5
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
    print('Preko Simpsona:',integral_,'kg, sa N=',N)

    analiticko=17.44659
    print('Analiticko rješenje:', analiticko,'kg')
    dif_t=analiticko-integral
    print('Razlika analiticko-trapez',dif_t)
    dif_S=analiticko-integral_
    print('Razlika analiticko-Simpson',dif_S)

    
maxwell(10)
maxwell(50)
maxwell(100)
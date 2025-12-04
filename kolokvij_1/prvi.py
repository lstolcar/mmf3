import numpy as np
import math as mt
import matplotlib.pyplot as plt

def p():
    y_lista=[]
    for x in np.linspace(-2,0,100):
        y=(1/(1+np.exp(-x)))
        y_lista.append(y)
    plt.figure()
    plt.plot(np.linspace(-2,0,100), y_lista, color='red',markersize=8, label='p_vezano')
    plt.xlabel('x') 
    plt.ylabel('p_vezano')
    plt.legend()  
    plt.title('p')
    plt.grid(True)  
    plt.show()  
def funkcija(x0=-1,epsilon=1e-8,N=1000):
   def pvezano(x):
       return   (1/(1+np.exp(-x)))
   def pvezano_crtica(x):
       return (np.exp(-x)/((1+np.exp(-x))**2))
   c=0
   while c<N:
        time=x0-(pvezano(x0)-0.3)/(pvezano_crtica(x0))
        if abs((pvezano(x0)-0.3)/(pvezano_crtica(x0)))<epsilon:
            break
        x0=time
        c=c+1
   print(f"Broj iteracija: {c}")       
   print(f"Priblizna vrijednost x-a: {time}")
   L=(1+time)/2
   print('[L]={}'.format(L) )
   return c, time
  
p()
funkcija()
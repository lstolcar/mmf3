import numpy as np
import math as mt
import matplotlib.pyplot as plt 

def sudar(y01,y02,A,B,C,D,a,b,N,epsilon,t0=2.1):
    def y1(t):
        return y01+A*np.cos(B*t)
    def y2(t):
        return y02+C*np.exp(D*t)   
    counter=0
    while counter<N:
        c=(a+b)/2
        if y1(c)-y2(c)<epsilon:
            b=c
        else:
            a=c
        if abs(y1(c)-y2(c))<epsilon or abs(b-a)<epsilon:
            break
        counter+=1
    print(f"Broj iteracija: {counter}") 
    print(f"Priblizna vrijednost sudara(bisekcija): {c}")
    def y1_crtica(t):
        return -A*B*np.sin(B*t)
    def y2_crtica(t):
        return C*D*np.exp(D*t)
    c=0
    
    while c<N:
        time=t0-(y1(t0)-y2(t0))/(y1_crtica(t0)-y2_crtica(t0))
        if (y1(t0)-y2(t0))/(y1_crtica(t0)-y2_crtica(t0))<epsilon:
            break
        t0=time
        c=c+1
    print(f"Broj iteracija: {c}")       
    print(f"Priblizna vrijednost sudara(NR): {time}")
    return c, time  

_, t_sudar = sudar(5,0.325,1,3,2,0.5,0,2.5,200,1e-8)



y01, y02, A, B, C, D = 5, 0.325, 1, 3, 2, 0.5

def y1(t):
    return y01 + A*np.cos(B*t)

def y2(t):
    return y02 + C*np.exp(D*t)

t = np.linspace(0, 5, 400)
plt.plot(t, y1(t), label='y1(t) = y01 + A cos(Bt)')
plt.plot(t, y2(t), label='y2(t) = y02 + C exp(Dt)')


plt.scatter(t_sudar, y1(t_sudar), color='red', zorder=5, label='Presjek')

plt.title('Presjek dviju funkcija')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

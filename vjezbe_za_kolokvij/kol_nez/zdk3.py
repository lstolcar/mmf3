import numpy as np
import math as mt           
import matplotlib.pyplot as plt
def f():
    y_lista=[]
    x_lista=[]
    for x in np.arange(0,10,0.001):
        funkcija=np.sin(2*x)-2*np.cos(x)
        y_lista.append(funkcija)
        x_lista.append(x)
    plt.figure()
    plt.plot(x_lista, y_lista, color='blue',markersize=8, label='f(x)')
    plt.xlabel('x')     
    plt.ylabel('f(x)')
    plt.legend()    
    plt.title('Funkcija f(x)=sin(2x)-2cos(x)')
    plt.grid(True)
    plt.show()
def zatvorena_domena(a,b,N,epsilon,h=0.001):  
    def funk(x):
        return np.sin(2*x)-2*np.cos(x)
    fa_1= ((funk(a + h) - funk(a - h)) / (2 * h) )
    fb_1= ((funk(b + h) - funk(b - h)) / (2 * h) )
    c=(a+b)/2
    fc_1=((funk(c+h)-funk(c-h))/(2*h))
    counter=0
    while counter<N:
        if fa_1*fc_1<0:
            b=c
            fb_1=fc_1
        else:
            a=c
            fa_1=fc_1
        if abs(fc_1)<epsilon or abs(b-a)<epsilon:
            break
        c= (a + b) / 2.0
        fc_1 = ((funk(c+h)-funk(c-h))/(2*h))
        counter+=1
    print(f"Broj iteracija: {counter}")
    print(f"Priblizna vrijednost korijena: {c}")
    f_2=((funk(c + h) - 2*funk(c) + funk(c - h)) / (h**2))
    if f_2 < 0:
        print('Broj {} je maksimum'.format(c))
    else:
        print('Broj {} je minimum'.format(c))
def otvorena_domena(x0, N, epsilon, h=0.001):
    def fu(x):
        return np.sin(2*x)-2*np.cos(x)
    counter=0
    while counter<N:
        x=x0-((((fu(x0 + h) - fu(x0 - h)) / (2 * h) ))/((fu(x0 + h) - 2*fu(x0) + fu(x0 - h)) / (h**2)))
        if abs(((((fu(x0 + h) - fu(x0 - h)) / (2 * h) ))/((fu(x0 + h) - 2*fu(x0) + fu(x0 - h)) / (h**2))))<epsilon:
            break
        x0=x
        counter+=1
    print(f"Broj iteracija: {counter}") 
    print(f"Priblizna vrijednost korijena: {x}")

f()
zatvorena_domena(0,2,1000,1e-8)
zatvorena_domena(2,4,1000,1e-8)
zatvorena_domena(4,6,1000,1e-8)
zatvorena_domena(6,8,1000,1e-8)
otvorena_domena(2,200,1e-8)
otvorena_domena(4,200,1e-8)
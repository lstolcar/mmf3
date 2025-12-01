import numpy as np
import math as mt           
import matplotlib.pyplot as plt
def f():
    y_lista=[]
    x_lista=[]
    for x in np.arange(-2,2,0.001):
        funkcija=9*x**4-8*x**2-x-6+10*np.cos(2*x)
        y_lista.append(funkcija)
        x_lista.append(x)
def zatvorena_domena(a,b,N,epsilon,h=0.001):  
    def funk(x):
        return 9*x**4-8*x**2-x-6+10*np.cos(2*x)
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
        

zatvorena_domena(-2,-0.5,1000,1e-8)
zatvorena_domena(-0.5,0.5,1000,1e-8)
zatvorena_domena(0.5,2,1000,1e-8)
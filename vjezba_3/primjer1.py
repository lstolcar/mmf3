import numpy as np
import matplotlib.pyplot as plt                 

def metoda_zatvorene_domene(a,b,N,epsilon):
    def f(x):
        return 7*(x**2) + 15*x - 32
    fa = f(a)
    fb = f(b)
    c= (a + b) / 2.0
    fc = f(c)   
    counter=0
    while counter<N:
        if fa*fc<0:
            b=c
            fb=fc
        else:
            a=c
            fa=fc
        if abs(fc)<epsilon or abs(b-a)<epsilon:
            break
        c= (a + b) / 2.0
        fc = f(c)
        counter+=1
    print(f"Broj iteracija: {counter}")
    print(f"Priblizna vrijednost korijena: {c}")
    return c    

metoda_zatvorene_domene(-2,2,200,1e-6)
        
        
    
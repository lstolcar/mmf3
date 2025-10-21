import numpy as np
import matplotlib.pyplot as plt 

def metoda_otvorene_domene(x0, N, epsilon):
    def f(x):
        return 7*(x**2) + 15*x - 32
    def f_crtica(x):
        return 14*x+15
    counter=0
    while counter<N:
        x=x0-(f(x0)/f_crtica(x0))
        if (f(x0)/f(x))<epsilon:
            break
        x0=x
        counter+=1
    print(f"Broj iteracija: {counter}") 
    print(f"Priblizna vrijednost korijena: {x}")
    print(f"Vrijednost pogreške: {f(x0)/f_crtica(x0)}")

metoda_otvorene_domene(2.5,200,1e-6)
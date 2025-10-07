import math as mt
import numpy as np
import matplotlib.pyplot as plt
def e_a(x):
    
    clan=1.
    ka=1
    ea=1.
    fa=1.
    while abs(clan)>=1.E-10:
        clan=((-1)**ka)*(((x)**ka)/fa)
        ea=ea+clan
        ka=ka+1
        fa=fa*ka
        #print(k)
        #print(clan)
    print("Za A; e^(-{})=".format(x),ea)
    print("Za A; broj interacija je: ",ka-1)


#e_a(10)
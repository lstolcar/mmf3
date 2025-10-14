import numpy as np      
import matplotlib.pyplot as plt
import math as mt
import derivacijacentralna as dc
import derivacijaunaprijed as du    
import derivacijaunazad as dz

def provjera(f, x, h):
    print("Provjera za h={}".format(h))
    print("Centralna: ")
    dc.derivacija_centralna(f, x, h)
    print("Unaprijed: ")
    du.derivacija_unaprijed(f, x, h)
    print("Unazad: ")
    dz.derivacija_unazad(f, x, h)
   

provjera(np.exp,0.5,1.E-1)
provjera(np.exp,0.5,1.E-4)
provjera(np.exp,0.5,1.E-6) 

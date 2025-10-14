import numpy as np
import matplotlib.pyplot as plt     
import math as mt
import funkcijacrtica2 as fc2
import funkcijacrtica3 as fc3   
import funkcijacrtica5 as fc5
def provjeraB(f, x, h):
    print("Za f2': ")
    fc2.funkcija_crtica2(f, x, h)
    print("Za f3': ")
    fc3.funkcija_crtica3(f, x, h)
    print("Za f5: ")
    fc5.funkcija_crtica5(f, x, h)
   

provjeraB(np.exp,0.5,1.E-1)
provjeraB(np.exp,0.5,1.E-4)
provjeraB(np.exp,0.5,1.E-6) 
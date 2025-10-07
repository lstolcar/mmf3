import math as mt
import numpy as np         
import matplotlib.pyplot as plt 
def e_b(x):
    sk=1.
    kb=1
    eb=1.
    while abs(sk)>=1.E-10:
        sk=-sk*(x/kb)
        eb=eb+sk
        kb=kb+1
        #print(k)
        #print(sk)
    print("Za B; e^(-{})=".format(x),eb)
    print("Za B; broj interacija je: ",kb-1)

#e_b(10) 
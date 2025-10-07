import math as mt
import numpy as np
import matplotlib.pyplot as plt
def e_c(x):
    clan=1.
    kc=1
    ec=1.
    fc=1.
    while abs(clan)>=1.E-10:
        clan=(((x)**kc)/(fc))
        ec=ec+clan
        kc=kc+1
        fc=fc*kc
        #print(k)
        #print(clan)
    #print("e^({})=".format(x),ec)
    print("Za C; e^(-{})=".format(x),1/ec)
    print("Za C; broj interacija je: ",kc-1)
#e_c(10)
import numpy as np
import matplotlib.pyplot as plt
import math as mt
def funkcija_crtica5(f, x, h):
    print( (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h) )
#funkcija_crtica5(np.exp,1,0.1)
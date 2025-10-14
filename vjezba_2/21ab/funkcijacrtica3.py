import numpy as np
import matplotlib.pyplot as plt 
import math as mt   
def funkcija_crtica3(f, x, h):
    print( (f(x + h) - f(x - h)) / (2 * h) )

funkcija_crtica3(np.exp,1,0.1)
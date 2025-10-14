import numpy as np
import matplotlib.pyplot as plt
import math as mt       
def funkcija_crtica2(f, x, h):
    print( (f(x + h) - f(x )) / ( h) )

funkcija_crtica2(np.exp,1,0.1)
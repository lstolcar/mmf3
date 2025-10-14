import numpy as np
import matplotlib.pyplot as plt                                     
import math as mt

def derivacija_unaprijed(f, x, h):
    print( (f(x + h) - f(x)) / h)                

#derivacija_unaprijed(np.exp,1,0.1)
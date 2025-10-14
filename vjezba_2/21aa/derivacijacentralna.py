import numpy as np          
import matplotlib.pyplot as plt     
import math as mt

def derivacija_centralna(f, x, h):
    print( (f(x + h) - f(x - h)) / (2 * h) )        

#derivacija_centralna(np.exp,1,0.1)
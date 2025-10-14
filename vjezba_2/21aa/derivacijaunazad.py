import numpy as np
import matplotlib.pyplot as plt     
import math as mt   

def derivacija_unazad(f, x, h):
    print( (f(x) - f(x - h)) / h)       

#derivacija_unazad(np.exp,1,0.1)
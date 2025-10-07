import math as mt
import numpy as np
import vjezbaA as e_a
import vjezbaB as e_b          
import vjezbaC as e_c
for x in np.linspace(0,100,11):
    print(x)
    e_a.e_a(x)
    e_b.e_b(x)
    e_c.e_c(x)
    print("Točan iznos za x={} je: ".format(x), np.exp(-x))
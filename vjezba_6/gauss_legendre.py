import math
import numpy as np

def gauleg(x1, x2, n):
    
 #   Za zadanu donju i gornju granicu integracije x1 i x2, i stupanj polinoma na ova funkcija vraća listu x i w duljine n, koji sadrže nultočke 
 #   i težine za kvadratur Gauss-Legendre kvadraturu na zadanom intervalu.  
  
    EPS = 1e-6  # Preciznost 
    m = (n + 1) // 2
    xm = 0.5 * (x2 + x1)
    xl = 0.5 * (x2 - x1)

    # Inicijalizacija
    x = np.zeros(n)
    w = np.zeros(n)

    for i in range(1, m + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            if abs(z - z1) < EPS:
                break
        x[i - 1] = xm - xl * z
        x[n - i] = xm + xl * z
        w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
        w[n - i] = w[i - 1]
    
    return x, w
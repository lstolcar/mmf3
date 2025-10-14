import numpy as np
import pandas as pd

def druga_derivacija(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)


f = np.exp
df_true = np.exp

x_values = [0,1,2,3,4,5,6,7,8,9,10]
h_values = [1e-1, 1e-2, 1e-3,1e-4,1e-5,1e-6]


blok_size = 2  
with open("rezultati.txt", "w") as ftxt:
    ftxt.write("TABLICA DRUGE DERIVACIJE (druga derivacija +/- greska (tocna))\n\n")
    
    for start in range(0, len(x_values), blok_size):
        blok_x = x_values[start:start+blok_size]
        
        podaci = []
        for h in h_values:
            red = {"h": h}
            for x in blok_x:
                df_druga = druga_derivacija(f, x, h)
                df_tocna = df_true(x)
                greska = abs(df_druga - df_tocna)
                red[x] = f"{df_druga:.8f} +/- {greska:.8f} ({df_tocna:.8f})"
            podaci.append(red)
        
        df = pd.DataFrame(podaci)
        df = df.set_index("h")
        ftxt.write(df.to_string())
        ftxt.write("\n\n") 




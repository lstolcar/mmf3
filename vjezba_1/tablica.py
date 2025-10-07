import math as mt
import numpy as np
import pandas as pd

rezultati = []

for x in np.linspace(0, 100, 11):
    clan = 1.0
    ka = 1
    ea = 1.0
    fa = 1.0
    while abs(clan) >= 1.E-10:
        clan = ((-1)**ka) * (x**ka) / fa
        ea =ea + clan
        ka =ka + 1
        fa =fa* ka
    sk = 1.0
    kb = 1
    eb = 1.0
    while abs(sk) >= 1.E-10:
        sk = -sk * (x / kb)
        eb =eb+ sk
        kb =kb+ 1
    clan = 1.0
    kc = 1
    ec = 1.0
    fc = 1.0
    while abs(clan) >= 1.E-10:
        clan = (x**kc) / fc
        ec =ec+ clan
        kc =kc+ 1
        fc =fc* kc
    ec = 1 / ec 
    tocna_vrijednost = np.exp(-x)

    rezultati.append({
        "x": x,
        "Metoda A": ea,
        "Iteracija A": ka - 1,
        "Metoda B": eb,
        "Iteracija B": kb - 1,
        "Metoda C": ec,
        "Iteracija C": kc - 1,
        "numpy.exp(-x)": tocna_vrijednost
    })

df = pd.DataFrame(rezultati)

#df = df.round(10)
#print(rezultati)
print(df.to_string(index=False))
with open("tablica.txt", "w") as f:
    f.write(df.to_string(index=False))


import numpy as np
import pandas as pd

def derivacija_unaprijed(f, x, h):
    return (f(x + h) - f(x)) / h  

def derivacija_unazad(f, x, h):
    return (f(x) - f(x - h)) / h  

def derivacija_centralna(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def funkcija_crtica2(f, x, h):
    return (f(x + h) - f(x)) / h

def funkcija_crtica3(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def funkcija_crtica5(f, x, h):
    return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12 * h)



f = np.exp
df_true = np.exp

x_values = [0.5, 1.5, 2.5]
h_values = [1e-1, 1e-4, 1e-6,1e-8,1e-10,1e-12,1e-14]


podaci = []

for x in x_values:
    for h in h_values:
        df_np = derivacija_unaprijed(f, x, h)
        df_zd = derivacija_unazad(f, x, h)
        df_cen = derivacija_centralna(f, x, h)
        f_2 = funkcija_crtica2(f, x, h)
        f_3 = funkcija_crtica3(f, x, h)
        f_5 = funkcija_crtica5(f, x, h)
        df_tocno = df_true(x)
        podaci.append({
            "x": x,
            "h": h,
            "Unaprijed": df_np,
            "Unazad": df_zd,
            "Centralna": df_cen,
            "Dvije tocke": f_2,
            "Tri tocke": f_3,
            "Pet tocka": f_5,
            "Tocna": df_tocno
        })


df = pd.DataFrame(podaci).round(8)


with open("rezultati.txt", "w") as ftxt:
    ftxt.write(df.to_string(index=False))


komentar = """

--------------------------------------------------------------------------------
KOMENTAR O TOCNOSTI REZULTATA:

Tocnost numerickih derivacija ovisi o velicini koraka h i o metodi koja se koristi.

1. Kada je h prevelik (npr. h = 10^-1), pogreska je veca jer se derivacija aproksimira
   grubim odstupanjem.

2. Kada je h premalen (npr. h = 10^-6), dolazi do zaokruzivanja zbog ogranicene
   preciznosti racunanja u racunalu.

3. Metode s vise tocki (npr. 3-tocka i 5-tocka) daju bolje rezultate jer koriste
   vise informacija o funkciji oko tocke x.

4. Centralne metode su opcenito tocnije od jednostavnih unaprijed/unazad derivacija jer imaju podatke
 i o pozitivnom i o negativnom dijelju nagiba krivulje.

Zakljucak:
- Optimalna vrijednost h je ona koja nije previse gruba, a opet da ne dolazi do zaokruzivanja.
- 5-tockasta formula daje najtocnije rezultate kada h nije ekstremno mali.

--------------------------------------------------------------------------------
"""


with open("rezultati.txt", "a") as ftxt:
    ftxt.write(komentar)







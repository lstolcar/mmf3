import math             
import numpy as np      

def gauleg(x1, x2, n):
    
    # Funkcija gauleg računa čvorove (x) i težine (w) za
    # Gauss–Legendreovu kvadraturu na intervalu [x1, x2].
    # x1 - donja granica integracije
    # x2 - gornja granica integracije
    # n  - broj čvorova (red kvadrature)
    # Povratna vrijednost:
    # x - niz duljine n koji sadrži čvorove integracije
    # w - niz duljine n koji sadrži pripadne težine
    

    EPS = 1e-6  
    # Tolerancija

    m = (n + 1) // 2  
    # Broj nultočaka koje treba izračunati.
    # Legendreovi polinomi su simetrični pa je dovoljno računati polovicu, a ostale dobijemo simetrijom.

    xm = 0.5 * (x2 + x1)  
    # Sredina intervala [x1, x2]

    xl = 0.5 * (x2 - x1)  
    # Polovina duljine intervala [x1, x2]
    # Ove vrijednosti služe za preslikavanje  intervala [-1, 1] u [x1, x2].

    # kreiranje nizova za čvorove i težine
    x = np.zeros(n)  
    # Niz za čvorove Gauss–Legendreove kvadrature

    w = np.zeros(n)  
    # Niz za težine Gauss–Legendreove kvadrature

    # GLAVNA PETLJA ZA IZRAČUN ČVOROVA I TEŽINA !
    for i in range(1, m + 1):

        # Početna aproksimacija i-tog korijena Legendreovog polinoma
        # Aproksimacija dolazi iz empirijske formule
        # koja daje vrlo dobru početnu vrijednost
        z = math.cos(math.pi * (i - 0.25) / (n + 0.5))

        # Newton-Raphsonova iteracija za nalaženje točne nultočke
        while True:

            # Početne vrijednosti za rekurzivno računanje
            # Legendreovih polinoma
            p1 = 1.0  
            # p1 predstavlja trenutnu vrijednost polinoma P_j(z)

            p2 = 0.0  
            # p2 predstavlja prethodnu vrijednost polinoma P_(j-1)(z)

            # Rekurzivno računanje Legendreovog polinoma P_n(z)
            for j in range(1, n + 1):

                p3 = p2  
                # p3 pamti vrijednost P_(j-2)(z)

                p2 = p1  
                # p2 postaje P_(j-1)(z)

                # Rekurzivna formula za Legendreove polinome:
                # P_j(z) = ((2j-1)zP_(j-1) - (j-1)P_(j-2)) / j
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j

            # Izračun derivacije Legendreovog polinoma P_n'(z)
            # Potrebno za Newton-Raphsonovu metodu
            pp = n * (z * p1 - p2) / (z * z - 1.0)

            # Spremanje stare vrijednosti z
            z1 = z

            # Newtonov korak:
            # nova aproksimacija = stara - P_n(z) / P_n'(z)
            z = z1 - p1 / pp

            # Provjera konvergencije:
            # ako je promjena dovoljno mala, prekidamo iteraciju
            if abs(z - z1) < EPS:
                break

        # Preslikavanje korijena sa standardnog intervala [-1, 1]
        # na interval [x1, x2]
        x[i - 1] = xm - xl * z
        x[n - i] = xm + xl * z
        # Koristi se simetrija oko sredine intervala

        # Računanje težina Gauss–Legendreove kvadrature
        w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)

        # Težine su također simetrične
        w[n - i] = w[i - 1]

    # Povrat čvorova i težina
    return x, w

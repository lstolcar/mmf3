import numpy as np  
import matplotlib.pyplot as plt 
import math as mt

def lagrange(x_vrijednosti,y_vrijednosti,x, Xmin=0, Xmax=5):
    n=len(x_vrijednosti)
    P2=[]

    P3=[]
    for i in range(n-1):
        L=1
        for j in range(n-1):
            if j!=i:
                L*=(x-x_vrijednosti[j])/(x_vrijednosti[i]-x_vrijednosti[j])
        P2.append(y_vrijednosti[i]*L)


    for i in range(n):
        L=1
        for j in range(n):
            if j!=i:
                L*=(x-x_vrijednosti[j])/(x_vrijednosti[i]-x_vrijednosti[j])
        P3.append(y_vrijednosti[i]*L)
    rezultat2=sum(P2)
    rezultat3=sum(P3)     

    print("Vrijednost interpolacijske polinoma u tocki x =",x,"je P_{",n-2 ," }(x) =",rezultat3)
    print("Vrijednost interpolacijske polinoma u tocki x =",x,"je P_{",n-1 ," }(x) =",rezultat2)  
    
    X=np.linspace(Xmin,Xmax,100)
    p2=[]
    L1y1=[]
    L2y2=[]
    L3y3=[]
    for k in X:
        s = 0
        for i in range(n-1):
            L = 1
            for j in range(n-1):
                if j != i:
                    L *= (k - x_vrijednosti[j]) / (x_vrijednosti[i] - x_vrijednosti[j])
            if i == 0:
                L1y1.append(y_vrijednosti[i]*L)
            elif i == 1:
                L2y2.append(y_vrijednosti[i]*L)
            elif i == 2:
                L3y3.append(y_vrijednosti[i]*L)
            s += y_vrijednosti[i]*L 
        p2.append(s) 

    plt.figure(figsize=(5, 5))
    plt.plot(X, L1y1, '--', label='y1*L1(x)')
    plt.plot(X, L2y2, '--', label='y2*L2(x)')
    plt.plot(X, L3y3, '--', label='y3*L3(x)')
    plt.plot(X, p2, color='black', linewidth=2, label='P2(x)')
    plt.scatter(x_vrijednosti, y_vrijednosti, color='red', zorder=1, label='Točke')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Lagrangeovi članovi i polinom P2(x)')
    plt.legend()
    plt.grid(True)
    plt.show()





lagrange([1,2,3,4],[-5,-12,-15,-8],2.5)
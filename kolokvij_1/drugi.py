import numpy as np
import math as mt
import matplotlib.pyplot as plt

def stap():
    T_lista=[]
    for x in np.linspace(0,1,100):
        T=50*x+280
        T_lista.append(T)
    plt.figure()
    plt.plot(np.linspace(0,1,100), T_lista, color='red',markersize=8, label='p_vezano')
    plt.xlabel('x') 
    plt.ylabel('p_vezano')
    plt.legend()  
    plt.title('p')
    plt.grid(True)  
    plt.show()  
def stap_podjela(L=1):
    A=np.array([[-2,1,0,0,0,0,0,0,0],[1,-2,1,0,0,0,0,0,0],[0,1,-2,1,0,0,0,0,0],[0,0,1,-2,1,0,0,0,0],[0,0,0,1,-2,1,0,0,0],[0,0,0,0,1,-2,1,0,0],[0,0,0,0,0,1,-2,1,0],[0,0,0,0,0,0,1,-2,1],[0,0,0,0,0,0,0,1,-2]])
    d=np.array([-280,0,0,0,0,0,0,0,-330])
    a=[]
    b=[]
    c=[]
    for i in range(9):
        b.append(A[i][i])
        if len(b)==9:
            break
        a.append(A[i+1][i])
        c.append(A[i][i+1])
    c_2=[]
    d_2=[]
    c_2.append(c[0]/b[0])
    d_2.append(d[0]/b[0])
    for i in range(1,9):
        d2=(d[i]-a[i-1]*d_2[i-1])/(b[i]-a[i-1]*c_2[i-1])
        d_2.append(d2)
        if i==8:
            break
        else:
            c2=c[i]/(b[i]-a[i-1]*c_2[i-1])
            c_2.append(c2)  
    
    I=[]
    for i in [8,7,6,5,4,3,2,1,0]:
        if i==8:
            I.append(d_2[-1])
        else:
            I.append(d_2[i]-c_2[i]*I[-1])
    I=I[::-1]   
    I = np.array([(float(i)) for i in I])
    

    print("T {}".format(I.reshape((9,1)) ))

    with open("linjedn.txt", "w") as ftxt:
        ftxt.write("T* \n")
        ftxt.write(str(I.reshape((9,1))))


stap()
stap_podjela()
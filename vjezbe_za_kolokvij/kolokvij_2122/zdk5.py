import numpy as np
import math as mt       
import matplotlib.pyplot as plt


def xevi():
    
    A=np.array([[3,210,0,0,0],[2,6,198,0,0],[0,5,9,165,0],[0,0,9,12,102],[0,0,0,14,15]])
    d=np.array([1,2,3,4,5])
    a=[]
    b=[]
    c=[]
    for i in range(5):
        b.append(A[i][i])
        if len(b)==5:
            break
        a.append(A[i+1][i])
        c.append(A[i][i+1])
    c_2=[]
    d_2=[]
    c_2.append(c[0]/b[0])
    d_2.append(d[0]/b[0])
    for i in range(1,5):
        d2=(d[i]-a[i-1]*d_2[i-1])/(b[i]-a[i-1]*c_2[i-1])
        d_2.append(d2)
        if i==4:
            break
        else:
            c2=c[i]/(b[i]-a[i-1]*c_2[i-1])
            c_2.append(c2)  
    
    I=[]
    for i in [4,3,2,1,0]:
        if i==4:
            I.append(d_2[-1])
        else:
            I.append(d_2[i]-c_2[i]*I[-1])
    I=I[::-1]   
    I = np.array([(float(i)) for i in I])
    

    print("x  {}".format(I.reshape((5,1)) ))

    with open("linjedn.txt", "w") as ftxt:
        ftxt.write("x * \n")
        ftxt.write(str(I.reshape((5,1))))

xevi()
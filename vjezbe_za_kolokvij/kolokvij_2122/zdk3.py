import numpy as np
import math as mt       
import matplotlib.pyplot as plt


def otpori(R1=-1, R2=[1,2,3,4,5], R3=-3):
    
    A=np.array([[R2[0],R3,0,0,0],[R1,R2[1],R3,0,0],[0,R1,R2[2],R3,0],[0,0,R1,R2[3],R3],[0,0,0,R1,R2[4]]])
    d=np.array([5,4,3,2,1])
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
    I = np.array([round(29*float(i)) for i in I])
    

    print("I = 1/29 * {}".format(I.reshape((5,1)) ))

    with open("linjedn.txt", "w") as ftxt:
        ftxt.write("I = 1/94 * \n")
        ftxt.write(str(I.reshape((5,1))))

otpori()

import numpy as np
import math as mt       
import matplotlib.pyplot as plt


def otpori(R1=1, R2=2, R3=4, R4=1):
    
    A=np.array([[R1+R2+R4,-R2,0,0],[-R2,R1+2*R2+R4,-R2,0],[0,-R2,R1+2*R2+R4,-R2],[0,0,-R2,R1+R2+R3+R4]])
    d=np.array([5,0,0,0])
    a=[]
    b=[]
    c=[]
    for i in range(4):
        b.append(A[i][i])
        if len(b)==4:
            break
        a.append(A[i+1][i])
        c.append(A[i][i+1])
    c_2=[]
    d_2=[]
    c_2.append(c[0]/b[0])
    d_2.append(d[0]/b[0])
    for i in range(1,4):
        d2=(d[i]-a[i-1]*d_2[i-1])/(b[i]-a[i-1]*c_2[i-1])
        d_2.append(d2)
        if i==3:
            break
        else:
            c2=c[i]/(b[i]-a[i-1]*c_2[i-1])
            c_2.append(c2)  
    
    I=[]
    for i in [3,2,1,0]:
        if i==3:
            I.append(d_2[-1])
        else:
            I.append(d_2[i]-c_2[i]*I[-1])
    I=I[::-1]   
    I = np.array([round(94*float(i)) for i in I])
    

    print("I = 1/94 * {}".format(I.reshape((4,1)) ))

    with open("linjedn.txt", "w") as ftxt:
        ftxt.write("I = 1/94 * \n")
        ftxt.write(str(I.reshape((4,1))))

otpori()
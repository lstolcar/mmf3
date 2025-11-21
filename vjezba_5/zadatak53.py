import numpy as np  
import matplotlib.pyplot as plt             
import math as mt

import numpy as np
a0_to_A = 0.52917721092    
hartree_to_K = 315775.04   
data = np.loadtxt(r"C:\Users\lovre\mmf3\mmf3\mmf3\vjezba_5\V(H-H).txt", comments="#",skiprows=2)
r_au = data[:, 0]
V_au = data[:, 1]
r_A = r_au * a0_to_A
V_K = V_au * hartree_to_K
converted = np.column_stack((r_A, V_K))
np.savetxt(r"C:\Users\lovre\mmf3\mmf3\mmf3\vjezba_5\V(H-H)_AK.txt", converted, header="r/Å   V/K", fmt="%.6f")
podatci = np.loadtxt(r"C:\Users\lovre\mmf3\mmf3\mmf3\vjezba_5\V(H-H)_AK.txt", comments="#",skiprows=1)
r_A0 = podatci[:, 0]
V_K0 = podatci[:, 1]
n=len(r_A0)
Pl=[]
X=np.linspace(0,10,100)
for x in X:
    s=0
    for i in range(n):
        L=1
        for j in range(n):
            if j!=i:
                L*=(x - r_A0[j])/(r_A0[i]-r_A0[j])
        s+=V_K0[i]*L 
    Pl.append(s)
#print(Pl)
plt.figure()
plt.plot(X, Pl,'o', color='red', label='Lagrangeovi polinom')
plt.plot(r_A0, V_K0,linestyle='none', marker='o', markerfacecolor='none', markeredgecolor='black', markeredgewidth=1, label='(r_{i},V_{i})', alpha=1)
plt.xlabel('r/Å')               
plt.ylabel('V/K') 
plt.title('Interpolacijski polinom P6(x) za potencijalnu energiju V(H-H)')
plt.legend() 
plt.grid(True)
plt.xlim(0, 11)    
plt.ylim(-10, 10)
plt.show()   



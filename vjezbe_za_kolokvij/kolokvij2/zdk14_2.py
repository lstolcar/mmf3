import numpy as np
import matplotlib.pyplot as plt
m=0.02
k=0.08
b=0.004
def F(x,v):
    return -k*x - b*v
def runge_kutta(t_in,t_fin,N,x0,f):
    step=(t_fin-t_in)/N
    t=[0]
    v=[0]
    x=[x0]
    F=[f(x0,0)]
    for i in np.arange(t_in,t_fin+step,step):
        #prvi korak (k1)
        t.append(i)
        k_v=f(x[-1],v[-1])/m
        sw=k_v
        k_x=v[-1]
        sk=k_x
        #drugi korak(k2)
        v_p=v[-1]+k_v*(step/2)
        x_p=x[-1]+k_x*(step/2)

        k_v=f(x_p,v_p)/m
        sw+=2*k_v
        k_x=v_p
        sk+=2*k_x
        #treći korak(k3)
        v_p=v[-1]+k_v*(step/2)
        x_p=x[-1]+k_x*(step/2)
        k_v=f(x_p,v_p)/m
        sw+=2*k_v
        k_x=v_p
        sk+=2*k_x
        #zadnji korak
        v_p=v[-1]+k_v*(step)
        x_p=x[-1]+k_x*(step)
        k_v=f(x_p,v_p)/m
        sw+=k_v
        k_x=v_p
        sk+=k_x
        #konacno
        v.append(v[-1]+(sw/6)*step)
        x.append(x[-1]+(sk/6)*step)
        F.append(f(x[-1],v[-1]))

    return t,x,v,F

t,x,v,F=runge_kutta(0,20,83,0.05,F)
plt.plot(t,x,label='x(t)')
plt.plot(t,v,label='v(t)')
plt.plot(t,F,label='F(t)')
plt.legend()
plt.xlabel("t(s)")
plt.show()

def analytical_solution(t):
    x=0.05*np.exp(-1*t/10)*np.cos((np.sqrt(399)/10)*t)+(0.05/np.sqrt(399))*np.sin((np.sqrt(399)/10)*t)
    return x
x_analytical=[analytical_solution(i) for i in t]
plt.plot(t,x_analytical,label='Analitičko rješenje')
plt.plot(t,x,label='Numeričko rješenje',linestyle='dashed')
plt.legend()
plt.xlabel("t(s)")
plt.ylabel("x(t)")
plt.show()

error=[abs(x[i]-x_analytical[i]) for i in range(len(t))]
plt.plot(t,error)  
plt.xlabel("t(s)")
plt.ylabel("Greška")
plt.title("Greška između analitičkog i numeričkog rješenja")
plt.show()

a=round((19.5/20)*len(t))
print(error[a])


analytical_solution(20)


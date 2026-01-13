import numpy as np
import matplotlib.pyplot as plt

def simulacija():
    l = 0.2484902028828339
    g = 9.81
    t0, tN = 0, 50
    N = 20000
    h = (tN - t0) / N
    t = np.linspace(t0, tN, N+1)
    theta0 = np.deg2rad(4)
    
    y_e = np.zeros((2, N+1))  
    y_pk = np.zeros((2, N+1))  
    y_rk2 = np.zeros((2, N+1)) 
    y_rk4 = np.zeros((2, N+1)) 
    
    for arr in [y_e, y_pk, y_rk2, y_rk4]:
        arr[0,0] = theta0
        arr[1,0] = 0
    def f(theta): return -(g/l) * np.sin(theta)

    for n in range(N):
        # 1. Euler
        y_e[0,n+1] = y_e[0,n] + h * y_e[1,n]
        y_e[1,n+1] = y_e[1,n] - h * (g/l) *y_e[0,n]
        

        # 2. PK
        p_theta = y_pk[0,n] + h * y_pk[1,n]
        p_omega = y_pk[1,n] + h * f(y_pk[0,n])
        y_pk[0,n+1] = y_pk[0,n] + (h/2) * (y_pk[1,n] + p_omega)
        y_pk[1,n+1] = y_pk[1,n] + (h/2) * (f(y_pk[0,n]) + f(p_theta))

        # 3. RK2
        k1_v = f(y_rk2[0,n])
        k1_p = y_rk2[1,n]
        k2_v = f(y_rk2[0,n] + h*k1_p)
        k2_p = y_rk2[1,n] + h*k1_v
        y_rk2[0,n+1] = y_rk2[0,n] + (h/2) * (k1_p + k2_p)
        y_rk2[1,n+1] = y_rk2[1,n] + (h/2) * (k1_v + k2_v)

        # 4. RK4
        k1_0 = h * y_rk4[1,n]
        k1_1 = h * f(y_rk4[0,n])
        k2_0 = h * (y_rk4[1,n] + 0.5*k1_1)
        k2_1 = h * f(y_rk4[0,n] + 0.5*k1_0)
        k3_0 = h * (y_rk4[1,n] + 0.5*k2_1)
        k3_1 = h * f(y_rk4[0,n] + 0.5*k2_0)
        k4_0 = h * (y_rk4[1,n] + k3_1)
        k4_1 = h * f(y_rk4[0,n] + k3_0)
        y_rk4[0,n+1] = y_rk4[0,n] + (k1_0 + 2*k2_0 + 2*k3_0 + k4_0)/6
        y_rk4[1,n+1] = y_rk4[1,n] + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)/6

    
    i_start, i_end = int(0/h), int(20/h)

    plt.figure(figsize=(10, 6))

    t_plot = t[i_start:i_end]
    plt.plot(t_plot, theta0 * np.cos(np.sqrt(g/l)*t_plot), 
             color='cyan', linewidth=5, label="analiticko")
    plt.plot(t_plot, y_e[0,i_start:i_end], 
             color='limegreen', linewidth=1, label="E-metoda")
    plt.plot(t_plot, y_pk[0,i_start:i_end], 
             color='blue', linestyle=(0, (5, 5)), linewidth=2, label="PK-metoda")
    plt.plot(t_plot, y_rk2[0,i_start:i_end], 
             color='red', linestyle=(0, (7, 7)), linewidth=2, label="RK2-metoda")
    plt.plot(t_plot, y_rk4[0,i_start:i_end], 
             color='black', linestyle=(0, (1, 5)), linewidth=3, label="RK4-metoda")


    plt.title(f"y'(0)=0,  y(0)=4°,  N = {N}")
    plt.xlim(19, 20)
    plt.ylim(-0.1, 0.1)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend(loc='lower left', frameon=False)
    plt.tick_params(direction='in', top=True, right=True)
    plt.show()
def Runge_Kutta4(theta1=4,theta2=8, theta3=16, theta4=32,theta5=64):
    l = 0.2484902028828339
    g = 9.81
    t0, tN = 0, 10
    N = 20000
    h = (tN - t0) / N
    t = np.linspace(t0, tN, N+1)
    theta1_ = theta1 * np.pi / 180
    theta2_ = theta2 * np.pi / 180
    theta3_ = theta3 * np.pi / 180
    theta4_ = theta4 * np.pi / 180
    theta5_ = theta5 * np.pi / 180  

    y_rk4_1 = np.zeros((2, N+1))
    y_rk4_2 = np.zeros((2, N+1)) 
    y_rk4_3 = np.zeros((2, N+1))
    y_rk4_4 = np.zeros((2, N+1))
    y_rk4_5 = np.zeros((2, N+1))
    for arr1 in [y_rk4_1]:
        arr1[0,0] = theta1_
        arr1[1,0] = 0
    def f1(theta): return -(g/l) * np.sin(theta)

    for n in range(N):
        # 4. RK4
        k1_0 = h * y_rk4_1[1,n]
        k1_1 = h * f1(y_rk4_1[0,n])
        k2_0 = h * (y_rk4_1[1,n] + 0.5*k1_1)
        k2_1 = h * f1(y_rk4_1[0,n] + 0.5*k1_0)
        k3_0 = h * (y_rk4_1[1 ,n] + 0.5*k2_1)
        k3_1 = h * f1(y_rk4_1[0,n] + 0.5*k2_0)
        k4_0 = h * (y_rk4_1[1,n] + k3_1)
        k4_1 = h * f1(y_rk4_1[0,n] + k3_0)
        y_rk4_1[0,n+1] = y_rk4_1[0,n] + (k1_0 + 2*k2_0 + 2*k3_0 + k4_0)/6
        y_rk4_1[1,n+1] = y_rk4_1[1,n] + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)/6

    for arr2 in [y_rk4_2]:
        arr2[0,0] = theta2_
        arr2[1,0] = 0
    def f2(theta): return -(g/l) * np.sin(theta)

    for n in range(N):
        # 4. RK4
        k1_0 = h * y_rk4_2[1,n]
        k1_1 = h * f2(y_rk4_2[0,n])
        k2_0 = h * (y_rk4_2[1,n] + 0.5*k1_1)
        k2_1 = h * f2(y_rk4_2[0,n] + 0.5*k1_0)
        k3_0 = h * (y_rk4_2[1 ,n] + 0.5*k2_1)
        k3_1 = h * f2(y_rk4_2[0,n] + 0.5*k2_0)
        k4_0 = h * (y_rk4_2[1,n] + k3_1)
        k4_1 = h * f2(y_rk4_2[0,n] + k3_0)
        y_rk4_2[0,n+1] = y_rk4_2[0,n] + (k1_0 + 2*k2_0 + 2*k3_0 + k4_0)/6
        y_rk4_2[1,n+1] = y_rk4_2[1,n] + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)/6

    for arr3 in [y_rk4_3]:
        arr3[0,0] = theta3_
        arr3[1,0] = 0
    def f3(theta): return -(g/l) * np.sin(theta)

    for n in range(N):
        # 4. RK4
        k1_0 = h * y_rk4_3[1,n]
        k1_1 = h * f3(y_rk4_3[0,n])
        k2_0 = h * (y_rk4_3[1,n] + 0.5*k1_1)
        k2_1 = h * f3(y_rk4_3[0,n] + 0.5*k1_0)
        k3_0 = h * (y_rk4_3[1 ,n] + 0.5*k2_1)
        k3_1 = h * f3(y_rk4_3[0,n] + 0.5*k2_0)
        k4_0 = h * (y_rk4_3[1,n] + k3_1)
        k4_1 = h * f3(y_rk4_3[0,n] + k3_0)
        y_rk4_3[0,n+1] = y_rk4_3[0,n] + (k1_0 + 2*k2_0 + 2*k3_0 + k4_0)/6
        y_rk4_3[1,n+1] = y_rk4_3[1,n] + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)/6

    for arr4 in [y_rk4_4]:
        arr4[0,0] = theta4_
        arr4[1,0] = 0
    def f4(theta): return -(g/l) * np.sin(theta)

    for n in range(N):
        # 4. RK4
        k1_0 = h * y_rk4_4[1,n]
        k1_1 = h * f4(y_rk4_4[0,n])
        k2_0 = h * (y_rk4_4[1,n] + 0.5*k1_1)
        k2_1 = h * f4(y_rk4_4[0,n] + 0.5*k1_0)
        k3_0 = h * (y_rk4_4[1 ,n] + 0.5*k2_1)
        k3_1 = h * f4(y_rk4_4[0,n] + 0.5*k2_0)
        k4_0 = h * (y_rk4_4[1,n] + k3_1)
        k4_1 = h * f4(y_rk4_4[0,n] + k3_0)
        y_rk4_4[0,n+1] = y_rk4_4[0,n] + (k1_0 + 2*k2_0 + 2*k3_0 + k4_0)/6
        y_rk4_4[1,n+1] = y_rk4_4[1,n] + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)/6

    for arr5 in [y_rk4_5]:
        arr5[0,0] = theta5_
        arr5[1,0] = 0
    def f5(theta): return -(g/l) * np.sin(theta)

    for n in range(N):
        # 4. RK4
        k1_0 = h * y_rk4_5[1,n]
        k1_1 = h * f5(y_rk4_5[0,n]) 
        k2_0 = h * (y_rk4_5[1,n] + 0.5*k1_1)
        k2_1 = h * f5(y_rk4_5[0,n] + 0.5*k1_0)
        k3_0 = h * (y_rk4_5[1 ,n] + 0.5*k2_1)
        k3_1 = h * f5(y_rk4_5[0,n] + 0.5*k2_0)
        k4_0 = h * (y_rk4_5[1,n] + k3_1)
        k4_1 = h * f5(y_rk4_5[0,n] + k3_0)
        y_rk4_5[0,n+1] = y_rk4_5[0,n] + (k1_0 + 2*k2_0 + 2*k3_0 + k4_0)/6
        y_rk4_5[1,n+1] = y_rk4_5[1,n] + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1)/6
    plt.figure(figsize=(10, 6))
    plt.plot(t, y_rk4_1[0,:], label=f"y(0)={theta1}°")
    plt.plot(t, theta1_ * np.cos(np.sqrt(g/l)*t),   color='cyan', label="analiticko")
    plt.xlim(0, 10)
    plt.ylim(-1, 1)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend(loc='upper right', frameon=False)
    plt.tick_params(direction='in', top=True, right=True)
    plt.show()  
    plt.plot(t, y_rk4_2[0,:], label=f"y(0)={theta2}°")
    plt.plot(t, theta2_ * np.cos(np.sqrt(g/l)*t),   color='cyan', label="analiticko")
    plt.xlim(0, 10)
    plt.ylim(-1, 1)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend(loc='upper right', frameon=False)
    plt.tick_params(direction='in', top=True, right=True)
    plt.show()
    plt.plot(t, y_rk4_3[0,:], label=f"y(0)={theta3}°")
    plt.plot(t, theta3_ * np.cos(np.sqrt(g/l)*t),   color='cyan', label="analiticko")
    plt.xlim(0, 10)
    plt.ylim(-1, 1)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend(loc='upper right', frameon=False)
    plt.tick_params(direction='in', top=True, right=True)
    plt.show()
    plt.plot(t, y_rk4_4[0,:], label=f"y(0)={theta4}°")
    plt.plot(t, theta4_ * np.cos(np.sqrt(g/l)*t),   color='cyan', label="analiticko")
    plt.xlim(0, 10)
    plt.ylim(-1, 1)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend(loc='upper right', frameon=False)
    plt.tick_params(direction='in', top=True, right=True)
    plt.show()
    plt.plot(t, y_rk4_5[0,:], label=f"y(0)={theta5}°")
    plt.plot(t, theta5_ * np.cos(np.sqrt(g/l)*t),   color='cyan', label="analiticko")
    plt.xlim(0, 10)
    plt.ylim(-1, 1)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend(loc='upper right', frameon=False)
    plt.tick_params(direction='in', top=True, right=True)
    plt.show()

def Euler():
    N=[10000, 20000, 40000, 80000, 160000, 320000, 640000]
    l = 0.2484902028828339
    g = 9.81
    t0, tN = 0, 50  
    theta0 = 4 * np.pi / 180
    lista_n1=[]
    lista_n2=[]
    lista_n3=[]
    lista_n4=[]
    lista_n5=[]
    lista_n6=[]
    lista_n7=[]

    for N_ in N:
        h = (tN - t0) / N_
        t = np.linspace(t0, tN, N_+1)
        if N_==10000:
            y_e = np.zeros((2, N_+1))
            for arr in [y_e]:
                arr[0,0] = theta0
                arr[1,0] = 0
            def f(theta): return -(g/l) * np.sin(theta)
            for n in range(N_):
                # 1. Euler
                y_e[0,n+1] = y_e[0,n] + h * y_e[1,n]
                y_e[1,n+1] = y_e[1,n] + h * f(y_e[0,n])
                lista_n1.append(y_e[0,n+1])
        elif N_==20000:
            y_e = np.zeros((2, N_+1))
            for arr in [y_e]:
                arr[0,0] = theta0
                arr[1,0] = 0
            def f(theta): return -(g/l) * np.sin(theta)
            for n in range(N_):
                # 1. Euler
                y_e[0,n+1] = y_e[0,n] + h * y_e[1,n]
                y_e[1,n+1] = y_e[1,n] + h * f(y_e[0,n])
                lista_n2.append(y_e[0,n+1])
        elif N_==40000:
            y_e = np.zeros((2, N_+1))
            for arr in [y_e]:
                arr[0,0] = theta0
                arr[1,0] = 0
            def f(theta): return -(g/l) * np.sin(theta)
            for n in range(N_):
                # 1. Euler
                y_e[0,n+1] = y_e[0,n] + h * y_e[1,n]
                y_e[1,n+1] = y_e[1,n] + h * f(y_e[0,n])
                lista_n3.append(y_e[0,n+1])
        elif N_==80000:
            y_e = np.zeros((2, N_+1))
            for arr in [y_e]:
                arr[0,0] = theta0
                arr[1,0] = 0
            def f(theta): return -(g/l) * np.sin(theta)
            for n in range(N_):
                # 1. Euler
                y_e[0,n+1] = y_e[0,n] + h * y_e[1,n]
                y_e[1,n+1] = y_e[1,n] + h * f(y_e[0,n])
                lista_n4.append(y_e[0,n+1])
        elif N_==160000:
            y_e = np.zeros((2, N_+1))
            for arr in [y_e]:
                arr[0,0] = theta0
                arr[1,0] = 0
            def f(theta): return -(g/l) * np.sin(theta)
            for n in range(N_):
                # 1. Euler
                y_e[0,n+1] = y_e[0,n] + h * y_e[1,n]
                y_e[1,n+1] = y_e[1,n] + h * f(y_e[0,n])
                lista_n5.append(y_e[0,n+1])
        elif N_==320000:
            y_e = np.zeros((2, N_+1))
            for arr in [y_e]:
                arr[0,0] = theta0
                arr[1,0] = 0
            def f(theta): return -(g/l) * np.sin(theta)
            for n in range(N_):
                # 1. Euler
                y_e[0,n+1] = y_e[0,n] + h * y_e[1,n]
                y_e[1,n+1] = y_e[1,n] + h * f(y_e[0,n])
                lista_n6.append(y_e[0,n+1])
        elif N_==640000:
            y_e = np.zeros((2, N_+1))
            for arr in [y_e]:
                arr[0,0] = theta0
                arr[1,0] = 0
            def f(theta): return -(g/l) * np.sin(theta)
            for n in range(N_):
                # 1. Euler
                y_e[0,n+1] = y_e[0,n] + h * y_e[1,n]
                y_e[1,n+1] = y_e[1,n] + h * f(y_e[0,n])
                lista_n7.append(y_e[0,n+1])
    plt.figure(figsize=(10, 6))
    plt.plot(np.linspace(t0, tN, 10000), lista_n1, label=f"N=10 000")
    plt.plot(np.linspace(t0, tN, 20000), lista_n2, label=f"N=20 000")
    plt.plot(np.linspace(t0, tN, 40000), lista_n3, label=f"N=40 000")
    plt.plot(np.linspace(t0, tN, 80000), lista_n4, label=f"N=80 000")
    plt.plot(np.linspace(t0, tN, 160000), lista_n5, label=f"N=160 000")
    plt.plot(np.linspace(t0, tN, 320000), lista_n6, label=f"N=320 000")       
    plt.plot(np.linspace(t0, tN, 640000), lista_n7, label=f"N=640 000")
    plt.plot(np.linspace(t0, tN, 10000), theta0 * np.cos(np.sqrt(g/l)*np.linspace(t0, tN, 10000)), 
             color='cyan', label="analiticko") 
    plt.title(f"Eulerova metoda za različite N")
    plt.xlim(0, 20)
    plt.ylim(-0.2, 0.2)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend(loc='upper right', frameon=False)
    plt.tick_params(direction='in', top=True, right=True)
    plt.show()

simulacija()
Runge_Kutta4()
Euler()
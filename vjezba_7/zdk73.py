import numpy as np
import matplotlib.pyplot as plt

def simulacija():
    l = 0.2484902028828339
    g = 9.81
    t0, tN = 0, 20
    N = 200000
    h = (tN - t0) / N
    t = np.linspace(t0, tN, N+1)

    theta0 = np.deg2rad(4)

    # y[0] = theta, y[1] = omega
    y_e   = np.zeros((2, N+1))
    y_pk  = np.zeros((2, N+1))
    y_rk2 = np.zeros((2, N+1))
    y_rk4 = np.zeros((2, N+1))

    for y in [y_e, y_pk, y_rk2, y_rk4]:
        y[0,0] = theta0
        y[1,0] = 0

    def f(theta):
        return -(g/l) * np.sin(theta)

    for n in range(N):

        # 1. Euler
        y_e[0,n+1] = y_e[0,n] + h * y_e[1,n]
        y_e[1,n+1] = y_e[1,n] + h * f(y_e[0,n])

        # 2. Prediktor–korektor (Heun)
        p_theta = y_pk[0,n] + h * y_pk[1,n]
        p_omega = y_pk[1,n] + h * f(y_pk[0,n])

        y_pk[0,n+1] = y_pk[0,n] + h/2 * (y_pk[1,n] + p_omega)
        y_pk[1,n+1] = y_pk[1,n] + h/2 * (f(y_pk[0,n]) + f(p_theta))

        # 3. RK2
        k1_theta = y_rk2[1,n]
        k1_omega = f(y_rk2[0,n])

        k2_theta = y_rk2[1,n] + h * k1_omega
        k2_omega = f(y_rk2[0,n] + h * k1_theta)

        y_rk2[0,n+1] = y_rk2[0,n] + h/2 * (k1_theta + k2_theta)
        y_rk2[1,n+1] = y_rk2[1,n] + h/2 * (k1_omega + k2_omega)

        ## 4. RK4
        k1_0 = h * y_rk4[1,n]
        k1_1 = h * f(y_rk4[0,n])

        k2_0 = h * (y_rk4[1,n] + 0.5*k1_1)
        k2_1 = h * f(y_rk4[0,n] + 0.5*k1_0)

        k3_0 = h * (y_rk4[1,n] + 0.5*k2_1)
        k3_1 = h * f(y_rk4[0,n] + 0.5*k2_0)

        k4_0 = h * (y_rk4[1,n] + k3_1)
        k4_1 = h * f(y_rk4[0,n] + k3_0)

        y_rk4[0,n+1] = y_rk4[0,n] + (k1_0 + 2*k2_0 + 2*k3_0 + k4_0) / 6
        y_rk4[1,n+1] = y_rk4[1,n] + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1) / 6


    # --- GRAF ---
    i_start, i_end = int(0/h), int(20/h)
    t_plot = t[i_start:i_end]

    plt.figure(figsize=(10,6))

    # Malo-kutna analitika (referenca)
    plt.plot(
        t_plot,
        theta0 * np.cos(np.sqrt(g/l)*t_plot),
        color='cyan', linewidth=5, label="analitičko (mali kut)"
    )

    plt.plot(t_plot, y_e[0,i_start:i_end], label="Euler", linewidth=1)
    plt.plot(t_plot, y_pk[0,i_start:i_end], '--', label="PK", linewidth=2)
    plt.plot(t_plot, y_rk2[0,i_start:i_end], '--', label="RK2", linewidth=2)
    plt.plot(t_plot, y_rk4[0,i_start:i_end], ':', label="RK4", linewidth=3)

    plt.title(f"y'(0)=0, y(0)=4°, N={N}")
    plt.xlim(19, 20)
    plt.ylim(-0.1, 0.1)
    plt.axhline(0, color='black', linewidth=0.8)
    plt.legend(frameon=False)
    plt.tick_params(direction='in', top=True, right=True)
    plt.show()

def Runge_Kutta4(theta1=4, theta2=8, theta3=16, theta4=32, theta5=64):


    l = 0.2484902028828339
    g = 9.81    
    t0, tN = 0, 10
    N = 200
    h = (tN - t0) / N
    t = np.linspace(t0, tN, N+1)

    
    thetas_deg = [theta1, theta2, theta3, theta4, theta5]
    thetas = [np.deg2rad(th) for th in thetas_deg]


    def f(theta):
        return -(g / l) * np.sin(theta)

    
    def rk4(theta0):
        y = np.zeros((2, N+1))
        y[0, 0] = theta0   
        y[1, 0] = 0.0      

        for n in range(N):
            k1_0 = h * y[1, n]
            k1_1 = h * f(y[0, n])

            k2_0 = h * (y[1, n] + 0.5 * k1_1)
            k2_1 = h * f(y[0, n] + 0.5 * k1_0)

            k3_0 = h * (y[1, n] + 0.5 * k2_1)
            k3_1 = h * f(y[0, n] + 0.5 * k2_0)

            k4_0 = h * (y[1, n] + k3_1)
            k4_1 = h * f(y[0, n] + k3_0)

            y[0, n+1] = y[0, n] + (k1_0 + 2*k2_0 + 2*k3_0 + k4_0) / 6
            y[1, n+1] = y[1, n] + (k1_1 + 2*k2_1 + 2*k3_1 + k4_1) / 6

        return y

    
    for theta0, theta_deg in zip(thetas, thetas_deg):

        y_rk4 = rk4(theta0)

    
        theta_analytic = theta0 * np.cos(np.sqrt(g/l) * t)

        plt.figure(figsize=(10, 6))
        plt.plot(t, y_rk4[0, :], color='red', linewidth=5, label=f"RK4, θ₀ = {theta_deg}°")
        plt.plot(t, theta_analytic, 'c', linewidth=5, label="Analitičko rješenje")

        plt.xlim(0, 10)
        plt.ylim(-0.5, 0.5)
        plt.axhline(0, color='black', linewidth=0.8)
        plt.legend(frameon=False)
        plt.tick_params(direction='in', top=True, right=True)
        plt.xlabel("t [s]")
        plt.ylabel("θ [rad]")
        plt.show()


def euler(N, t0=0, tN=20):
    g = 9.81
    l = 0.2484902028828339
    theta0 = 4 * np.pi / 180

    h = (tN - t0) / N
    t = np.linspace(t0, tN, N + 1)

    theta = np.zeros(N + 1)
    omega = np.zeros(N + 1)

    theta[0] = theta0
    omega[0] = 0.0

    for n in range(N):
        theta[n+1] = theta[n] + h * omega[n]
        omega[n+1] = omega[n] - h * (g/l) * np.sin(theta[n])

    return t, theta


Ns = [10_000, 20_000, 40_000, 80_000, 160_000, 320_000, 640_000]

plt.figure(figsize=(10, 6))

for N in Ns:
    t, theta = euler(N)
    plt.plot(t, theta, label=f"$y_E(t)$ za N = {N}")

t_anal = np.linspace(0, 50, 10000)
theta0 = 4 * np.pi / 180
plt.plot( t_anal, theta0 * np.cos(np.sqrt(9.81 / 0.2484902028828339) * t_anal), linewidth=2, label="$y_a(t)$" )

plt.xlim(0, 20)
plt.ylim(-0.2, 0.2)
plt.axhline(0, color="black", linewidth=0.8)
plt.legend(frameon=True)
plt.xlabel("t")
plt.ylabel("θ(t)")
plt.title("Eulerova metoda – numerička divergencija")
plt.show()



simulacija()
#Runge_Kutta4()
#euler()
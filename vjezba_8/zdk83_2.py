import numpy as np
import matplotlib.pyplot as plt

def parcijalna_implicitna(N=100, D=1e-2, L=20.0, T_final=200, dt=0.5):

    dx = L / (N + 1)
    x = np.linspace(0, L, N + 2)
    alpha = D * dt / dx**2
    a = -alpha * np.ones(N-1)
    b = (1 + 2*alpha) * np.ones(N)
    c = -alpha * np.ones(N-1)
    u = np.zeros(N)
    for i in range(N):
        if 2.0 <= x[i+1] <= 5.0:
            u[i] = 5.5

    time_points = [0, 50, 100, 150, 200]
    results = {0: u.copy()}

    t = 0
    while t < T_final:
        d = u.copy()
        c2 = np.zeros(N-1)
        d2 = np.zeros(N)
        c2[0] = c[0] / b[0]
        d2[0] = d[0] / b[0]

        for i in range(1, N-1):
            naz = b[i] - a[i-1] * c2[i-1]
            c2[i] = c[i] / naz
            d2[i] = (d[i] - a[i-1] * d2[i-1]) / naz

        d2[-1] = (d[-1] - a[-1] * d2[-2]) / (b[-1] - a[-1] * c2[-2])
        u_new = np.zeros(N)
        u_new[-1] = d2[-1]
        for i in range(N-2, -1, -1):
            u_new[i] = d2[i] - c2[i] * u_new[i+1]

        u = u_new
        t += dt

        if t in time_points:
            results[t] = u.copy()

    plt.figure(figsize=(10,6))
    for time, data in results.items():
        plt.plot(x[1:-1], data, label=f't = {time}')
    plt.xlabel('x')
    plt.ylabel('ρ(x,t)')
    plt.title('Implicitna (1D)')
    plt.legend()
    plt.grid()
    plt.show()

parcijalna_implicitna()


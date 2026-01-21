import numpy as np
import matplotlib.pyplot as plt

def Crank_Nicolson(N=100, D=1e-2, L=20.0, T_final=200, dt=0.5):
    dx = L / (N + 1)
    x = np.linspace(0, L, N + 2)
    alpha = D * dt / (dx**2) 
    
    a = -alpha * np.ones(N - 1)
    b = (2 + 2 * alpha) * np.ones(N)
    c = -alpha * np.ones(N - 1)
    

    u = np.zeros(N)
    for i in range(N):
        xi = x[i+1] 
        if 2.0 <= xi <= 5.0:
            u[i] = 5.5

    time_points = [0, 50, 100, 150, 200]
    results = {0: u.copy()}
    
    t = 0
    while t < T_final:
        d = np.zeros(N)
        for i in range(N):
            u_prev = u[i-1] if i > 0 else 0.0 
            u_next = u[i+1] if i < N-1 else 0.0  
            d[i] = alpha * u_prev + (2 - 2 * alpha) * u[i] + alpha * u_next

        c2 = np.zeros(N - 1)
        d2 = np.zeros(N)
        c2[0] = c[0] / b[0]
        d2[0] = d[0] / b[0]

        for i in range(1, N - 1):
            denom = b[i] - a[i-1] * c2[i-1]
            c2[i] = c[i] / denom
            d2[i] = (d[i] - a[i-1] * d2[i-1]) / denom

        denom_last = b[-1] - a[-1] * c2[-1]
        d2[-1] = (d[-1] - a[-1] * d2[-1]) / denom_last

        u_new = np.zeros(N)
        u_new[-1] = d2[-1]
        for i in range(N - 2, -1, -1):
            u_new[i] = d2[i] - c2[i] * u_new[i+1]

        u = u_new
        t += dt
        
        
        
        if t in time_points:
            results[t] = u.copy()

    plt.figure(figsize=(10, 6))
    for tp, val in results.items():
        full_u = np.concatenate(([0], val, [0]))
        plt.plot(x, full_u, label=f't = {tp}s')
    
    plt.xlabel('x / m')
    plt.ylabel('rho(x,t) / kg/m')
    plt.title('Crank-Nicolson: Difuzija gustoće čestica')
    plt.legend()
    plt.grid(True)
    plt.show()

Crank_Nicolson()
        


import numpy as np
import matplotlib.pyplot as plt
metoda="eksplicitna" 
A = 1 
L=10  
T_final = 10
dt = 0.0001

N = 100
dx = 0.1
x = np.linspace(-5, 5, N + 2) 
alpha = A * dt / dx**2

def initial_condition(x_val):
    return 25*(x_val)**2-(x_val)**4
    

rho = np.vectorize(initial_condition)(x)

time_points = [0, 4, 8] 
results = {0.0: rho.copy()}

num_steps = int(T_final / dt)

if metoda == "eksplicitna":
    for j in range(1, num_steps + 1):
        rho_new = rho.copy()
        for i in range(1, N + 1):
            rho_new[i] = alpha * rho[i+1] + (1 - 2 * alpha) * rho[i] + alpha * rho[i-1]

        rho = rho_new   
    
        if j * dt in time_points:
            results[j * dt] = rho.copy()

elif metoda == "implicitna":
    for n in range(1, num_steps + 1):
        matrica = np.zeros((N, N))
        for i in range(N):
            if i > 0:
                matrica[i, i - 1] = -alpha
            matrica[i, i] = 1 + 2 * alpha
            if i < N - 1:
                matrica[i, i + 1] = -alpha
        rho_inner = rho[1:-1]
        rho_inner_new = np.linalg.solve(matrica, rho_inner)
        rho[1:-1] = rho_inner_new
        if n * dt in time_points:
            results[n * dt] = rho.copy()

plt.figure(figsize=(10, 6))
for time, data in results.items():
    plt.plot(x, data, label=f't = {time} s')

plt.xlabel('x / m')
plt.ylabel('$\\rho(x, t)$ / kg/m')
plt.title('{} metoda'.format(metoda.capitalize()))
plt.legend()
plt.grid(True)
plt.show()
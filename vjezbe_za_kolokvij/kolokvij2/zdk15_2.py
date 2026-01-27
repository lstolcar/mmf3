import numpy as np
import matplotlib.pyplot as plt

metoda = "implicitna" 
A = 0.02 
L = 20  
T_final = 500
dt = 0.5

N = 100
dx = 0.15
x = np.linspace(0, L, N + 2) 
alpha = A * dt / dx**2

def initial_condition(x_val):
    return -0.1 * x_val**2 + 2 * x_val

rho = np.vectorize(initial_condition)(x)

# vremenski trenuci za ispis
time_points = [150*dt, 300*dt, 450*dt]
results = {0.0: rho.copy()}

num_steps = int(T_final / dt)

# ---- TABLICA PROMJENJIVIH RUBNIH UVJETA ----
# vrijeme -> (lijevi rub, desni rub)
rubni_uvjeti = {
    150*dt: (1.0, 0.5),
    300*dt: (0.5, 0.2),
    450*dt: (0.2, 0.0)
}

if metoda == "eksplicitna":
    for j in range(1, num_steps + 1):
        rho_new = rho.copy()
        for i in range(1, N + 1):
            rho_new[i] = (
                alpha * rho[i+1]
                + (1 - 2 * alpha) * rho[i]
                + alpha * rho[i-1]
            )

        rho = rho_new

        # ---- PRIMJENA PROMJENJIVIH RUBNIH UVJETA ----
        rho[0], rho[-1] = rubni_uvjeti.get(j*dt, (rho[0], rho[-1]))

        if j * dt in time_points:
            results[j * dt] = rho.copy()

elif metoda == "implicitna":
    # matrica je stalna pa je gradimo jednom
    matrica = np.zeros((N, N))
    for i in range(N):
        if i > 0:
            matrica[i, i - 1] = -alpha
        matrica[i, i] = 1 + 2 * alpha
        if i < N - 1:
            matrica[i, i + 1] = -alpha

    for n in range(1, num_steps + 1):
        rho_inner = rho[1:-1]
        rho_inner_new = np.linalg.solve(matrica, rho_inner)
        rho[1:-1] = rho_inner_new

        # ---- PRIMJENA PROMJENJIVIH RUBNIH UVJETA ----
        rho[0], rho[-1] = rubni_uvjeti.get(n*dt, (rho[0], rho[-1]))

        if n * dt in time_points:
            results[n * dt] = rho.copy()

# ---- CRTANJE ----
plt.figure(figsize=(10, 6))
for time, data in results.items():
    plt.plot(x, data, label=f't = {time} s')

plt.xlabel('x / m')
plt.ylabel(r'$\rho(x, t)$ / kg/m')
plt.title(f'{metoda.capitalize()} metoda')
plt.legend()
plt.grid(True)
plt.show()

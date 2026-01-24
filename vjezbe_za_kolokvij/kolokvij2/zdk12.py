import numpy as np
import matplotlib.pyplot as plt


def simulacija():
    t0, tN = 0, 4
    N = 100
    h = (tN - t0) / N
    t = np.linspace(t0, tN, N+1)



    y_pk  = np.zeros(N+1)
    

    def f(x_values):
        return 2*x_values

    for n in range(N):
        # Prediktor–korektor (Heun)

        y_pk[n+1] = y_pk[n] + h/2 * (f(n*h) + f(n*h + h))

        
        


    # --- GRAF ---
    i_start, i_end = int(t0/h), int(tN/h)
    t_plot = t[i_start:i_end+1]

    plt.figure(figsize=(10,6))

    plt.scatter(t_plot, y_pk[i_start:i_end+1], label="PK", linewidth=2)
    plt.title(f"N={N}")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()

simulacija()
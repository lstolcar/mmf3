import numpy as np
import matplotlib.pyplot as plt
import math as mt

def skok_padobranca_rk4(m=80, h0=6000, g=9.81, rho=1.225, Cd=1.0, A_osoba=0.7, A_padobran=44.0, h_otvaranja=30, t_max=300):
    dt = 0.01
    N = int(t_max / dt)  
    t = np.linspace(0, t_max, N+1)

    y = np.zeros((2, N+1))  
    y[0, 0] = h0 
    y[1, 0] = 0
    
   
    t_start_otvaranja = -1 
    vrijeme_inflacije = 3.0 

    for n in range(N):
        if y[0, n] <= 0:
            break

        
        if y[0, n] <= h_otvaranja and t_start_otvaranja == -1:
            t_start_otvaranja = t[n]

        
        def f(y_trenutno, t_trenutno):
            visina = y_trenutno[0]
            brzina = y_trenutno[1]
            
           
            if t_start_otvaranja == -1:
                A = A_osoba
            else:
                progres = (t_trenutno - t_start_otvaranja) / vrijeme_inflacije
                progres = min(1.0, max(0.0, progres)) 
                A = A_osoba + (A_padobran - A_osoba) * progres

            k_trenutno = 0.5 * rho * Cd * A
            return np.array([brzina, -g + (k_trenutno/m) * brzina**2])

        k1 = f(y[:, n], t[n])
        k2 = f(y[:, n] + 0.5*dt*k1, t[n] + 0.5*dt)
        k3 = f(y[:, n] + 0.5*dt*k2, t[n] + 0.5*dt)
        k4 = f(y[:, n] + dt*k3, t[n] + dt)

        y[:, n+1] = y[:, n] + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

    return t[:n+1], y[:, :n+1]

vrijeme, rezultati = skok_padobranca_rk4()

visina = rezultati[0]
brzina = rezultati[1]


plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.plot(vrijeme, visina, color='blue', label='Visina (m)')
plt.axhline(1000, color='red', linestyle='--', label='Otvaranje padobrana')
plt.title('Visina padobranca kroz vrijeme')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Visina (m)')
plt.grid(True)
plt.legend()


plt.subplot(1, 2, 2)
plt.plot(vrijeme, np.abs(brzina), color='green', label='Brzina (m/s)')
plt.title('Brzina padobranca kroz vrijeme')
plt.xlabel('Vrijeme (s)')
plt.ylabel('Brzina (m/s)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
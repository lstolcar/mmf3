import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Wedge 

def skok_padobranca_rk4(m=80, h0=6000, g=9.81, rho=1.225, A_osoba=0.7, A_padobran=25.0, h_otvaranja=1000, t_max=300,N=10000):
    dt = t_max / N 
    t = np.linspace(0, t_max, int(N)+1)
    y = np.zeros((2, int(N)+1))  
    y[0, 0] = h0 
    y[1, 0] = 0
    t_start_otvaranja = -1 
    vrijeme_inflacije = 3.0 
    for n in range(int(N)):
        if y[0, n] <= 0:
            break
        if y[0, n] <= h_otvaranja and t_start_otvaranja == -1:
            t_start_otvaranja = t[n]
        def f(y_trenutno, t_trenutno):
            visina = y_trenutno[0]
            brzina = y_trenutno[1]
            
            if t_start_otvaranja == -1:
                A = A_osoba
                Cd = 1.0
            else:
                progres = (t_trenutno - t_start_otvaranja) / vrijeme_inflacije
                progres = min(1.0, max(0.0, progres)) 
                A = A_osoba + (A_padobran - A_osoba) * progres
                Cd = 1.0 + 0.5 * progres

            k_trenutno = 0.5 * rho * Cd * A
            return np.array([brzina, -g + (k_trenutno/m) * brzina**2])

        k1 = f(y[:, n], t[n])
        k2 = f(y[:, n] + 0.5*dt*k1, t[n] + 0.5*dt)
        k3 = f(y[:, n] + 0.5*dt*k2, t[n] + 0.5*dt)
        k4 = f(y[:, n] + dt*k3, t[n] + dt)

        y[:, n+1] = y[:, n] + (dt/6)*(k1 + 2*k2 + 2*k3 + k4)

    return t[:n+1], y[:, :n+1] , m, h0, N, h_otvaranja

vrijeme, rezultati, m, h0, N, h_otvaranja = skok_padobranca_rk4()

visina = rezultati[0]
brzina = rezultati[1]


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(vrijeme, visina, color='blue', label='Visina(m)')
plt.axhline(h_otvaranja, color='red', linestyle='--', label='Otvaranje padobrana')
plt.title('Visina padobranca kroz vrijeme, N={}, h0={}m'.format(N, h0), fontsize=15)
plt.xlabel('Vrijeme (s)', fontsize=25)
plt.ylabel('Visina (m)', fontsize=25)
plt.grid(True)
plt.legend(fontsize=20)

plt.subplot(1, 2, 2)
plt.plot(vrijeme, np.abs(brzina), color='green', label='Brzina (m/s)')
plt.title('Brzina padobranca kroz vrijeme, N={}, h0={}m'.format(N, h0), fontsize=15)
plt.xlabel('Vrijeme (s)', fontsize=25)
plt.ylabel('Brzina (m/s)', fontsize=25)
plt.grid(True)
plt.legend(fontsize=20)

plt.tight_layout()
plt.show()


plt.plot(vrijeme, m*9.81*visina, label='Potencijalna energija (J)')
plt.plot(vrijeme, 0.5*m*brzina**2, label='Kinetička energija (J)')
plt.plot(vrijeme, m*9.81*h0-0.5*m*brzina**2-m*9.81*visina, label='Gubitak energije (J)')
plt.title('Energija padobranca', fontsize=25)
plt.xlabel('Vrijeme (s)')
plt.ylabel('Energija (J)')
plt.grid(True)
plt.legend()
plt.show()


fig, ax = plt.subplots(figsize=(5, 8))

ax.set_xlim(-1, 1)
ax.set_ylim(0, max(visina) * 1.05)
ax.set_ylabel('Visina (m)', fontsize=20)
ax.set_title('Animacija skoka padobranca', fontsize=20)
ax.grid(True)

ax.plot([0,0],[0,max(visina)], linestyle='--')

point, = ax.plot(0, visina[0], 'ro', markersize=10)


padobran = Wedge(center=(0, visina[0]), r=1000, theta1=0, theta2=180, color='orange', alpha=0.6)
padobran.set_visible(False)
ax.add_patch(padobran)

text_label = ax.text(0.05, 0.80, '', transform=ax.transAxes, fontsize=15)
ax.axhline(h_otvaranja, color='red', linestyle='--', label='Otvaranje padobrana')
ax.legend()

def init():
    point.set_data([0], [visina[0]])
    text_label.set_text('')
    padobran.set_visible(False)
    return point, text_label, padobran

def animate(i):
    point.set_data([0], [visina[i]])

    text_label.set_text(
        f'Vrijeme: {vrijeme[i]:.1f} s\n'
        f'Visina: {visina[i]:.1f} m\n'
        f'Brzina: {brzina[i]:.1f} m/s'
    )

    if visina[i] <= h_otvaranja:
        padobran.set_visible(True)

        
        progres = min(1.0, (h_otvaranja - visina[i]) / 300)
        padobran.set_radius(0.04 + 0.12 * progres)

        padobran.set_center((0, visina[i] + 100))
    else:
        padobran.set_visible(False)

    return point, text_label, padobran

step = 10  
indeksi = range(0, len(vrijeme), step)

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=indeksi,
    init_func=init,
    interval=10,
    blit=True
)

ani.save('skok_padobranca.gif', writer='pillow', fps=30)

plt.show()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

def skok_padobranca_rk4(m=80, h0=6000, g=9.81, rho=1.225, A_osoba=0.7, A_padobran=44.0, h_otvaranja=1000, t_max=300):
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

    return t[:n+1], y[:, :n+1] , m, h0

vrijeme, rezultati, m, h0 = skok_padobranca_rk4()

visina = rezultati[0]
brzina = rezultati[1]


plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.plot(vrijeme, visina, color='blue', label='Visina (m)')
plt.axhline(1000, color='red', linestyle='--', label='Otvaranje padobrana')
plt.title('Visina padobranca kroz vrijeme', fontsize=25)
plt.xlabel('Vrijeme (s)', fontsize=25)
plt.ylabel('Visina (m)', fontsize=25)
plt.grid(True)
plt.legend(fontsize=20)


plt.subplot(1, 2, 2)
plt.plot(vrijeme, np.abs(brzina), color='green', label='Brzina (m/s)')
plt.title('Brzina padobranca kroz vrijeme', fontsize=25)
plt.xlabel('Vrijeme (s)', fontsize=25)
plt.ylabel('Brzina (m/s)', fontsize=25)
plt.grid(True)
plt.legend(fontsize=20)

plt.tight_layout()
plt.show()

plt.plot(vrijeme, m*9.81*visina, color='purple', label='Potencijalna energija (J)')
plt.plot(vrijeme, 0.5*m*brzina**2, color='orange', label='Kinetička energija (J)')
plt.plot(vrijeme, m*9.81*h0-0.5*m*brzina**2-m*9.81*visina, color='cyan', label='Gubitak energije (J)')
plt.title('Energija padobranca kroz vrijeme', fontsize=25)
plt.xlabel('Vrijeme (s)', fontsize=25)
plt.ylabel('Energija (J)', fontsize=25)
plt.grid(True)
plt.legend(fontsize=20)
plt.show()

fig, ax = plt.subplots(figsize=(5, 8))

ax.set_xlim(-1, 1)
ax.set_ylim(0, max(visina) * 1.05)
ax.set_ylabel('Visina (m)', fontsize=25)
ax.set_title('Animacija skoka padobranca',fontsize=25)
ax.grid(True)


ax.plot([0,0],[0,max(visina)], color='gray', linestyle='--')


point, = ax.plot(0, visina[0], 'ro', markersize=12)


text_label = ax.text(0.05, 0.80, '', transform=ax.transAxes, fontsize=20)

ax.axhline(1000, color='red', linestyle='--', label='Padobranac')
ax.legend(fontsize=20)

def init():
    point.set_data([0], [visina[0]])
    text_label.set_text('')
    return point, text_label

def animate(i):

    point.set_data([0], [visina[i]])

    trenutna_visina = visina[i]
    trenutna_brzina = brzina[i]

    text_label.set_text(
        f'Vrijeme: {vrijeme[i]:.1f} s\n'
        f'Visina: {trenutna_visina:.1f} m\n'
        f'Brzina: {trenutna_brzina:.1f} m/s'
    )

    return point, text_label

step = 10  
indeksi = range(0, len(vrijeme), step)

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=indeksi,          
    init_func=init,
    interval=0.001,          
    blit=True,
    repeat=True
)

plt.show()
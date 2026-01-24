import numpy as np
import matplotlib.pyplot as plt

def simulacija():
    t0, tN = 0, 20
    N = 50
    h = (tN - t0) / N
    t = np.linspace(t0, tN, N+1)
    k=80e-3
    b=4e-3
    m=20e-3
    
    iks = np.zeros((2, N+1))
    
    iks[0,0] = 5e-2 # pozicija x
    iks[1,0] = 0 # brzina v

    
    def f_acc(x, v):
        return -(k/m)*x - (b/m)*v

    
    for n in range(N):
        
        k1_x = h * iks[1,n]
        k1_v = h * f_acc(iks[0,n], iks[1,n])

        k2_x = h * (iks[1,n] + 0.5*k1_v)
        k2_v = h * f_acc(iks[0,n] + 0.5*k1_x, iks[1,n] + 0.5*k1_v)

        k3_x = h * (iks[1,n] + 0.5*k2_v)
        k3_v = h * f_acc(iks[0,n] + 0.5*k2_x, iks[1,n] + 0.5*k2_v)

        k4_x = h * (iks[1,n] + k3_v)
        k4_v = h * f_acc(iks[0,n] + k3_x, iks[1,n] + k3_v)

        
        iks[0,n+1] = iks[0,n] + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
        iks[1,n+1] = iks[1,n] + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6

    
    akceleracija= -(k/m)*iks[0,:]-(b/m)*iks[1,:]

    def analiticka(x):
        w = np.sqrt(399)

        brojnik = (np.sin(w * x / 10) / (20 * w)) + (np.cos(w * x / 10) / 20)
        nazivnik = np.exp(x / 10)

        return brojnik / nazivnik

    
    print(f"Vremenski korak (h): {h:.6f}")
    print(f"Konačni položaj x(5s): {iks[0,-1]:.6f} m")
    print(f"Konačna brzina v(5s): {iks[1,-1]:.6f} m/s")

    plt.figure(figsize=(10, 6))
    plt.plot(t, iks[0,:], label="Položaj (x) [m]", linewidth=2)
    plt.plot(t, analiticka(t),'--' , label='Analiticko', linewidth=2)
    #plt.plot(t, iks[1,:], label="Brzina (v) [m/s]", linewidth=2)
    #plt.plot(t, akceleracija, '--', label="Akceleracija (a) [m/s²]", linewidth=2)
    
    plt.xlabel("Vrijeme (t) [s]")
    plt.ylabel("Vrijednosti")
    plt.title("Simulacija gibanja tijela (RK4)")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()
    
    greska = np.abs(iks[0,:] - analiticka(t))
    print(f"Maksimalna greška: {np.max(greska):.2e} m") 

    plt.figure(figsize=(10, 4))
    plt.plot(t, greska, color='red')
    plt.title("Iznos numeričke pogreške (Absolutno odstupanje)")
    plt.xlabel("Vrijeme [s]")
    plt.ylabel("Greška [m]")
    plt.grid(True)
    plt.show()

simulacija()
import numpy as np
import matplotlib.pyplot as plt


m = 0.200 
l = 0.2484902028828339 
g = 9.81 
theta0_deg = 4.0 
theta0 = np.radians(theta0_deg) 
omega0 = 0.0

T = 2 * np.pi * np.sqrt(l / g)

t_start_plot = 17 * T
t_end_plot = 20 * T
t_max = 20 * T 
N = 20000
h = t_max / N
t_values = np.linspace(0, t_max, N+1)

def accel(theta):
    return -(g/l) * np.sin(theta)

theta_E = np.zeros(N+1)
omega_E = np.zeros(N+1)
theta_E[0], omega_E[0] = theta0, omega0

for i in range(N):
    a = accel(theta_E[i])
    theta_E[i+1] = theta_E[i] + omega_E[i] * h
    omega_E[i+1] = omega_E[i] + a * h

theta_JUG = np.zeros(N+1)
omega_JUG = np.zeros(N+1)
theta_JUG[0], omega_JUG[0] = theta0, omega0

for i in range(N):
    a = accel(theta_JUG[i])
    theta_JUG[i+1] = theta_JUG[i] + omega_JUG[i]*h + 0.5*a*(h**2)
    omega_JUG[i+1] = omega_JUG[i] + a*h

theta_RK4 = np.zeros(N+1)
omega_RK4 = np.zeros(N+1)
theta_RK4[0], omega_RK4[0] = theta0, omega0

def f_sys(state):
    th, om = state
    return np.array([om, -(g/l)*np.sin(th)])

for i in range(N):
    y_curr = np.array([theta_RK4[i], omega_RK4[i]])
    
    k1 = f_sys(y_curr)
    k2 = f_sys(y_curr + 0.5 * h * k1)
    k3 = f_sys(y_curr + 0.5 * h * k2)
    k4 = f_sys(y_curr + h * k3)
    
    y_next = y_curr + (h/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    
    theta_RK4[i+1] = y_next[0]
    omega_RK4[i+1] = y_next[1]

mask = (t_values >= t_start_plot) & (t_values <= t_end_plot)

plt.figure(figsize=(10, 8))
plt.plot(theta_E[mask], omega_E[mask], label='Euler (EN)', linestyle='--', alpha=0.7)
plt.plot(theta_JUG[mask], omega_JUG[mask], label='JUG (Uniform Accel)', linestyle='-.', alpha=0.7)
plt.plot(theta_RK4[mask], omega_RK4[mask], label='Runge-Kutta 4 (RK4)', linewidth=1.5, color='black')

plt.title(f'Fazni prostor (17.-20. titraj), N={N}')
plt.xlabel('Kut [rad]')
plt.ylabel('Kutna brzina [rad/s]')
plt.legend()
plt.grid(True)
plt.show()
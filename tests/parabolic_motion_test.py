import numpy as np
import matplotlib.pyplot as plt

def runge_kutta4(f, y0, t):
    y0 = np.array(y0, dtype=float) 
    y = np.zeros((len(t), len(y0)))
    y[0] = y0
    for i in range(1, len(t)):
        h = t[i] - t[i-1]
        k1 = np.array(f(y[i-1], t[i-1]))
        k2 = np.array(f(y[i-1] + 0.5 * h * k1, t[i-1] + 0.5 * h))
        k3 = np.array(f(y[i-1] + 0.5 * h * k2, t[i-1] + 0.5 * h))
        k4 = np.array(f(y[i-1] + h * k3, t[i-1] + h))
        y[i] = y[i-1] + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
    return y

# Parameters
v0 = 20.0    # Vinitial velocity (m/s)
theta = 45   # Launch angle (grades)
g = 9.81     # Gravity (m/s²)
t_max = 3.0  # Maximum time (s)
dt = 0.01    # Passage of time (s)

# Initial conditions
vy0 = v0 * np.sin(np.radians(theta))
vx0 = v0 * np.cos(np.radians(theta))
y0 = [0, vx0, 0, vy0]  # [x, vx, y, vy]

# System of equations
def derivadas(y, t):
    return [y[1], 0, y[3], -g]

# Simulation
t = np.arange(0, t_max, dt)
sol = runge_kutta4(derivadas, y0, t)

# Results
x = sol[:, 0]
y = sol[:, 2]

# Graphic
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'g-', linewidth=2)
plt.title("Trajectory of a Projectile")
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.axis('equal')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

# Parameters  
k = 1.0      # Spring constant (N/m)
alpha = 0.1  # Damping coefficient
x0 = 2.0     # Starting position (m)
v0 = 0.0     # Initial velocity (m/s)
t_max = 20.0 # Maximum time (s)
dt = 0.01    # Passage of time (s)

# Initialization
t = np.arange(0, t_max + dt, dt)
x = np.zeros_like(t)
v = np.zeros_like(t)
x[0], v[0] = x0, v0

# Euler's method
for i in range(1, len(t)):
    x[i] = x[i-1] + v[i-1] * dt
    v[i] = v[i-1] + (-k * x[i-1] - alpha * v[i-1]) * dt

# Graphics
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(t, x, 'r-', label='Posición')
plt.xlabel("Tiempo (s)")
plt.ylabel("x(t)")
plt.title("Posición vs. Tiempo")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x, v, 'b-')
plt.xlabel("Posición (m)")
plt.ylabel("Velocidad (m/s)")
plt.title("Espacio Fase")
plt.grid(True)
plt.tight_layout()
plt.show()
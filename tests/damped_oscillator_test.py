import numpy as np
import matplotlib.pyplot as plt

# Parámetros
k = 1.0      # Constante del resorte (N/m)
alpha = 0.1  # Coeficiente de amortiguamiento
x0 = 2.0     # Posición inicial (m)
v0 = 0.0     # Velocidad inicial (m/s)
t_max = 20.0 # Tiempo máximo (s)
dt = 0.01    # Paso de tiempo (s)

# Inicializaciónw
t = np.arange(0, t_max + dt, dt)
x = np.zeros_like(t)
v = np.zeros_like(t)
x[0], v[0] = x0, v0

# Método de Euler
for i in range(1, len(t)):
    x[i] = x[i-1] + v[i-1] * dt
    v[i] = v[i-1] + (-k * x[i-1] - alpha * v[i-1]) * dt

# Gráficos
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
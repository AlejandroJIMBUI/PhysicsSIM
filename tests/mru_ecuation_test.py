import matplotlib.pyplot as plt
import numpy as np

# Parámetros
x0 = 5.0    # Posición inicial (m)
v = 10.0    # Velocidad (m/s)
t_max = 5.0 # Tiempo máximo (s)
dt = 0.1    # Paso de tiempo (s)

# Simulación
t = np.arange(0, t_max + dt, dt)
x = x0 + v * t

# Gráfico
plt.figure(figsize=(10, 5))
plt.plot(t, x, 'bo-', label='Posición')
plt.title("Movimiento Rectilíneo Uniforme")
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición (m)")
plt.grid(True)
plt.legend()
plt.show()
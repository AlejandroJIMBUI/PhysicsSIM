import numpy as np
import matplotlib.pyplot as plt

# Parámetros
N = 1000     # Número de pasos
dt = 0.1     # Paso de tiempo
sigma = 0.5  # Desviación estándar del paso

# Trayectoria aleatoria
dx = np.random.normal(0, sigma, N)
dy = np.random.normal(0, sigma, N)
x = np.cumsum(dx)
y = np.cumsum(dy)

# Gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', alpha=0.7)
plt.scatter(x[0], y[0], color='green', label='Inicio')
plt.scatter(x[-1], y[-1], color='red', label='Fin')
plt.title("Movimiento Browniano 2D")
plt.xlabel("Posición X")
plt.ylabel("Posición Y")
plt.grid(True)
plt.legend()
plt.show()
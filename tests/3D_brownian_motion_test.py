from vpython import sphere, vector, color, rate, canvas
import numpy as np

# Parámetros
N = 1000     # Número de pasos
dt = 0.1     # Paso de tiempo (no used in this simple simulation)
sigma = 0.5  # Desviación estándar del paso

scene = canvas(title='Movimiento Browniano 3D',
               width=800, height=600,
               center=vector(0,0,0),
               background=color.white)

# Generar pasos aleatorios en 3D
dx = np.random.normal(0, sigma, N)
dy = np.random.normal(0, sigma, N)
dz = np.random.normal(0, sigma, N)

# Posiciones acumuladas
x = np.cumsum(dx)
y = np.cumsum(dy)
z = np.cumsum(dz)

# Crear esfera para el punto inicial
start = sphere(pos=vector(x[0], y[0], z[0]), radius=0.3, color=color.green)

# Crear esfera para el punto final (se actualizará al final)
end = sphere(pos=vector(x[0], y[0], z[0]), radius=0.3, color=color.red)

# Crear esfera para la partícula en movimiento
particle = sphere(pos=vector(x[0], y[0], z[0]), radius=0.2, color=color.blue, make_trail=True, trail_color=color.blue)

# Animar el movimiento Browniano
for i in range(1, N):
    rate(100)  # Controla la velocidad de la animación
    particle.pos = vector(x[i], y[i], z[i])

# Actualizar la posición del punto final
end.pos = vector(x[-1], y[-1], z[-1])

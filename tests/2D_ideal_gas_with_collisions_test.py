from vpython import *
import numpy as np

# Parámetros
L = 30              # Tamaño de la caja
N = 20              # Número de partículas
radio = 0.5         # Radio de las partículas
max_vel = 5.0       # Velocidad máxima inicial

scene = canvas(width=800, height=600, range=L)
pared = box(pos=vector(0, 0, 0), size=vector(L, L, 0.1), color=color.blue, opacity=0.2)

# Inicializar partículas
particulas = []
for _ in range(N):
    pos = vector(np.random.uniform(-L/2 + radio, L/2 - radio),
                 np.random.uniform(-L/2 + radio, L/2 - radio),
                 0)
    vel = vector(np.random.uniform(-max_vel, max_vel),
                 np.random.uniform(-max_vel, max_vel),
                 0)
    particula = sphere(pos=pos, radius=radio, color=color.red, make_trail=True)
    particula.velocidad = vel
    particulas.append(particula)

dt = 0.01
while True:
    rate(100)
    for p in particulas:
        p.pos += p.velocidad * dt
        
        # Colisiones con las paredes
        if abs(p.pos.x) >= L/2 - radio:
            p.velocidad.x *= -1
        if abs(p.pos.y) >= L/2 - radio:
            p.velocidad.y *= -1
from vpython import sphere, vector, color, rate, canvas, arrow
import numpy as np

# Parámetros
k = 1.0      # Constante del resorte (N/m)
alpha = 0.1  # Coeficiente de amortiguamiento
x0 = vector(2.0, 0, 0)  # Posición inicial en 3D (m)
v0 = vector(0, 1.0, 0)  # Velocidad inicial en 3D (m/s)
t_max = 20.0 # Tiempo máximo (s)
dt = 0.01    # Paso de tiempo (s)

# Inicialización
t = np.arange(0, t_max + dt, dt)
N = len(t)
x = [x0]
v = [v0]

# Crear ventana 3D
scene = canvas(title='Oscilador Amortiguado 3D',
               width=800, height=600,
               center=vector(0,0,0),
               background=color.white)

# Crear esfera para la partícula
particle = sphere(pos=x0, radius=0.2, color=color.red, make_trail=True, trail_color=color.blue)

# Crear flechas para mostrar fuerzas (opcional)
force_spring = arrow(pos=particle.pos, axis=vector(0,0,0), color=color.green)
force_damping = arrow(pos=particle.pos, axis=vector(0,0,0), color=color.orange)

# Simulación con método de Euler en 3D
for i in range(1, N):
    rate(100)
    # Calcular fuerzas
    F_spring = -k * x[i-1]
    F_damping = -alpha * v[i-1]
    a = F_spring + F_damping

    # Actualizar velocidad y posición
    v_new = v[i-1] + a * dt
    x_new = x[i-1] + v[i-1] * dt

    v.append(v_new)
    x.append(x_new)

    # Actualizar posición de la partícula
    particle.pos = x_new

    # Actualizar flechas de fuerzas
    force_spring.pos = particle.pos
    force_spring.axis = F_spring

    force_damping.pos = particle.pos
    force_damping.axis = F_damping

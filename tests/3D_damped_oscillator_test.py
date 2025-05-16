from vpython import sphere, vector, color, rate, canvas, arrow
import numpy as np

# Parameters
k = 1.0      # Spring constant (N/m)
alpha = 0.1  # Damping coefficient
x0 = vector(2.0, 0, 0)  # Initial position in 3D (m)
v0 = vector(0, 1.0, 0)  # Initial velocity in 3D (m/s)
t_max = 20.0 # Maximum time (s)
dt = 0.01    # Passage of time (s)

# Initialization
t = np.arange(0, t_max + dt, dt)
N = len(t)
x = [x0]
v = [v0]

scene = canvas(title='3D Damped Oscillator',
               width=800, height=600,
               center=vector(0,0,0),
               background=color.white)

# Create sphere for the particle
particle = sphere(pos=x0, radius=0.2, color=color.red, make_trail=True, trail_color=color.blue)

# Create arrows to show forces (optional)
force_spring = arrow(pos=particle.pos, axis=vector(0,0,0), color=color.green)
force_damping = arrow(pos=particle.pos, axis=vector(0,0,0), color=color.orange)

# Simulation with the Euler method in 3D
for i in range(1, N):
    rate(100)
    # Calculate forces
    F_spring = -k * x[i-1]
    F_damping = -alpha * v[i-1]
    a = F_spring + F_damping

    # Update speed and position
    v_new = v[i-1] + a * dt
    x_new = x[i-1] + v[i-1] * dt

    v.append(v_new)
    x.append(x_new)

    # Update particle position
    particle.pos = x_new

    # Update force arrows
    force_spring.pos = particle.pos
    force_spring.axis = F_spring

    force_damping.pos = particle.pos
    force_damping.axis = F_damping

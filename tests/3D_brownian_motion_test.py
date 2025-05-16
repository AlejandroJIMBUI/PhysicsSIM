from vpython import sphere, vector, color, rate, canvas
import numpy as np

# Parameters
N = 1000     # Number of steps
dt = 0.1     # Time step (not used in this simple simulation)
sigma = 0.5  # Standard deviation of the step
scene = canvas(title='3D Brownian Motion',
               width=800, height=600,
               center=vector(0,0,0),
               background=color.white)

# Generate random steps in 3D
dx = np.random.normal(0, sigma, N)
dy = np.random.normal(0, sigma, N)
dz = np.random.normal(0, sigma, N)

# Accumulated positions
x = np.cumsum(dx)
y = np.cumsum(dy)
z = np.cumsum(dz)

# Create sphere for the initial point
start = sphere(pos=vector(x[0], y[0], z[0]), radius=0.3, color=color.green)

# Create sphere for end point (will be updated at the end)
end = sphere(pos=vector(x[0], y[0], z[0]), radius=0.3, color=color.red)

# Create sphere for the moving particle
particle = sphere(pos=vector(x[0], y[0], z[0]), radius=0.2, color=color.blue, make_trail=True, trail_color=color.blue)

# Animate Brownian motion
for i in range(1, N):
    rate(100)  # Controls the speed of the animation
    particle.pos = vector(x[i], y[i], z[i])

# Update the position of the end point
end.pos = vector(x[-1], y[-1], z[-1])

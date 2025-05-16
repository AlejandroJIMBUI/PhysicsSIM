import matplotlib.pyplot as plt
import numpy as np

# Parameters
x0 = 5.0    # Starting position (m)
v = 10.0    # Speed (m/s)
t_max = 5.0 # Maximum time (s)
dt = 0.1    # Passage of time (s)

# Simulation
t = np.arange(0, t_max + dt, dt)
x = x0 + v * t

# Graphic
plt.figure(figsize=(10, 5))
plt.plot(t, x, 'bo-', label='Position')
plt.title("Uniform Rectilinear Motion")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.legend()
plt.show()
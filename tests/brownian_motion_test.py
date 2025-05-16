import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 1000     # Number of steps
dt = 0.1     # Passage of time
sigma = 0.5  # Standard deviation of the step

# Random trajectory
dx = np.random.normal(0, sigma, N)
dy = np.random.normal(0, sigma, N)
x = np.cumsum(dx)
y = np.cumsum(dy)

# Graphic
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', alpha=0.7)
plt.scatter(x[0], y[0], color='green', label='Start')
plt.scatter(x[-1], y[-1], color='red', label='End')
plt.title("2D Brownian Motion")
plt.xlabel("Position X")
plt.ylabel("Position Y")
plt.grid(True)
plt.legend()
plt.show()
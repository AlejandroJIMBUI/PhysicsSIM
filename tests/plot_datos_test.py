import numpy as np
import matplotlib.pyplot as plt

# Load data from file
data = np.loadtxt('data/datos.txt', skiprows=1)

tiempo = data[:, 0]
altura = data[:, 1]
experimental = data[:, 2]

# Calculate margin of error
error = np.abs(altura - experimental)

# Graphing data
plt.figure(figsize=(12, 6))

plt.plot(tiempo, altura, 'o-', label='Height (m)')
plt.plot(tiempo, experimental, 's-', label='Experimental')

# Connect height points with experimental
for i in range(len(tiempo)):
    plt.plot([tiempo[i], tiempo[i]], [altura[i], experimental[i]], 'k--', alpha=0.5)

# Plot margin of error as error bar
plt.errorbar(tiempo, altura, yerr=error, fmt='o', ecolor='gray', alpha=0.5, label='Margin of error')

plt.title('Height and Experimental Data vs Time with Margin of Error')
plt.xlabel('Time (s)')
plt.ylabel('Height / Experimental')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

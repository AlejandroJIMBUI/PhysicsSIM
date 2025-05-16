import numpy as np
import matplotlib.pyplot as plt

# Cargar datos desde archivo
data = np.loadtxt('data/datos.txt', skiprows=1)

tiempo = data[:, 0]
altura = data[:, 1]
experimental = data[:, 2]

# Calcular margen de error
error = np.abs(altura - experimental)

# Graficar datos
plt.figure(figsize=(12, 6))

plt.plot(tiempo, altura, 'o-', label='Altura (m)')
plt.plot(tiempo, experimental, 's-', label='Experimental')

# Conectar puntos de altura con experimental
for i in range(len(tiempo)):
    plt.plot([tiempo[i], tiempo[i]], [altura[i], experimental[i]], 'k--', alpha=0.5)

# Graficar margen de error como barra de error
plt.errorbar(tiempo, altura, yerr=error, fmt='o', ecolor='gray', alpha=0.5, label='Margen de error')

plt.title('Datos de Altura y Experimental vs Tiempo con Margen de Error')
plt.xlabel('Tiempo (s)')
plt.ylabel('Altura / Experimental')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

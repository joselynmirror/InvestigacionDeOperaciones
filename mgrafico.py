# Importar las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt

# Definir las restricciones y la función objetivo
x = np.linspace(0, 20, 1000)
y1 = 10 * np.ones(len(x))
y2 = (12 - 3 * x) / 4

# Definir la función objetivo a maximizar
z = 9000 * x + 1200 * y2

# Graficar la región factible y la función objetivo
plt.plot(x, y1, label='X <= 20')
plt.plot(x, y2, label='3X + 4Y >= 12')
plt.fill_between(x, y1, y2, where=(y1 >= y2), alpha=0.2)
plt.plot(x, z, label='Función objetivo')
plt.xlim(0, 20)
plt.ylim(0, 15)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Problema de programación lineal')
plt.legend()

# Encontrar el punto óptimo
x_opt = round(np.max(x[z >= 36000]), 2)
y_opt = round((12 - 3 * x_opt) / 4, 2)
z_opt = round(9000 * x_opt + 1200 * y_opt, 2)
plt.scatter(x_opt, y_opt, color='r', label='Punto óptimo ({},{})'.format(x_opt, y_opt))
plt.annotate('Z = {}'.format(z_opt), xy=(x_opt, y_opt), xytext=(x_opt+1, y_opt-1),
             arrowprops=dict(facecolor='red', shrink=0.05))
plt.legend()

plt.show()
# Importar las bibliotecas necesarias
from scipy.optimize import minimize

# Definir la función objetivo y las restricciones
def funcion_objetivo(x):
    return 6 * x[0] + 2 * x[1]

def restriccion_1(x):
    return 0.5 * x[0] + 0.2 * x[1] - 4

def restriccion_2(x):
    return -2 * x[0] - 3 * x[1] + 20

def restriccion_3(x):
    return x[0] + x[1] - 10

# Definir el punto de partida para la optimización
x0 = [0, 0]

# Resolver el problema utilizando el método SLSQP a través de la función minimize
resultado = minimize(funcion_objetivo, x0, method='SLSQP', constraints=[{'type': 'ineq', 'fun': restriccion_1},                                                                 
                                                                        {'type': 'ineq', 'fun': restriccion_2},   
                                                                        {'type': 'eq', 'fun': restriccion_3}])

# Imprimir el resultado
if resultado.success:
    print("Solución óptima:")
    print("x =", round(resultado.x[0], 2))
    print("y =", round(resultado.x[1], 2))
    print("Valor óptimo de la función objetivo: Z =", round(resultado.fun, 2))
else:
    print("El problema no tiene solución óptima.")
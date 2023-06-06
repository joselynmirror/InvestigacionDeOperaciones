#Importar as bibliotecas necesarias
from scipy.optimize import linprog

# Definir los coeficientes de la función objetivo
c = [6, 2]

# Definir los coeficientes de las restricciones
A = [[1, 2], [3, 2]]
b = [4, 8]

# Definir los coeficientes de las variables adicionales y de holgura
c_fase1 = [0, 0, 1, 1, 0, 0]
A_fase1 = [[1, 2, 1, 0, 1, 0], [3, 2, 0, 1, 0, 1]]
b_fase1 = [4, 8]
# Resolver la fase 1 del método de dos fases
res_fase1 =linprog(c=c_fase1, A_ub=A_fase1, b_ub=b_fase1, method="simplex")
# Verificar si se encontró una solución óptima para la fase 1
if res_fase1.success:
    # Verificar si la solución es factible para el problema original
    if res_fase1.fun == 0:
        # Eliminar las variables adicionales y de holgura de la fase 1
        c_fase2 = c
        A_fase2 = A
        b_fase2 = b
        # Resolver la fase 2 del método de dos fases
        res_fase2 = linprog(c=c_fase2, A_ub=A_fase2, b_ub=b_fase2, method="simplex")
        # Imprimir la solución óptima de la fase 2
        print("Se encontró una solución óptima:")
        print(f"X = {res_fase2.x[0]}, Y = {res_fase2.x[1]}, Z = {res_fase2.fun}")
    else:
        # Imprimir un mensaje de error si la solución de la fase 1 no es factible
        print("El problema no tiene solución factible.")
else:
    # Imprimir un mensaje de error si no se encontró una solución óptima para la fase 1
    print("No se encontró una solución óptima para la fase 1.")
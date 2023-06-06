# Importar la biblioteca pulp
import pulp

# Definir los datos del problema
oferta = {"Silo 1": 15, "Silo 2": 25, "Silo 3": 10}
demanda = {"Molino 1": 5, "Molino 2": 15, "Molino 3": 15, "Molino 4": 15}
costos = {"Silo 1": {"Molino 1": 10, "Molino 2": 2, "Molino 3": 20, "Molino 4": 11},
          "Silo 2": {"Molino 1": 7, "Molino 2": 9, "Molino 3": 24, "Molino 4": 18},
          "Silo 3": {"Molino 1": 4, "Molino 2": 14, "Molino 3": 16, "Molino 4": 18}}

# Crear el problema de transporte
problema = pulp.LpProblem("Transporte", pulp.LpMinimize)

# Crear las variables de decisión
x = pulp.LpVariable.dicts("x", ((i, j) for i in oferta for j in demanda), lowBound=0, cat="Integer")

# Definir la función objetivo
problema += pulp.lpSum([x[(i, j)] * costos[i][j] for i in oferta for j in demanda]), "Costo total de transporte"

# Definir las restricciones de oferta
for i in oferta:
    problema += pulp.lpSum([x[(i, j)] for j in demanda]) <= oferta[i], f"Oferta de {i}"

# Definir las restricciones de demanda
for j in demanda:
    problema += pulp.lpSum([x[(i, j)] for i in oferta]) >= demanda[j], f"Demanda de {j}"

# Resolver el problema
problema.solve()

# Imprimir la solución
if problema.status == pulp.LpStatusOptimal:
    costo_minimo = pulp.value(problema.objective)
    print(f"El costo total de transporte mínimo es: {costo_minimo}")
    for i in oferta:
        for j in demanda:
            cantidad = x[(i, j)].varValue
            if cantidad > 0:
                print(f"Se deben transportar {cantidad} camiones cargados desde {i} hasta {j}.")
else:
    print("El problema no tiene solución óptima.")
import numpy as np
A = np.array([[10, 15],[20, 5]])
B = np.array([[5, 12],[15, 8]])
total= A + B
precio = 50
ingreso= total * precio

print("RESULTADOS CON NUMPY ")
print("Total de productos vendidos (Sábado + Domingo):")
print(total)

print("\nIngreso total en pesos:")
print(ingreso)

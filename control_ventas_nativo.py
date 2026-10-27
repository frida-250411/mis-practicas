A = [[10, 15],[20, 5]]
B = [[5, 12],[15, 8]]
precio = 50

total = [[A[i][j] + B[i][j] for j in range(2)]for i in range(2)]
ingreso = [[total[i][j] * precio for j in range(2)]for i in range(2)]

print("\nRESULTADOS CON PYTHON NATIVO")
print("Total de productos vendidos (Sábado + Domingo):")
for fila in total:
    print(fila)

print("\nIngreso total en pesos:")
for fila in ingreso:
    print(fila)

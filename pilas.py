pila = []

print("¿La pila está vacía?", len(pila) == 0)
for i in range(1, 11):
    pila.append(f"Taco {i}")

print("Pila después de agregar 10 elementos:", pila)
if len(pila) > 0:
    print("Elemento en la cima:", pila[-1])
else:
    print("La pila está vacía")

for _ in range(4):
    if len(pila) > 0:
        elemento_sacado = pila.pop()
        print("Se desapila:", elemento_sacado)

print("Pila después de sacar 4 elementos:", pila)

print("Cantidad de elementos restantes:", len(pila))
print("¿La pila está vacía?", len(pila) == 0)
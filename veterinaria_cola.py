from collections import deque
import time

cola_veterinaria = deque()

cola_veterinaria.append("Turno 1 - MAX - PERRO - LUIS HERNANDEZ")
cola_veterinaria.append("Turno 2 - LUNA - GATO - MARIA LOPEZ")
cola_veterinaria.append("Turno 3 - ROCKY - PERRO - CARLOS PEREZ")

print("Mascotas registradas en la veterinaria:")
for paciente in cola_veterinaria:
    print(" -", paciente)

print("\nIniciando atención veterinaria")

while len(cola_veterinaria) > 0:
    paciente = cola_veterinaria.popleft()

    print("\nLlamando a consulta:", paciente)

    time.sleep(1)

    print("Consulta finalizada:", paciente)
    print("(Mascotas restantes en la fila:",
          len(cola_veterinaria), ")")

print("\nTodas las mascotas han sido atendidas. Cola vacía.")
from collections import deque
import time
cola_reproduccion = deque()
#Agregar canciones a la cola
cola_reproduccion.append("1. Antologia")
cola_reproduccion.append("2. Viento")
cola_reproduccion.append("3. Primera Cita")
#MOSTRAR LAS CANCIONES EN ESPERA
print("Canciones en espera")
for cancion in cola_reproduccion:
    print("_",cancion)
    print("Iniciando reproduccción")
#EL REPRODUCTOR PROCESA LA COLA, CANCION POR CANCION
#DESENCOLAR
while cola_reproduccion:
    cancion_actual = cola_reproduccion.popleft()
    print(f"Sonando: {cancion_actual}")
    time.sleep(1) #Simule la duracion del tema
    print(f"Finalizo: {cancion_actual}")
    #MUESTRA CUANTAS CANCIONES QUEDAN EN LA COLA
    print(f"(Quedan: {len(cola_reproduccion)} canciones en la cola)")
    print("La cola de reproducción ha finalizado")
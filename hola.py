# Programa de saludo
print("¡Hola, Mundo!")

# Pedir un dato al usuario
nombre = input("¿Cómo te llamas? ")
print(f"Mucho gusto, {nombre}. ¡Bienvenido a Python!")
En Python, "burbuja" y "lo de pivote" hacen referencia a dos de los algoritmos de ordenamiento más conocidos: Ordenamiento de Burbuja (Bubble Sort) y Ordenamiento Rápido (Quicksort), el cual utiliza un elemento llamado pivote.
Aquí tienes la explicación sencilla y el código en Python para cada uno:

1. Ordenamiento de Burbuja (Bubble Sort)

Es el método más simple. Compara elementos adyacentes de la lista y los intercambia si están en el orden incorrecto. Los elementos más grandes "flotan" hacia el final de la lista como burbujas.
• Ventaja: Es muy fácil de entender.
• Desventaja: Es muy lento para listas grandes.
python
def ordenamiento_burbuja(lista):
    n = len(lista)
    # Recorremos todos los elementos de la lista
    for i in range(n):
        # Los últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Burbuja:", ordenamiento_burbuja(numeros))
Usa el código con precaución.

2. Ordenamiento con Pivote (Quicksort)

Es uno de los algoritmos más rápidos y eficientes. Funciona bajo la estrategia de "divide y vencerás":
1. Elige un elemento de la lista llamado pivote (puede ser el primero, el último o uno central).
2. Mueve todos los elementos menores que el pivote a su izquierda.
3. Mueve todos los elementos mayores que el pivote a su derecha.
4. Repite el proceso recursivamente con las sublistas izquierda y derecha.
• Ventaja: Es extremadamente rápido en la práctica.
• Desventaja: Es un poco más complejo de implementar de forma tradicional, aunque en Python se puede escribir de forma muy elegante.
python
def quicksort(lista):
    # Si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(lista) <= 1:
        return lista
    
    # Elegimos el elemento central como pivote
    pivote = lista[len(lista) // 2]
    
    # Separamos los elementos en tres listas
    izq = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    der = [x for x in lista if x > pivote]
    
    # Juntamos todo aplicando recursividad
    return quicksort(izq) + centro + quicksort(der)

# Ejemplo de uso
numeros = [64, 34, 25, 12, 22, 11, 90]
print("Quicksort (Pivote):", quicksort(numeros))
Usa el código con precaución.

Comparación rápida


Algoritmo	Velocidad (Listas grandes)	Complejidad	¿Cómo funciona?
Burbuja	Muy lento	Baja	Compara parejas de vecinos.
Quicksort (Pivote)	Muy rápido	Media-Alta	Divide la lista usando un centro (pivote).

Si te interesa, puedo ayudarte a analizar cómo cambia el rendimiento de Quicksort según el pivote que elijas o mostrarte cómo hacer que el algoritmo de burbuja sea más eficiente interrumpiendo el ciclo si la lista ya está ordenada. ¿Cuál de los dos te gustaría profundizar?

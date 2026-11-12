def maxima_profundidad(comentarios):
    if len(comentarios) == 0:
        return 0

    profundidad_maxima = 0
    for elem in comentarios:
        if isinstance(elem, list):
            profundidad = 1 + maxima_profundidad(elem)
        else:
            profundidad = 1

        if profundidad > profundidad_maxima:
            profundidad_maxima = profundidad

    return profundidad_maxima

hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
resultado = maxima_profundidad(hilo)
print("Profundidad máxima:", resultado)

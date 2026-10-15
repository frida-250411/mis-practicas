historial_navegador = []

# OPERACION APILAR PUSH
historial_navegador.append("google.com")
historial_navegador.append("youtube.com")
historial_navegador.append("wikipedia.org")
print("Historial cargado:", historial_navegador)

# OPERACION TOP PEEK
pagina_actual = historial_navegador[-1]
print("Pagina actual en pantalla:", pagina_actual)

# OPERACION DESAPILADA (POP)
pagina_cerrada = historial_navegador.pop()
print("Saliendo de:", pagina_cerrada)
print("Historial despues de presionar atras:", historial_navegador)

# OPERACION TAMAÑO (SIZE)
total_paginas = len(historial_navegador)
print("Paginas previas guardadas:", total_paginas)

# OPERACION VACIA (EMPTY)
sin_paginas = len(historial_navegador) == 0
print("El historial está vacío?", sin_paginas)
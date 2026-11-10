def limpiar_feed(publicaciones):

    if len(publicaciones) <= 1:
        return publicaciones
    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])
    else:
        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

feed = ["Post A", "Post B", "Post B", "Post C", "Post B"]

resultado = limpiar_feed(feed)
print(resultado)

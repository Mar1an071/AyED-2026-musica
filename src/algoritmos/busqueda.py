def busqueda_lineal(coleccion, clave, obtener_clave=None):

    extractor = obtener_clave if obtener_clave is not None else (lambda x: x)
    for elemento in coleccion:
        if extractor(elemento) == clave:
            return elemento
    return None


def busqueda_binaria(coleccion, clave, obtener_clave=None):

    extractor = obtener_clave if obtener_clave is not None else (lambda x: x)
    
    if not isinstance(coleccion, (list, tuple)):
        coleccion = list(coleccion)

    izq = 0
    der = len(coleccion) - 1

    while izq <= der:
        medio = (izq + der) // 2
        valor = extractor(coleccion[medio])

        if valor == clave:
            return coleccion[medio]
        elif valor < clave:
            izq = medio + 1
        else:
            der = medio - 1

    return None


def esta_ordenada(coleccion, obtener_clave=None):

    extractor = obtener_clave if obtener_clave is not None else (lambda x: x)
    anterior = None
    primero = True
    for elemento in coleccion:
        valor = extractor(elemento)
        if not primero and valor < anterior:
            return False
        anterior = valor
        primero = False
    return True

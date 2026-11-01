def ordenar_seleccion(coleccion, clave=None, obtener_clave=None):

    criterio = obtener_clave if obtener_clave is not None else clave
    extractor = criterio if criterio is not None else (lambda x: x)

    lista = list(coleccion)
    n = len(lista)

    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if extractor(lista[j]) < extractor(lista[pos_min]):
                pos_min = j
        lista[i], lista[pos_min] = lista[pos_min], lista[i]

    return lista


def ordenar_insercion(coleccion, clave=None, obtener_clave=None):

    criterio = obtener_clave if obtener_clave is not None else clave
    extractor = criterio if criterio is not None else (lambda x: x)

    lista = list(coleccion)
    n = len(lista)

    for i in range(1, n):
        actual = lista[i]
        valor_actual = extractor(actual)
        j = i - 1
        while j >= 0 and extractor(lista[j]) > valor_actual:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

    return lista

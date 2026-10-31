def ordenar_seleccion(coleccion, clave=None, obtener_clave=None):
    """Ordenamiento por selección (Selection Sort).
    
    Devuelve una nueva secuencia ordenada ascendentemente.
    Complejidad: O(n²) en todos los casos.
    Estabilidad: No estable (intercambia elementos no adyacentes).
    No utiliza sorted() ni list.sort().
    """
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
    """Ordenamiento por inserción (Insertion Sort).
    
    Devuelve una nueva secuencia ordenada ascendentemente.
    Complejidad: O(n) mejor caso (ya ordenado), O(n²) caso promedio y peor.
    Estabilidad: Sí es estable (mantiene el orden relativo con condición estricta >).
    No utiliza sorted() ni list.sort().
    """
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



def ordenar_seleccion(coleccion, obtener_clave):
    """
    Ordena la colección in-place mediante el algoritmo de Selección (ascendente).
    Algoritmo NO estable. Complejidad O(n²).
    """
    n = len(coleccion)
    for i in range(n - 1):
        pos_min = i
        for j in range(i + 1, n):
            if obtener_clave(coleccion[j]) < obtener_clave(coleccion[pos_min]):
                pos_min = j
        coleccion[i], coleccion[pos_min] = coleccion[pos_min], coleccion[i]
    return coleccion


def ordenar_insercion(coleccion, obtener_clave):
    """
    Ordena la colección in-place mediante el algoritmo de Inserción (ascendente).
    Algoritmo ESTABLE. Complejidad O(n) en el mejor caso, O(n²) en el peor.
    """
    for i in range(1, len(coleccion)):
        actual = coleccion[i]
        j = i - 1
        while j >= 0 and obtener_clave(coleccion[j]) > obtener_clave(actual):
            coleccion[j + 1] = coleccion[j]  
            j -= 1
        coleccion[j + 1] = actual  
    return coleccion
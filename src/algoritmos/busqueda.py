def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """Devuelve el elemento cuya clave es igual a 'clave', o None si no existe.
    
    Funciona sobre cualquier iterable de forma secuencial.
    No utiliza 'in' de Python sobre la colección ni .index().
    """
    extractor = obtener_clave if obtener_clave is not None else (lambda x: x)
    for elemento in coleccion:
        if extractor(elemento) == clave:
            return elemento
    return None


def busqueda_binaria(coleccion, clave, obtener_clave=None):
    """Búsqueda binaria sobre una colección ordenada por obtener_clave.
    
    REQUIERE que la colección esté ordenada previamente bajo el mismo criterio.
    Si recibe un iterable sin acceso aleatorio O(1) (como ListaEnlazada),
    se convierte a secuencia indexable en O(n).
    No utiliza el módulo bisect ni funciones de la biblioteca estándar.
    """
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



def busqueda_lineal(coleccion, clave, obtener_clave=None):
        
    for elemento in coleccion:
        if obtener_clave is None:
            if elemento == clave:
                return elemento
        elif obtener_clave(elemento) == clave:
            return elemento
    return None


def busqueda_binaria(coleccion, clave, obtener_clave):
    """
   
    """
    izq = 0
    der = len(coleccion) - 1
    
    while izq <= der:
        medio = (izq + der) // 2
        valor = obtener_clave(coleccion[medio])
        
        if valor == clave:
            return coleccion[medio]
        elif valor < clave:
            izq = medio + 1  
        else:
            der = medio - 1  
            
    return None  
from src.excepciones import ItemNoEncontradoError


def _base_titulo(titulo):
    return titulo.split("(")[0].strip()

def _recolectar_versiones(canciones, base_titulo, indice, resultado):
    if indice >= len(canciones):
        return resultado
    cancion = canciones[indice]
    if _base_titulo(cancion.titulo) == base_titulo:
        resultado.append(cancion)
    return _recolectar_versiones(canciones, base_titulo, indice + 1, resultado)

def cadena_versiones(biblioteca, id_origen):
    origen = biblioteca.buscar_id(id_origen)
    canciones = biblioteca.listar_canciones()
    base = _base_titulo(origen.titulo)
    resultado = []
    return _recolectar_versiones(canciones, base, 0, resultado)

def _mostrar_recursivo(canciones,indice):
    if indice >= len(canciones):
        return
    print(canciones[indice])
    _mostrar_recursivo(canciones,indice+1)


def mostrar_cadena_recursivo(canciones):
    if not canciones:
        raise ItemNoEncontradoError("No se encontraron canciones en la cadena.")
    _mostrar_recursivo(canciones, 0)



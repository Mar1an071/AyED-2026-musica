from src.excepciones import ItemNoEncontradoError


def recolectar_por_genero(canciones, genero, indice, resultado):
    if indice >= len(canciones):
        return resultado
    cancion = canciones[indice]
    if cancion.genero == genero:
        resultado.append(cancion)
    return recolectar_por_genero(canciones, genero, indice + 1, resultado)

def cadena_por_genero(biblioteca,id_origen):
    origen = biblioteca.buscar_id(id_origen)
    canciones = biblioteca.listar_canciones()
    indice_origen = -1
    for i in range(len(canciones)):
        if canciones[i].id == id_origen:
            indice_origen = i
            break
    if indice_origen == -1:
        raise ItemNoEncontradoError(f"No se encontró la canción con ID {id_origen}")
    resultado = [origen]
    return recolectar_por_genero(canciones, origen.genero, indice_origen + 1, resultado)


def mostrar_recursivo(canciones, indice):
    if indice >= len(canciones):
        return
    print(canciones[indice])
    mostrar_recursivo(canciones, indice + 1)

def mostrar_cadena_por_genero(canciones):
    if not canciones:
        print("sin resultados")
        return
    mostrar_recursivo(canciones,0)




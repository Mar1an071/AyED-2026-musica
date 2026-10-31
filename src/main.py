from src.config import TEMA
from src.dominio.biblioteca import Biblioteca
from src.persistencia.texto import cargar_csv
from src.excepciones import ItemNoEncontradoError
from src.dominio.recursion import cadena_versiones, mostrar_cadena_recursivo
from src.dominio.playlist import Playlist
from src.dominio.historial import Historial
from src.dominio.cola_reproduccion import ColaReproduccion
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError
from src.algoritmos.busqueda import busqueda_binaria, busqueda_lineal
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

CRITERIOS = {
    "1": ("Título", lambda c: c.titulo.lower()),
    "2": ("Artista", lambda c: c.artista.lower()),
    "3": ("Año", lambda c: c.anio),
    "4": ("Duración (seg)", lambda c: c.duracion_seg),
}

ALGORITMOS = {
    "1": ("selección", ordenar_seleccion),
    "2": ("inserción", ordenar_insercion),
}

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")

def cargar_biblioteca():
    biblioteca = Biblioteca()
    cargar_csv("data/canciones.csv",biblioteca)
    return biblioteca

def listar_canciones(biblioteca):
    for c in biblioteca.listar_canciones():
        print(c)
    
def ver_detalle(biblioteca):
    entrada = input("Ingrese el ID de la canción: ").strip()
    try:
        id_cancion = int(entrada)
    except ValueError:
        print("id invalido")
        return
    try:
        cancion = biblioteca.buscar_id(id_cancion)
        print(cancion)
    except ItemNoEncontradoError:
        print("Cancion no encontrada")

def operacion_recursiva(biblioteca):
    entrada = input("Ingrese el ID de la canción para ver sus canciones derivadas: ").strip()
    try:
        id_cancion = int(entrada)
    except ValueError:
        print("id invalido")
        return
    try:
        cadena = cadena_versiones(biblioteca, id_cancion)
        if not cadena:
            print("No se encontraron canciones derivadas.")
            return
        base = cadena[0].titulo.split("(")[0].strip()
        print(f"Versiones de '{base}': ({len(cadena)} canciones): ")
        mostrar_cadena_recursivo(cadena)
    except ItemNoEncontradoError:
        print("Cancion no encontrada")

def opcion_buscar(biblioteca):
    print()
    print("=== 3. Buscar ===")
    print("1. Por título (búsqueda lineal)")
    print("2. Por título (búsqueda binaria)")
    print("3. Volver al menú principal")
    opcion = input("> ").strip()
    if opcion == "3":
        return
    if opcion not in ("1", "2"):
        print("Opción inválida.")
        return

    consulta = input("Ingresá el título: ").strip()
    if not consulta:
        print("El título no puede estar vacío.")
        return

    clave = consulta.lower()
    obtener_titulo = lambda c: c.titulo.lower()

    if opcion == "1":
        resultado = busqueda_lineal(
            biblioteca.listar_canciones(), clave, obtener_clave=obtener_titulo
        )
        if resultado is None:
            print(f"No se encontró '{consulta}' (búsqueda lineal).")
        else:
            print(f"Encontrada (búsqueda lineal): {resultado}")
        return

    ordenadas = ordenar_insercion(
        biblioteca.listar_canciones(), obtener_clave=obtener_titulo
    )
    print("Catálogo ordenado por título (inserción); usando búsqueda binaria.")
    resultado = busqueda_binaria(ordenadas, clave, obtener_clave=obtener_titulo)
    if resultado is None:
        print(f"No se encontró '{consulta}' (búsqueda binaria).")
    else:
        print(f"Encontrada (búsqueda binaria): {resultado}")

def opcion_ordenar(biblioteca):
    print()
    print("=== 4. Ordenar ===")
    print("1. Por título")
    print("2. Por artista")
    print("3. Por año")
    print("4. Por duración")
    print("5. Volver al menú principal")
    criterio_opcion = input("Criterio > ").strip()
    if criterio_opcion == "5":
        return
    else:
        if criterio_opcion not in CRITERIOS:
            print("Opción inválida.")
            return
    nombre_criterio, obtener_clave = CRITERIOS[criterio_opcion]

    print("1. Selección (no estable)")
    print("2. Inserción (estable)")
    algoritmo_opcion = input("Algoritmo > ").strip()
    if algoritmo_opcion not in ALGORITMOS:
        print("Opción inválida.")
        return
    nombre_algoritmo, algoritmo = ALGORITMOS[algoritmo_opcion]

    ordenadas = algoritmo(biblioteca.listar_canciones(), obtener_clave=obtener_clave)
    print(f"Catálogo ordenado por {nombre_criterio.lower()} ({nombre_algoritmo}).")
    for cancion in ordenadas:
        print(cancion)

def opcion_playlist(biblioteca, playlist):
    while True:
        print()
        print("=== 6. Playlist (colección principal) ===")
        print("1. Listar canciones")
        print("2. Agregar canción")
        print("3. Quitar canción")
        print("4. Volver al menú principal")
        opcion = input("> ").strip()
        if opcion == "1":
            canciones = playlist.listar()
            if len(canciones) == 0:
                print("La playlist está vacía.")
            else:
                for c in canciones:
                    print(c)
        elif opcion == "2":
            entrada = input("Ingrese el ID de la canción a agregar: ").strip()
            try:
                id_cancion = int(entrada)
            except ValueError:
                print("id invalido")
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
                playlist.agregar_cancion(cancion)
                print(f"Canción '{cancion.titulo}' agregada a la playlist.")
            except ItemNoEncontradoError:
                print("Canción no encontrada.")
            except ColeccionLlenaError as e:
                print(e)
        elif opcion == "3":
            entrada = input("Ingrese el ID de la canción a quitar: ").strip()
            try:
                id_cancion = int(entrada)
            except ValueError:
                print("id invalido")
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
            except ItemNoEncontradoError:
                print("Canción no encontrada en el catálogo.")
                continue
            try:
                playlist.eliminar(cancion)
                print(f"Canción '{cancion.titulo}' eliminada de la playlist.")
            except ItemNoEncontradoError:
                print("Esa canción no está en la playlist.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def opcion_historial(historial):
    while True:
        print()
        print("=== 7. Historial (pila) ===")
        print("1. Ver el historial")
        print("2. Ver la última")
        print("3. Deshacer (sacar la última)")
        print("4. Volver al menú principal")
        opcion = input("> ").strip()
        if opcion == "1":
            if historial.esta_vacio():
                print("El historial está vacío.")
            else:
                for cancion in historial.listar():
                    print(cancion)
        elif opcion == "2":
            try:
                print(f"Última del historial: {historial.ver_ultima()}")
            except PilaVaciaError as e:
                print(e)
        elif opcion == "3":
            try:
                cancion = historial.deshacer_cancion()
                print(f"Deshecho: '{cancion.titulo}' salió del historial.")
            except PilaVaciaError as e:
                print(e)
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def opcion_cola(biblioteca, cola, historial):
    while True:
        print()
        print("=== 8. Cola de reproducción ===")
        print("1. Encolar canción")
        print("2. Reproducir siguiente")
        print("3. Volver al menú principal")
        opcion = input("> ").strip()
        if opcion == "1":
            entrada = input("ID de la canción a encolar: ").strip()
            try:
                id_cancion = int(entrada)
            except ValueError:
                print("id invalido")
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
            except ItemNoEncontradoError:
                print("Canción no encontrada.")
                continue
            cola.encolar_cancion(cancion)
            historial.registrar_cancion(cancion)
            print(f"Canción '{cancion.titulo}' encolada y registrada en el historial.")
        elif opcion == "2":
            try:
                cancion = cola.reproducir_siguiente()
                print(f"Reproduciendo: {cancion}")
            except ColaVaciaError as e:
                print(f"No se puede reproducir: {e}")
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar Canciones")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return
    biblioteca = cargar_biblioteca()
    playlist = Playlist(tope=6)
    historial = Historial()
    cola = ColaReproduccion()
    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            listar_canciones(biblioteca)
        elif opcion == "2":
            ver_detalle(biblioteca)
        elif opcion == "3":
            opcion_buscar(biblioteca)
        elif opcion == "4":
            opcion_ordenar(biblioteca)
        elif opcion == "5":
            operacion_recursiva(biblioteca)
        elif opcion == "6":
            opcion_playlist(biblioteca, playlist)
        elif opcion == "7":
            opcion_historial(historial)
        elif opcion == "8":
            opcion_cola(biblioteca, cola, historial)
        elif opcion == "9":
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()

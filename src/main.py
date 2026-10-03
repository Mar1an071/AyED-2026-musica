from src.config import TEMA
from src.dominio.biblioteca import Biblioteca
from src.persistencia.texto import cargar_csv
from src.excepciones import ItemNoEncontradoError
from src.dominio.recursion import cadena_versiones, mostrar_cadena_recursivo
from src.dominio.playlist import Playlist
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import ColeccionLlenaError, ColeccionVaciaError, PilaVaciaError, ColaVaciaError

TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
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

def opcion_playlist(biblioteca, playlist): 
    while True:
        print()
        print(f"=== Playlist: {playlist.nombre} ===")
        print("1. Listar canciones")
        print("2. Agregar canción")
        print("3. Quitar canción")
        print("4. Volver al menú principal")
        opcion = input("> ").strip()
        if opcion == "1":
            for c in playlist.listar_canciones():
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
            except ColeccionLlenaError:
                print("La playlist está llena. No se puede agregar más canciones.")
        elif opcion == "3":
            entrada = input("Ingrese el ID de la canción a quitar: ").strip()
            try:
                id_cancion = int(entrada)
            except ValueError:
                print("id invalido")
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
                playlist.quitar_cancion(cancion)
                print(f"Canción '{cancion.titulo}' eliminada de la playlist.")
            except ItemNoEncontradoError:
                print("Canción no encontrada en la playlist.")
            except ColeccionVaciaError:
                print("La playlist está vacía. No hay canciones para quitar.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def opcion_historial(biblioteca, historial):
    while True:
        print()
        print("=== Historial (Pila) ===")
        print("1. Listar canciones en el historial")
        print("2. Agregar canción al historial")
        print("3. Quitar canción del historial")
        print("4. Volver al menú principal")
        opcion = input("> ").strip()
        if opcion == "1":
            try:
                for c in historial.listar_canciones():
                    print(c)
            except PilaVaciaError:
                print("El Historial está vacío.")
        elif opcion == "2":
            entrada = input("ID de la canción a agregar al historial: ").strip()
            try:
                id_cancion = int(entrada)
            except ValueError:
                print("id invalido")
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
                historial.agregar_cancion(cancion)
                print(f"Canción '{cancion.titulo}' agregada al historial.")
            except ItemNoEncontradoError:
                print("Canción no encontrada.")
            except ColeccionLlenaError:
                print("El Historial está lleno, no se puede agregar más canciones.")
        elif opcion == "3":
            try:
                cancion = historial.quitar_cancion()
                print(f"Canción '{cancion.titulo}' eliminada del historial.")
            except PilaVaciaError:
                print("El Historial está vacío. No hay canciones para quitar.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def opcion_cola(biblioteca, cola):
    while True:
        print()
        print("=== Cola ===")
        print("1. Listar canciones en la cola")
        print("2. Agregar canción a la cola")
        print("3. Quitar canción de la cola")
        print("4. Volver al menú principal")
        opcion = input("> ").strip()
        if opcion == "1":
            try:
                for c in cola.listar_canciones():
                    print(c)
            except ColaVaciaError:
                print("La Cola está vacía.")
        elif opcion == "2":
            entrada = input("ID de la canción a agregar a la cola: ").strip()
            try:
                id_cancion = int(entrada)
            except ValueError:
                print("id invalido")
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
                cola.agregar_cancion(cancion)
                print(f"Canción '{cancion.titulo}' agregada a la cola.")
            except ItemNoEncontradoError:
                print("Canción no encontrada.")
            except ColeccionLlenaError:
                print("La Cola está llena, no se puede agregar más canciones.")
        elif opcion == "3":
            try:
                cancion = cola.quitar_cancion()
                print(f"Canción '{cancion.titulo}' eliminada de la cola.")
            except ColaVaciaError:
                print("La Cola está vacía. No hay canciones para quitar.")
        elif opcion == "4":
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
    playlist = opcion_playlist()
    historial = opcion_historial()
    cola = opcion_cola()
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
        elif opcion == "5":
            operacion_recursiva(biblioteca)
        elif opcion == "6":
            opcion_playlist(biblioteca, Playlist)
        elif opcion == "7":
            opcion_historial(biblioteca, Pila)
        elif opcion == "8":
            opcion_cola(biblioteca, Cola)
        elif opcion in {"3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()

from src.config import TEMA
from src.dominio.biblioteca import Biblioteca
from src.persistencia.texto import cargar_csv
from src.excepciones import ItemNoEncontradoError
from src.dominio.recursion import cadena_versiones, mostrar_cadena_recursivo
from src.dominio.playlist import Playlist
from src.dominio.historial import Historial
from src.dominio.cola_reproduccion import ColaReproduccion
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError

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
                playlist.eliminar(cancion)
                print(f"Canción '{cancion.titulo}' eliminada de la playlist.")
            except ItemNoEncontradoError:
                print("Canción no encontrada.")
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

def opcion_historial(biblioteca, historial):
    while True:
        print()
        print("=== 7. Historial (pila) ===")
        print("1. Registrar canción")
        print("2. Deshacer (sacar la última)")
        print("3. Volver al menú principal")
        opcion = input("> ").strip()
        if opcion == "1":
            entrada = input("ID de la canción a registrar: ").strip()
            try:
                id_cancion = int(entrada)
            except ValueError:
                print("id invalido")
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
                historial.registrar_cancion(cancion)
                print(f"Canción '{cancion.titulo}' registrada en el historial.")
            except ItemNoEncontradoError:
                print("Canción no encontrada.")
        elif opcion == "2":
            try:
                cancion = historial.deshacer_cancion()
                print(f"Deshecho: '{cancion.titulo}' salió del historial.")
            except PilaVaciaError as e:
                print(f"No se puede deshacer: {e}")
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

def opcion_cola(biblioteca, cola):
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
                cola.encolar_cancion(cancion)
                print(f"Canción '{cancion.titulo}' encolada.")
            except ItemNoEncontradoError:
                print("Canción no encontrada.")
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
        elif opcion == "5":
            operacion_recursiva(biblioteca)
        elif opcion == "6":
            opcion_playlist(biblioteca, playlist)
        elif opcion == "7":
            opcion_historial(biblioteca, historial)
        elif opcion == "8":
            opcion_cola(biblioteca, cola)
        elif opcion in {"3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()

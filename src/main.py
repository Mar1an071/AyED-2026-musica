from src.config import TEMA
from src.dominio.biblioteca import Biblioteca
from src.dominio.historial import Historial
from src.persistencia.texto import cargar_csv
from src.excepciones import ItemNoEncontradoError
from src.dominio.recursion import cadena_versiones, mostrar_cadena_recursivo
from src.dominio.playlist import Playlist
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.excepciones import ColeccionLlenaError, ColeccionVaciaError, PilaVaciaError, ColaVaciaError, ArchivoInvalidoError


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

def pedir_id(mensaje):
    entrada = input(mensaje).strip()
    try:
        return int(entrada)
    except ValueError:
        print("id invalido")
        return None


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

def opcion_playlist(biblioteca, playlist):
    playlist = Playlist()
    while True:
        print()
        print("--- 6. Colección principal: Playlist ---")
        print(f"1. Agregar canción   (tope {playlist.tamanio()}/{6})")
        print("2. Eliminar canción")
        print("3. Listar playlist")
        print("0. Volver")
        opcion = input("> ").strip()
        if opcion == "0":
            return
        elif opcion == "1":
            id_cancion = pedir_id("Ingrese el ID de la canción: ")
            if id_cancion is None:
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
                playlist.agregar(cancion)
                print(f"Agregado: {cancion.titulo}")
            except ArchivoInvalidoError as e:
                print(f"Archivo inválido: {e}")
            except ColeccionLlenaError as e:
                print(f"La playlist esta llena: {e}")
        elif opcion == "2":
            id_cancion = pedir_id("Ingrese el ID de la canción a quitar: ")
            if id_cancion is None:
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
                playlist.eliminar(cancion)
                print(f"Quitada: {cancion.titulo}")
            except ColeccionVaciaError as e:
                print(f"La playlist está vacía: {e}")
        elif opcion == "3":
            if playlist.esta_vacia():
                print("La playlist está vacía.")
                continue
            for i, cancion in enumerate(playlist.listar(), start=1):
                print(f"  {i}. {cancion}")
        else:
            print("Opción inválida.")

def opcion_historial(biblioteca, historial):
    pila = Pila()
    historial = Historial()
    while True:
        print()
        print("--- 7. Historial (pila / deshacer) ---")
        print("1. Registrar canción (reproducir)")
        print("2. Deshacer última")
        print("3. Ver la última sin sacarla")
        print("4. Ver cuántas hay en el historial")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return
        elif opcion == "1":
            id_cancion = pedir_id("Ingrese el ID de la canción a registrar: ")
            if id_cancion is None:
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
                historial.registrar_cancion(cancion)
                print(f"Registrada: {cancion.titulo}")
            except ArchivoInvalidoError as e:
                print(f"Archivo inválido: {e}")
        elif opcion == "2":
            try:
                cancion = historial.deshacer_cancion()
                print(f"Deshecho: {cancion}")
            except PilaVaciaError as e:
                print(f"No se puede deshacer: {e}")
        elif opcion == "3":
            try:
                cancion = historial.ver_ultima()
                print(f"Ultima del historial: {cancion}")
            except PilaVaciaError as e:
                print(f"No se puede deshacer: {e}")
        elif opcion == "4":
            print(f"Canciones en el historial: {historial.listar()}")
        else:
            print("Opción inválida.")

def opcion_cola(biblioteca, cola):
    cola = Cola()
    while True:
        print()
        print("--- 8. Cola de reproducción ---")
        print("1. Encolar canción")
        print("2. Reproducir siguiente")
        print("3. Ver la siguiente sin sacarla")
        print("4. Ver cuántas hay en cola")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            return
        elif opcion == "1":
            id_cancion = pedir_id("Ingrese el ID de la canción a encolar: ")
            if id_cancion is None:
                continue
            try:
                cancion = biblioteca.buscar_id(id_cancion)
                cola.encolar_cancion(cancion)
                print(f"Encolada: {cancion.titulo}")
            except ItemNoEncontradoError as e:
                print(f"No se encontro ese elemento: {e}")
        elif opcion == "2":
            try:
                cancion = cola.reproducir_siguiente()
                print(f"Reproduciendo: {cancion}")
            except ColaVaciaError as e:
                print(f"No se puede reproducir: {e}")
        elif opcion == "3":
            try:
                cancion = cola.ver_siguiente()
                print(f"La siguiente es: {cancion}")
            except ColaVaciaError as e:
                print(f"No se puede reproducir: {e}")
        elif opcion == "4":
            print(f"Canciones en cola: {cola.listar()}")
        else:
            print("Opción inválida.")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return
    biblioteca = cargar_biblioteca()
    historial = opcion_historial()
    cola = opcion_cola()
    playlist = opcion_playlist()
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

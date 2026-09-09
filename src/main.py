from src.config import TEMA
from src.dominio.biblioteca import Biblioteca
from src.persistencia.texto import cargar_csv
from src.excepciones import ItemNoEncontradoError

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
        elif opcion in {"3", "4", "5", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()

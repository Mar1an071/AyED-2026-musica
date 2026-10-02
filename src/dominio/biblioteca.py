from src.excepciones import ItemNoEncontradoError
from src.tads.lista_enlazada import ListaEnlazada
class Biblioteca:
    def __init__(self):
        self._canciones = ListaEnlazada()

    def agregar_canciones(self, cancion):
        self._canciones.insertar_al_final(cancion)

    def listar_canciones(self):
        return self._canciones
    
    def buscar_id(self, id):
        for c in self._canciones:
            if c.id == id:
                return c
        raise ItemNoEncontradoError("Cancion no encontrada")
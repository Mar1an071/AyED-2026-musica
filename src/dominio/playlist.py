from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError, ItemNoEncontradoError

class Playlist:
    def __init__(self, tope=6):
        self._canciones = ListaEnlazada()
        self._tope = tope

    def agregar_cancion(self, cancion):
        if self._canciones.tamanio() >= self._tope:
            raise ColeccionLlenaError(f"Playlist llena, máximo {self._tope} canciones")
        self._canciones.insertar_al_final(cancion)
    
    def eliminar(self, cancion):
        if not self._canciones.eliminar(cancion):
            raise ItemNoEncontradoError("Esa canción no está en la playlist.")

    def listar(self):
        return self._canciones

    def esta_vacia(self):
        return self._canciones.esta_vacia()


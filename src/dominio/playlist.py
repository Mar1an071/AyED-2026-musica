from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError

class Playlist:
    def __init__(self, tope=6):
        self._canciones = ListaEnlazada()
        self._tope = tope

    def agregar_cancion(self, cancion):
        if self._canciones.tamanio() >= self._tope:
            raise ColeccionLlenaError(f"Playlist llena, máximo {self._tope} canciones")
        self._canciones.insertar_al_final(cancion)
    
    def eliminar(self, cancion):
        self._canciones.eliminar(cancion)

    def listar(self):
        return self._canciones

    
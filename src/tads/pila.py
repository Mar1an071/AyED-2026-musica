from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError


class Pila:
    """Pila implementada sobre ListaEnlazada (LIFO)."""

    def __init__(self):
        self._items = ListaEnlazada()

    def apilar(self, dato):
        """Agrega al tope. Equivale a insertar_al_inicio en la lista."""
        self._items.insertar_al_inicio(dato)

    def desapilar(self):
        """Sacá el tope. Si la pila está vacía, lanzá PilaVaciaError."""
        if self.esta_vacia():
            raise PilaVaciaError("No hay elementos en el historial para deshacer.")
        tope = self._items._cabeza.dato
        self._items.eliminar(tope)
        return tope

    def ver_tope(self):
        """Mirá el del tope sin sacarlo."""
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()
    
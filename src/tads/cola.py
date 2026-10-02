class Cola:
    """Cola implementada sobre ListaEnlazada (FIFO)."""

    def __init__(self):
        self._items = ListaEnlazada()

    def encolar(self, dato):
        """Agrega al final de la cola."""
        self._items.insertar_al_final(dato)

    def desencolar(self):
        """Sacá del frente. Si la cola está vacía, lanzá ColaVaciaError."""
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")
        frente = self._items._cabeza.dato
        self._items.eliminar(frente)
        return frente

    def ver_frente(self):
        """Mirá el del frente sin sacarlo."""
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._items._cabeza.dato

    def esta_vacia(self):
        return self._items.esta_vacia()
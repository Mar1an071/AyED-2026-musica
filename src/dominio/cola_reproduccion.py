from src.tads.cola import Cola


class ColaReproduccion:
    def __init__(self):
        self._cola = Cola()

    def encolar_cancion(self, cancion):
        self._cola.encolar(cancion)

    def reproducir_siguiente(self):
        return self._cola.desencolar()
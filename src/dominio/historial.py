from src.tads.pila import Pila


class Historial:
    def __init__(self):
        self._pila = Pila()

    def registrar_cancion(self, cancion):
        self._pila.apilar(cancion)

    def deshacer_cancion(self):
        return self._pila.desapilar()
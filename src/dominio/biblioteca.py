from src.excepciones import ItemNoEncontradoError

class Biblioteca:
    def __init__(self):
        self.canciones = []

    def agregar_canciones(self, cancion):
        self.canciones.append(cancion)

    def listar_canciones(self):
        return self.canciones
    
    def buscar_id(self, id):
        for c in self.canciones:
            if c.id == id:
                return c
        raise ItemNoEncontradoError("Cancion no encontrada")
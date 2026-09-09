import csv
from pathlib import Path
from src.dominio.canciones import Cancion
from src.excepciones import ArchivoInvalidoError

def cargar_csv(ruta, biblioteca):
    """Carga secuencial. Devuelve una lista de dicts (E1 puede quedar así)."""
    try:
        with open(ruta, encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                c = Cancion(int(fila["id"]), fila["titulo"],fila["artista"],fila["album"],fila["genero"],int(fila["anio"]),int(fila["duracion_seg"]))
                biblioteca.agregar_canciones(c)
            return biblioteca
    except(FileNotFoundError, PermissionError, UnicodeDecodeError, csv.Error) as err:
        raise ArchivoInvalidoError(f"No se pudo cargar el archivo {ruta}: {err}") from err


def guardar_csv(ruta, filas, encabezados):
    raise NotImplementedError
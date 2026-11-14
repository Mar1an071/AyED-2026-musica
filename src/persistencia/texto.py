import csv
from pathlib import Path
from src.dominio.canciones import Cancion
from src.excepciones import ArchivoInvalidoError

RAIZ = Path(__file__).resolve().parent.parent.parent
DATA = RAIZ / "data"


def cargar_csv(ruta, biblioteca):
    try:
        with open(ruta, encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                c = Cancion(
                    int(fila["id"]),
                    fila["titulo"],
                    fila["artista"],
                    fila["album"],
                    fila["genero"],
                    int(fila["anio"]),
                    int(fila["duracion_seg"]),
                )
                biblioteca.agregar_canciones(c)
            return biblioteca
    except (FileNotFoundError, PermissionError, UnicodeDecodeError, csv.Error) as err:
        raise ArchivoInvalidoError(f"No se pudo cargar el archivo {ruta}: {err}") from err


def cargar_texto(ruta):
    ruta = Path(ruta)
    if not ruta.exists():
        raise ArchivoInvalidoError(f"No existe el archivo: {ruta}")

    filas = []
    try:
        with ruta.open("r", encoding="utf-8") as archivo:
            linea_encabezado = archivo.readline()
            if not linea_encabezado:
                raise ArchivoInvalidoError("El archivo está vacío.")
            encabezado = [c.strip() for c in linea_encabezado.strip().split(",")]

            for num_linea, linea in enumerate(archivo, start=2):
                linea = linea.strip()
                if not linea:
                    continue
                valores = [v.strip() for v in linea.split(",")]
                if len(valores) != len(encabezado):
                    raise ArchivoInvalidoError(
                        f"Línea {num_linea} con {len(valores)} campos "
                        f"(se esperaban {len(encabezado)}): {linea}"
                    )
                filas.append(dict(zip(encabezado, valores)))
        return filas
    except UnicodeDecodeError as err:
        raise ArchivoInvalidoError(f"Error de codificación en {ruta}: {err}") from err


def guardar_texto(ruta, filas, encabezados):
    ruta = Path(ruta)
    try:
        with ruta.open("w", encoding="utf-8", newline="") as archivo:
            archivo.write(",".join(encabezados) + "\n")
            for fila in filas:
                campos = [str(fila.get(clave, "")) for clave in encabezados]
                archivo.write(",".join(campos) + "\n")
    except (PermissionError, OSError) as err:
        raise ArchivoInvalidoError(f"No se pudo guardar el archivo {ruta}: {err}") from err


guardar_csv = guardar_texto

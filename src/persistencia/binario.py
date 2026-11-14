import struct
from src.dominio.canciones import Cancion
from src.excepciones import ArchivoInvalidoError, ItemNoEncontradoError

MAGIA = b"AYED"
TEMA_MUSICA = b"M"
HEADER_FMT = "<4s 1s I"
HEADER_SIZE = struct.calcsize(HEADER_FMT)

REGISTRO_FMT = "<I 50s 40s 35s 12s H H"
REGISTRO_SIZE = struct.calcsize(REGISTRO_FMT)


def _a_bytes(texto, ancho):
    datos = texto.encode("utf-8")[:ancho]
    return datos.ljust(ancho, b"\x00")


def _a_texto(campo_bytes):
    return campo_bytes.split(b"\x00", 1)[0].decode("utf-8")


def _cancion_a_tupla(cancion):
    return (
        cancion.id,
        _a_bytes(cancion.titulo, 50),
        _a_bytes(cancion.artista, 40),
        _a_bytes(cancion.album, 35),
        _a_bytes(cancion.genero, 12),
        cancion.anio,
        cancion.duracion_seg,
    )


def _tupla_a_cancion(tupla):
    id_, titulo_b, artista_b, album_b, genero_b, anio, duracion = tupla
    return Cancion(
        id=id_,
        titulo=_a_texto(titulo_b),
        artista=_a_texto(artista_b),
        album=_a_texto(album_b),
        genero=_a_texto(genero_b),
        anio=anio,
        duracion_seg=duracion,
    )


def posicion_del_id(catalogo, id_buscado):
    for posicion, item in enumerate(catalogo):
        if item.id == id_buscado:
            return posicion
    raise ItemNoEncontradoError(f"No hay ítem con id {id_buscado}")


def guardar_binario(ruta, items):
    canciones = list(items)
    with open(ruta, "wb") as f:
        header = struct.pack(HEADER_FMT, MAGIA, TEMA_MUSICA, len(canciones))
        f.write(header)
        for cancion in canciones:
            registro = struct.pack(REGISTRO_FMT, *_cancion_a_tupla(cancion))
            f.write(registro)


def cargar_binario(ruta):
    try:
        with open(ruta, "rb") as f:
            header_bytes = f.read(HEADER_SIZE)
            if len(header_bytes) < HEADER_SIZE:
                raise ArchivoInvalidoError(
                    f"Archivo truncado: se esperaban al menos {HEADER_SIZE} bytes de header."
                )

            magia, tema, cantidad = struct.unpack(HEADER_FMT, header_bytes)

            if magia != MAGIA:
                raise ArchivoInvalidoError(
                    f"Magia inválida: se esperaba {MAGIA!r}, se encontró {magia!r}."
                )

            if tema != TEMA_MUSICA:
                raise ArchivoInvalidoError(
                    f"Tema ajeno: se esperaba {TEMA_MUSICA!r}, se encontró {tema!r}."
                )

            canciones = []
            for i in range(cantidad):
                datos = f.read(REGISTRO_SIZE)
                if len(datos) < REGISTRO_SIZE:
                    raise ArchivoInvalidoError(
                        f"Archivo truncado en el registro {i + 1}: "
                        f"se esperaban {REGISTRO_SIZE} bytes, se leyeron {len(datos)}."
                    )
                tupla = struct.unpack(REGISTRO_FMT, datos)
                canciones.append(_tupla_a_cancion(tupla))

            return canciones

    except FileNotFoundError:
        raise ArchivoInvalidoError(f"No se encontró el archivo: {ruta}")


def actualizar_registro(ruta, posicion, cancion):
    offset = HEADER_SIZE + posicion * REGISTRO_SIZE
    registro = struct.pack(REGISTRO_FMT, *_cancion_a_tupla(cancion))
    with open(ruta, "r+b") as f:
        f.seek(0, 2)
        tamanio = f.tell()
        if offset + REGISTRO_SIZE > tamanio:
            raise ArchivoInvalidoError(
                f"Posición {posicion} fuera de rango "
                f"(el archivo tiene {(tamanio - HEADER_SIZE) // REGISTRO_SIZE} registros)."
            )
        f.seek(offset)
        f.write(registro)


def alta_binario(ruta, cancion):
    with open(ruta, "r+b") as f:
        f.seek(5)
        cantidad = struct.unpack("<I", f.read(4))[0]

        f.seek(0, 2)
        registro = struct.pack(REGISTRO_FMT, *_cancion_a_tupla(cancion))
        f.write(registro)

        f.seek(5)
        f.write(struct.pack("<I", cantidad + 1))


def baja_binario(ruta, posicion):
    with open(ruta, "r+b") as f:
        f.seek(5)
        cantidad = struct.unpack("<I", f.read(4))[0]

        if posicion < 0 or posicion >= cantidad:
            raise ArchivoInvalidoError(
                f"Posición {posicion} fuera de rango (hay {cantidad} registros)."
            )

        for i in range(posicion + 1, cantidad):
            offset_origen = HEADER_SIZE + i * REGISTRO_SIZE
            offset_destino = HEADER_SIZE + (i - 1) * REGISTRO_SIZE
            f.seek(offset_origen)
            datos = f.read(REGISTRO_SIZE)
            f.seek(offset_destino)
            f.write(datos)

        f.seek(5)
        f.write(struct.pack("<I", cantidad - 1))

    nuevo_tamanio = HEADER_SIZE + (cantidad - 1) * REGISTRO_SIZE
    with open(ruta, "r+b") as f:
        f.truncate(nuevo_tamanio)

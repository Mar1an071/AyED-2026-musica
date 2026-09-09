# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Musica
- Por qué lo eligieron (5–8 líneas): Nuestro grupo eligió el tema de canciones debido a que estas mismas en general son parte de nuestra vida cotidiana, en cualquier ámbito y momento uno escucha música ya sea acompañado o individualmente. Por otro lado, nos permite aplicar conceptos de programacion de forma practica y motivadora, uniendo nuestro interes personal con plataformas que utilizan estos datos, como por ejemplo: Spotify y YouTube Music

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

1 - Ítem del catálogo: es la clase Cancion dentro de la carpeta src/dominio/canciones.py 
1.1 - Mutable o inmutable: 
    - ID: inmutable por convencion, ya que si cambio el id de alguna cancion se romperia la busqueda de la funcion buscar_id() que esta dentro de Biblioteca.
    - titulo, album, genero, anio, artista, duracion_seg: son mutables porque son atributos públicos reasignables.

1.2 - La Biblioteca concentra todo. La coleccion principal trabaja con un subconjunto de canciones tomadas del catálogo. La pila registra el historial con criterio último en entrar primero en salir. La cola ordena los pendientes con criterio primero en entrar primero en salir.
    

```text
  Biblioteca (catálogo: todas las canciones)
                         |
                         v
        Colección principal (canciones activas)
                         |
                +--------+--------+
                v                 v
        Pila (historial)   Cola (pendientes)
```

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |

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

La operación recursiva agrupa y muestra versiones de una misma canción (original, live, acoustic, remix, unplugged) a partir de un ID ingresado por el usuario.

- Función: cadena_versiones(biblioteca, id_origen): tiene como objetivo devolver una lista con todas las canciones que comparten el mismo titulo base que la cancion de origen. Utiliza como ayuda _base_titulo(titulo) que normaliza el titulo con .split() para eliminar sufijos entre parentesis.

ayuda del recursivo: _recolectar_versiones(canciones, base_titulo, indice, resultado): recorre recursivamente la lista de objetos Cancion() y agrega a la lista 'resultado' todas las que coincidan con 'base_titulo', avanzando solo hacia adelante.

- Caso base: if indice >= len(canciones):
    return resultado

Ocurre cuando el indice es igual o mayor a los elementos de la lista de canciones (67 elementos). Al cumplirse la condicion significa que ya reviso toda la lista, por lo que la funcion detiene la recursividad y devuelve la lista resultado (con todas las versiones encontradas).

- Caso recursivo: 
cancion = canciones[indice]
if _base_titulo(cancion.titulo) == base_titulo:
    resultado.append(cancion)
return _recolectar_versiones(canciones, base_titulo, indice + 1, resultado)

Ocurre mientras el índice es menor a la cantidad de canciones (67). mientras se cumpla esta condicion se extrae el objeto Cancion() en la posición actual (canciones[indice]), se normaliza su titulo con _base_titulo y se compara con indice + 1 hasta alcanzar el caso base. 



- Impresión recursiva: mostrar_cadena_recursivo(canciones) es la funcion que muestra el resultado. usa como ayuda a _mostrar_recursivo(canciones, indice). caso base: if indice >= len(canciones):return. Caso recursivo: print(canciones[indice]) y luego se llama a sí misma con _mostrar_recursivo(canciones, indice+1). se usa en el main.py despues de obtener la cadena.


- Traza de un ejemplo real del dataset: 

Ejemplo 1 - canción con versiones: id_origen =  1 ("De musica ligera"). cadena_versiones obtiene base = "De Musica Ligera" y llama _recolectar_versiones(..., 0, []). Recorre todos los indices (de 0 a 66); en indice 0 coincide y lo agrega a la lista resultado; en indice 61 coincide con "De Musica Ligera (Unplugged), _base_titulo devuelve "De Musica Ligera" y tambien agrega a la lista resultado. Caso base en indice 67 devuelve la lista resultado con las dos canciones y mostrar_cadena_recursivo imprime las dos canciones.

Ejemplo 2 - cancion sin versiones: id_origen = 60 ("Que Ves"). Recorrido completo solo encuentra coincidencia en su propia posicion. Se devuelve una lista de un solo elemento.

Ejemplo 3 - Id inexistente: id_origen = 1000. biblioteca.buscar_id(1000) lanza ItemNoEncontradoError.


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

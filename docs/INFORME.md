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
| ListaEnlazada | esta_vacia, tamanio, insertar_al_inicio, insertar_al_final, eliminar, buscar, __iter__, __len__, __getitem__ | _cabeza apunta al primer nodo o None; _tamanio es la cantidad exacta; el último nodo tiene siguiente = None; sin list de Python por abajo |
| Pila | apilar, desapilar, ver_tope, esta_vacia, tamanio, __iter__ | LIFO (último en entrar, primero en salir): el tope es siempre _items._cabeza |
| Cola | encolar, desencolar, ver_frente, esta_vacia | FIFO (primero en entrar, primero en salir): frente _cabeza, final el nodo con siguiente = None |

Dónde se usa cada uno en el dominio.

ListaEnlazada esta como base de Biblioteca._canciones y Playlist._canciones; Pila dentro de Historial._pila; Cola en ColaReproduccion._cola (incluímos que el historial se llena desde la cola).
Encapsulamiento — aclara que _cabeza sí se lee, pero solo dentro de Pila y Cola, que son las clases dueñas de su lista.
Excepciones propias — tabla de qué se lanza cuando y en qué opción se captura.


## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| **listar catalogo** | $0(n)$ | $0(1)$ | Recorre consecutivamente los $n$ elementos del catálogo una sola vez [3].|
|**busqueda lineal** | peor: $0(n)$ / mejor: $0(1)$ |$0(1)$ | Inspecciona cada elemento secuencialmente hasta encontrar la coincidencia o alcanzar el final [3, 4].| 
| **busqueda binaria ** | $0(\log n)$ | $0(1)$ | Requiere coleccion ordenada; en cada paso divide el rango de búsqueda a la mitad [3, 5, 6]. |
| **ordenamiento selleccion** | $0(n^2)$ siempre | $0(1)$ |dos bucles anidados que efectuan aproximadamente $\frac{n^2}{2}$ comparaciones, independientemente del orden previo [3, 7, 8]. |
|**Ordenamiento Inserción** | Mejor: $O(n)$ / Peor: $O(n^2)$ | $O(1)$ | Si ya está ordenado realiza 1 comparación por elemento; si está invertido desplaza todo a la derecha [3, 8, 9]. |

En esta sección se analiza la complejidad teórica (notación Big-O) de las operaciones principales del sistema de gestión de la biblioteca musical y se contrasta con las mediciones de tiempo de ejecución reales [1, 3].

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
| Operación | Dataset Original ($n = \dots$) | Dataset Agrandado ($10n = \dots$) | Comportamiento Observado |
| :--- | :--- | :--- | :--- |
| **Búsqueda lineal** | `0.0000XX s` | `0.0000YY s` | Crecimiento proporcional al tamaño ($\approx 10\times$) [11]. |
| **Búsqueda binaria** | `0.0000AA s` | `0.0000BB s` | Incremento mínimo e imperceptible ($O(\log n)$) [6, 11]. |
| **Ordenamiento Selección** | `0.0000CC s` | `0.0000DD s` | Crecimiento cuadrático ($\approx 100\times$ más tiempo) [8, 11]. |
| **Ordenamiento Inserción** | `0.0000EE s` | `0.0000FF s` | Crecimiento cuadrático ($\approx 100\times$ más tiempo en el peor caso) [9, 11]. |

Resultados obtenidos mediante el script de mediciones (`src/algoritmos/mediciones.py`) comparando el catálogo original ($n$) frente al dataset ampliado ($10n$) [1, 2, 10, 11]:

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |

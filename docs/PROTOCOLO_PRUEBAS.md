# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback | pasa ✅  | Se importaron las clases bibliotecas y cancion de /dominio y la funcion cargar_csv de /persistencia al main. En el main se crearon funciones las cuales cargan el csv y listan las canciones |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue | pasa ✅ | Se creo la funcion ver_detalle() la cual busca el id ingresado por el usuario y si lo encuentra imprime el detalle de la cancion |
| P03 | E2 | En el menú elegir 5 (Operación recursiva) e ingresar 1 | id = 1 (De Musica Ligera - Rock, tiene 62 Unplugged) | Imprime la cadena con versiones de 'De Musica Ligera' (2 canciones), sin traceback, vuelve al menú. | pasa ✅ |   |
| P04 | E2 | En el menú elegir 5 e ingresar 60 | id = 60 'Que Ves' (sin versiones) | Versiones de 'Que Ves' (1 canción) es el caso base unitario, sin traceback, vuelve al menú | pasa ✅ |  |
| P05 | E1 | Ver detalle de un ítem que existe | id = 32 | Muestra 32 - Bohemian Rhapsody - Queen ... sin traceback, vuelve al menú | pasa ✅ | |
| P06 | E1 | Ver detalle con id no numérico | id = abc | Mensaje id invalido, no se cae, vuelve al menú | pasa ✅ | |
| P07 | E2 | Elegir opción de menú inválida | input = 99 | Mensaje: Opción inválida, vuelve a mostrar el menú | pasa ✅ | |
| P08 | E2 | Dejar el input vacío y dar enter | input = `` (vacío) | No explota, trata como opción inválida y vuelve a preguntar | pasa ✅ | |
| P09 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia |  |  |
| P10 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue |  |  |
| P11 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue |  |  |
| P12 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones |  |  |
| P13 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P14 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P15 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P16 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P17 | E5 | Guardar CSV, salir, volver a entrar |  | los datos siguen |  |  |
| P18 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P19 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |

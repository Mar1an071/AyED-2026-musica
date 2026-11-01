# src/algoritmos/mediciones.py

import time
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
from src.dominio.biblioteca import Biblioteca
from src.persistencia.texto import cargar_csv


def medir_tiempo(funcion, *args, **kwargs):
    """Mide con perf_counter el tiempo exacto que tarda en ejecutarse una función."""
    inicio = time.perf_counter()
    resultado = funcion(*args, **kwargs)
    fin = time.perf_counter()
    return fin - inicio, resultado


def ejecutar_benchmarking(catalogo):
    """
    Ejecuta las mediciones empíricas requeridas para la Entrega 4
    y muestra los resultados formateados para docs/INFORME.md §5.
    """
    datos_n = list(catalogo)
    datos_10n = datos_n * 10

    criterio = lambda item: item.titulo.lower()
    # Clave no existente para medir peor caso (recorrido completo de la colección)
    clave_busqueda = "cancion inexistente"

    # Preparar colecciones ordenadas para la búsqueda binaria
    datos_n_ord = ordenar_insercion(datos_n, obtener_clave=criterio)
    datos_10n_ord = ordenar_insercion(datos_10n, obtener_clave=criterio)

    # Para mediciones de microsegundos usamos un promedio de repeticiones para estabilidad
    repeticiones = 100

    # 1. Búsqueda Lineal
    t_acum = 0.0
    for _ in range(repeticiones):
        t, _ = medir_tiempo(busqueda_lineal, datos_n, clave_busqueda, obtener_clave=criterio)
        t_acum += t
    t_lin_n = t_acum / repeticiones

    t_acum = 0.0
    for _ in range(repeticiones):
        t, _ = medir_tiempo(busqueda_lineal, datos_10n, clave_busqueda, obtener_clave=criterio)
        t_acum += t
    t_lin_10n = t_acum / repeticiones

    # 2. Búsqueda Binaria
    t_acum = 0.0
    for _ in range(repeticiones):
        t, _ = medir_tiempo(busqueda_binaria, datos_n_ord, clave_busqueda, obtener_clave=criterio)
        t_acum += t
    t_bin_n = t_acum / repeticiones

    t_acum = 0.0
    for _ in range(repeticiones):
        t, _ = medir_tiempo(busqueda_binaria, datos_10n_ord, clave_busqueda, obtener_clave=criterio)
        t_acum += t
    t_bin_10n = t_acum / repeticiones

    # 3. Ordenamiento Selección
    t_sel_n, _ = medir_tiempo(ordenar_seleccion, datos_n, obtener_clave=criterio)
    t_sel_10n, _ = medir_tiempo(ordenar_seleccion, datos_10n, obtener_clave=criterio)

    # 4. Ordenamiento Inserción
    t_ins_n, _ = medir_tiempo(ordenar_insercion, datos_n, obtener_clave=criterio)
    t_ins_10n, _ = medir_tiempo(ordenar_insercion, datos_10n, obtener_clave=criterio)

    print("=" * 70)
    print("       MEDICIÓN DE COMPLEJIDAD (time.perf_counter) — ENTREGA 4")
    print("=" * 70)
    print(f"Catálogo Original (n) : {len(datos_n)} canciones")
    print(f"Catálogo Agrandado (10n): {len(datos_10n)} canciones")
    print("-" * 70)
    print(f"Búsqueda lineal (n={len(datos_n)})     : {t_lin_n:.8f} s | (10n={len(datos_10n)}): {t_lin_10n:.8f} s  (Ratio: {t_lin_10n/t_lin_n:.1f}x)")
    print(f"Búsqueda binaria (n={len(datos_n)})    : {t_bin_n:.8f} s | (10n={len(datos_10n)}): {t_bin_10n:.8f} s  (Ratio: {t_bin_10n/t_bin_n:.1f}x)")
    print(f"Ordenamiento Selección (n) : {t_sel_n:.8f} s | (10n): {t_sel_10n:.8f} s  (Ratio: {t_sel_10n/t_sel_n:.1f}x)")
    print(f"Ordenamiento Inserción (n) : {t_ins_n:.8f} s | (10n): {t_ins_10n:.8f} s  (Ratio: {t_ins_10n/t_ins_n:.1f}x)")
    print("=" * 70)

    return {
        "n": len(datos_n),
        "10n": len(datos_10n),
        "t_lin_n": t_lin_n,
        "t_lin_10n": t_lin_10n,
        "t_bin_n": t_bin_n,
        "t_bin_10n": t_bin_10n,
        "t_sel_n": t_sel_n,
        "t_sel_10n": t_sel_10n,
        "t_ins_n": t_ins_n,
        "t_ins_10n": t_ins_10n,
    }


if __name__ == "__main__":
    biblioteca = Biblioteca()
    cargar_csv("data/canciones.csv", biblioteca)
    ejecutar_benchmarking(biblioteca.listar_canciones())

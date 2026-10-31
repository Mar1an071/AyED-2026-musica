# src/algoritmos/mediciones.py

import time
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion


def medir_tiempo(funcion, *args, **kwargs):
    """Mide con perf_counter el tiempo exacto que tarda en ejecutarse una función."""
    inicio = time.perf_counter()
    resultado = funcion(*args, **kwargs)
    fin = time.perf_counter()
    return fin - inicio, resultado

def ejecutar_benchmarking(catalogo):
    """
    Ejecuta las mediciones empíricas requeridas para la Persona 3
    y las imprime en el formato exacto para docs/INFORME.md §5.
    """
    datos_n = list(catalogo)
    datos_10n = datos_n * 10  
    
    
    criterio = lambda item: item.nombre if hasattr(item, 'nombre') else item.titulo
   
    clave_busqueda = criterio(datos_n[len(datos_n) // 2]) if datos_n else "Cancion"

    print("=" * 65)
    print("          BENCHMARKING DE COMPLEJIDAD (Persona 3)")
    print("=" * 65)
    print(f"Tamaño n: {len(datos_n)} elementos | Tamaño 10n: {len(datos_10n)} elementos\n")

    t_lin_n, _ = medir_tiempo(busqueda_lineal, datos_n, clave_busqueda, obtener_clave=criterio)
    t_lin_10n, _ = medir_tiempo(busqueda_lineal, datos_10n, clave_busqueda, obtener_clave=criterio)

    datos_n_ord = ordenar_insercion(datos_n, obtener_clave=criterio)
    datos_10n_ord = ordenar_insercion(datos_10n, obtener_clave=criterio)

    t_bin_n, _ = medir_tiempo(busqueda_binaria, datos_n_ord, clave_busqueda, obtener_clave=criterio)
    t_bin_10n, _ = medir_tiempo(busqueda_binaria, datos_10n_ord, clave_busqueda, obtener_clave=criterio)

    t_sel_n, _ = medir_tiempo(ordenar_seleccion, datos_n, obtener_clave=criterio)
    t_sel_10n, _ = medir_tiempo(ordenar_seleccion, datos_10n, obtener_clave=criterio)

    t_ins_n, _ = medir_tiempo(ordenar_insercion, datos_n, obtener_clave=criterio)
    t_ins_10n, _ = medir_tiempo(ordenar_insercion, datos_10n, obtener_clave=criterio)

    print("--- TIEMPOS OBTENIDOS (en segundos) ---")
    print(f"Búsqueda lineal (n={len(datos_n)})     : {t_lin_n:.8f} s | (10n={len(datos_10n)}): {t_lin_10n:.8f} s")
    print(f"Búsqueda binaria (n={len(datos_n)})    : {t_bin_n:.8f} s | (10n={len(datos_10n)}): {t_bin_10n:.8f} s")
    print(f"Ordenamiento Selección (n) : {t_sel_n:.8f} s | (10n): {t_sel_10n:.8f} s")
    print(f"Ordenamiento Inserción (n) : {t_ins_n:.8f} s | (10n): {t_ins_10n:.8f} s")
    print("=" * 65)

if __name__ == "__main__":
  
    pass

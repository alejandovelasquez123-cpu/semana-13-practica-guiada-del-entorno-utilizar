"""
01_explorar_datos.py

Objetivo del archivo:
Explorar todos los archivos CSV del laboratorio antes de hacer cálculos más avanzados.

Qué aprenderás con este script:
- Cómo cargar archivos CSV con pandas.
- Cómo identificar filas, columnas y datos faltantes.
- Cómo interpretar una salida básica de datos en terminal.
- Por qué revisar la estructura del archivo antes de analizarlo.
"""

# BLOQUE 1: importaciones.
# Path ayuda a construir rutas de archivo independientes del sistema operativo.
# pandas permite leer CSV y convertirlos en DataFrames, que son tablas de datos en Python.
from pathlib import Path
import pandas as pd

# BLOQUE 2: rutas principales.
# BASE_DIR representa la carpeta principal del laboratorio.
# DATA_DIR representa la carpeta donde están los archivos CSV.
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

# BLOQUE 3: diccionario de archivos.
# Un diccionario permite asociar un nombre legible con la ruta real de cada archivo.
# La clave se muestra al estudiante; el valor es la ruta que Python usa para abrir el CSV.
archivos = {
    "Producción de leche": DATA_DIR / "produccion_leche.csv",
    "Cosecha de maíz": DATA_DIR / "cosecha_maiz.csv",
    "Inventario de animales": DATA_DIR / "inventario_animales.csv",
    "Ventas de productos": DATA_DIR / "ventas_productos.csv",
    "Clima de la vereda": DATA_DIR / "clima_vereda.csv",
}

print("=== Exploración general de archivos CSV ===")
print("Esta fase permite conocer la estructura de los datos antes de analizarlos.\n")

# BLOQUE 4: recorrido de todos los archivos.
# for permite repetir la misma exploración para cada CSV sin copiar y pegar código.
for nombre, ruta in archivos.items():
    print("\n" + "=" * 80)
    print(nombre.upper())
    print(f"Archivo: {ruta.name}")

    # BLOQUE 5: carga del CSV.
    # pd.read_csv lee el archivo y lo convierte en un DataFrame llamado df.
    # df es una tabla con filas y columnas.
    df = pd.read_csv(ruta)

    # BLOQUE 6: forma del DataFrame.
    # df.shape devuelve una tupla: (cantidad_de_filas, cantidad_de_columnas).
    filas, columnas = df.shape
    print(f"Filas: {filas:,}")
    print(f"Columnas: {columnas}")

    # BLOQUE 7: nombres de columnas.
    # list(df.columns) permite ver qué variables trae el archivo.
    # Este paso es clave para evitar errores como KeyError por escribir mal una columna.
    print("Columnas disponibles:")
    for columna in df.columns:
        print(f"- {columna}")

    # BLOQUE 8: datos faltantes.
    # isna() identifica valores vacíos.
    # sum() cuenta cuántos vacíos hay en cada columna.
    faltantes = df.isna().sum()
    faltantes = faltantes[faltantes > 0]
    if faltantes.empty:
        print("Datos faltantes: no se detectaron columnas con valores vacíos.")
    else:
        print("Datos faltantes por columna:")
        print(faltantes)

    # BLOQUE 9: primeras filas.
    # head(3) muestra una muestra pequeña de la tabla para entender el contenido.
    print("\nPrimeras 3 filas:")
    print(df.head(3).to_string(index=False))

# BLOQUE 10: cierre.
print("\nExploración completada. Registra tus observaciones en la bitácora técnica.")

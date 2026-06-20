"""
00_verificar_entorno.py

Objetivo del archivo:
Verificar que el laboratorio esté listo para trabajar. Este script no analiza datos todavía;
su función es comprobar que el entorno de programación tenga Python, librerías y archivos CSV.

Por qué es importante:
Antes de iniciar un proyecto técnico se debe validar que el entorno funciona. Si se intenta analizar
datos sin revisar dependencias o rutas, los errores pueden aparecer más adelante y ser más difíciles
de diagnosticar.
"""

# BLOQUE 1: importaciones básicas.
# pathlib permite trabajar con rutas de carpetas y archivos de una forma más segura que escribir textos fijos.
# sys permite consultar información del intérprete de Python que está ejecutando el programa.
from pathlib import Path
import sys

# BLOQUE 2: definición de rutas del proyecto.
# __file__ representa la ubicación de este archivo Python.
# resolve() convierte esa ubicación en una ruta absoluta.
# parents[1] sube dos niveles: desde src/ hasta la carpeta principal del laboratorio.
# Esto permite que el programa funcione aunque el proyecto esté en escritorios o computadores diferentes.
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

# BLOQUE 3: presentación inicial en la terminal.
# Estos print ayudan a confirmar qué versión de Python se está usando y dónde está ubicado el proyecto.
print("=== Verificación del entorno ===")
print(f"Python: {sys.version.split()[0]}")
print(f"Carpeta base del laboratorio: {BASE_DIR}")

# BLOQUE 4: verificación de librerías externas.
# pandas se usa para leer y analizar CSV.
# matplotlib se usa para generar gráficos.
# try/except permite capturar un error si una librería no está instalada, sin detener todo el programa.
try:
    import pandas as pd
    print(f"pandas instalado: {pd.__version__}")
except ImportError:
    print("ERROR: pandas no está instalado. Ejecuta: pip install -r requirements.txt")

try:
    import matplotlib
    print(f"matplotlib instalado: {matplotlib.__version__}")
except ImportError:
    print("ERROR: matplotlib no está instalado. Ejecuta: pip install -r requirements.txt")

# BLOQUE 5: lista oficial de archivos CSV esperados.
# Si alguno falta, los scripts posteriores pueden fallar.
archivos = [
    "produccion_leche.csv",
    "cosecha_maiz.csv",
    "inventario_animales.csv",
    "ventas_productos.csv",
    "clima_vereda.csv",
]

# BLOQUE 6: revisión de existencia y tamaño de cada archivo.
# exists() confirma si el archivo está realmente en la carpeta data.
# stat().st_size obtiene el tamaño del archivo en bytes; luego lo convertimos a MB.
print("\n=== Archivos de datos ===")
archivos_encontrados = 0
for nombre in archivos:
    ruta = DATA_DIR / nombre
    if ruta.exists():
        archivos_encontrados += 1
        tamano_mb = ruta.stat().st_size / (1024 * 1024)
        print(f"OK: {nombre} ({tamano_mb:.2f} MB)")
    else:
        print(f"FALTA: {nombre}")

# BLOQUE 7: cierre con interpretación técnica.
print("\n=== Resultado de la verificación ===")
print(f"Archivos encontrados: {archivos_encontrados} de {len(archivos)}")
if archivos_encontrados == len(archivos):
    print("El laboratorio está listo para continuar con la exploración de datos.")
else:
    print("Hay archivos faltantes. Revisa la carpeta data antes de continuar.")

"""
05_script_con_errores.py

ATENCIÓN: este archivo contiene errores intencionales.

Objetivo del estudiante:
1. Ejecutar el archivo.
2. Leer el mensaje de error.
3. Identificar la línea del problema.
4. Corregir un error a la vez.
5. Ejecutar nuevamente.
6. Documentar cada corrección en la bitácora.

Importante:
No borres todo el código para reemplazarlo por otro. El objetivo es practicar depuración, no evitarla.
"""

# BLOQUE 1: importaciones correctas.
# Estos dos import no son el problema. Empieza revisando los mensajes que aparezcan después de ejecutar.
from pathlib import Path
import pandas as pd

# BLOQUE 2: rutas del proyecto.
# BASE_DIR ubica la carpeta principal del laboratorio.
# DATA_DIR ubica la carpeta de datos.
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"

# BLOQUE 3: carga de datos.
# Este archivo sí existe. Si aparece FileNotFoundError, revisa que estés ejecutando desde la carpeta correcta.
df = pd.read_csv(DATA_DIR / "produccion_leche.csv")

# BLOQUE 4: inspección recomendada.
# Pista: si tienes un error de columna, ejecuta temporalmente esta línea para ver los nombres reales:
# print(df.columns)

# BLOQUE 5: error intencional de columna.
# Esta columna no existe con ese nombre. Debes revisar las columnas reales del CSV.
# En el CSV la columna se llama exactamente "litros" (ver cabecera del archivo).
# Si en tu ejecución esto fallara, ejecuta temporalmente: print(df.columns)
df["litros"] = pd.to_numeric(df["litros"], errors="coerce")

total = df["litros"].sum()


print("Total de leche:", total)

# BLOQUE 6: error intencional de sintaxis.
# Falta cerrar algo en esta línea. Lee el mensaje SyntaxError y observa la marca ^ en la terminal.
print("Promedio de leche:", df["litros"].mean())


"""
02_analizar_produccion.py

Objetivo del archivo:
Analizar la producción de leche y generar evidencias técnicas en la carpeta reportes.

Este script muestra un flujo básico de análisis de datos:
1. Cargar datos.
2. Convertir tipos.
3. Detectar registros sospechosos.
4. Filtrar datos válidos.
5. Calcular indicadores.
6. Agrupar por finca.
7. Exportar reportes.
8. Generar un gráfico.
"""

# BLOQUE 1: importaciones.
# pandas se usa para manipular datos en tablas.
# matplotlib.pyplot permite crear gráficos.
# Path permite manejar rutas de archivos.
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# BLOQUE 2: rutas principales.
# REPORT_DIR se crea para guardar resultados sin mezclar datos originales con datos procesados.
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reportes"
REPORT_DIR.mkdir(exist_ok=True)

# BLOQUE 3: carga del archivo de producción de leche.
# El archivo original está en data/ y no debe modificarse.
ruta = DATA_DIR / "produccion_leche.csv"
df = pd.read_csv(ruta)

# BLOQUE 4: conversión de tipos.
# A veces un CSV trae números como texto. pd.to_numeric convierte esos valores a números reales.
# errors="coerce" significa: si un dato no se puede convertir, se reemplaza por NaN.
# pd.to_datetime convierte texto en fechas para futuros análisis temporales.
df["litros"] = pd.to_numeric(df["litros"], errors="coerce")
df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

print("=== Análisis de producción de leche ===")
print(f"Registros cargados: {len(df):,}")

# BLOQUE 5: detección de registros sospechosos.
# En este laboratorio consideramos sospechosos los registros vacíos, negativos o demasiado altos.
# Esta regla es una decisión técnica y debe justificarse en el informe.
sospechosos = df[df["litros"].isna() | (df["litros"] < 0) | (df["litros"] > 35)]
print(f"Registros sospechosos detectados: {len(sospechosos):,}")

# BLOQUE 6: filtrado de registros válidos.
# Para calcular totales y promedios confiables se usan solo registros entre 0 y 35 litros.
validos = df[df["litros"].notna() & (df["litros"] >= 0) & (df["litros"] <= 35)].copy()
print(f"Registros válidos usados para cálculos: {len(validos):,}")

# BLOQUE 7: indicadores generales.
# sum() calcula total.
# mean() calcula promedio.
# round() redondea para que el resultado sea más legible.
total_litros = validos["litros"].sum()
promedio_litros = validos["litros"].mean()

print(f"Total de litros válidos: {total_litros:,.2f}")
print(f"Promedio por registro válido: {promedio_litros:.2f}")

# BLOQUE 8: agrupación por finca.
# groupby permite resumir datos por categoría.
# agg calcula varias medidas al mismo tiempo: cantidad, suma y promedio.
# sort_values ordena de mayor a menor producción total.
produccion_por_finca = (
    validos.groupby("finca")["litros"]
    .agg(["count", "sum", "mean"])
    .sort_values("sum", ascending=False)
)

print("\nProducción por finca:")
print(produccion_por_finca)

# BLOQUE 9: exportación de reportes CSV.
# Estos archivos son evidencias técnicas que luego se pueden abrir en Excel, LibreOffice o VS Code.
produccion_por_finca.to_csv(REPORT_DIR / "resumen_produccion_por_finca.csv", encoding="utf-8")
sospechosos.to_csv(REPORT_DIR / "registros_sospechosos_leche.csv", index=False, encoding="utf-8")

# BLOQUE 10: generación de gráfico.
# El gráfico permite comunicar el resultado de forma visual.
# tight_layout ajusta márgenes para que etiquetas y títulos no queden cortados.
plt.figure(figsize=(10, 5))
produccion_por_finca["sum"].plot(kind="bar")
plt.title("Producción total de leche por finca")
plt.xlabel("Finca")
plt.ylabel("Litros")
plt.tight_layout()
plt.savefig(REPORT_DIR / "grafico_produccion_por_finca.png")
plt.close()

# BLOQUE 11: cierre y verificación de salidas.
print("\nReportes generados en la carpeta reportes:")
print("- resumen_produccion_por_finca.csv")
print("- registros_sospechosos_leche.csv")
print("- grafico_produccion_por_finca.png")
print("\nAbre la carpeta reportes y toma captura de los archivos generados.")

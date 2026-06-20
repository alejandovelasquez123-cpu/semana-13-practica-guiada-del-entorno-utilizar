"""
06_reto_estudiante.py

Reto avanzado del estudiante.

Este archivo está incompleto a propósito. Debes completar las secciones marcadas con TODO.
El reto consiste en analizar ventas y cosecha de maíz usando como referencia los scripts anteriores.

Resultado esperado:
- reportes/reto_ventas_por_producto.csv
- reportes/reto_maiz_por_finca.csv
"""

# BLOQUE 1: importaciones.
from pathlib import Path
import pandas as pd

# BLOQUE 2: rutas del proyecto.
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reportes"
REPORT_DIR.mkdir(exist_ok=True)

# BLOQUE 3: carga de datos.
# ventas contiene información económica.
# maiz contiene información agrícola por finca y lote.
ventas = pd.read_csv(DATA_DIR / "ventas_productos.csv")
maiz = pd.read_csv(DATA_DIR / "cosecha_maiz.csv")

print("=== Reto del estudiante: ventas y cosecha de maíz ===")
print("Completa los TODO del archivo y ejecuta nuevamente.\n")

# TODO 1: convierte precio_unitario_cop y cantidad a valores numéricos.
# Pista: usa pd.to_numeric(ventas["nombre_columna"], errors="coerce")
ventas["precio_unitario_cop"] = pd.to_numeric(ventas["precio_unitario_cop"], errors="coerce")
ventas["cantidad"] = pd.to_numeric(ventas["cantidad"], errors="coerce")

# TODO 2: crea una columna llamada valor_total_cop.
# Pista: multiplica cantidad por precio_unitario_cop.
ventas["valor_total_cop"] = ventas["cantidad"] * ventas["precio_unitario_cop"]

# TODO 3: calcula el valor total vendido por producto usando groupby.
# Pista: ventas.groupby("producto")["valor_total_cop"].sum()
ventas_por_producto = (
    ventas.dropna(subset=["producto", "valor_total_cop"])
    .groupby("producto")["valor_total_cop"]
    .sum()
    .sort_values(ascending=False)
)

# TODO 4: guarda el resultado en reportes/reto_ventas_por_producto.csv.
# Pista: usa to_csv(REPORT_DIR / "nombre_archivo.csv", encoding="utf-8")
ventas_por_producto.to_csv(
    REPORT_DIR / "reto_ventas_por_producto.csv",
    encoding="utf-8",
    header=["valor_total_cop"],
)

# TODO 5: convierte kilos_cosechados a valor numérico y calcula el total de kilos por finca.
# Pista: maiz.groupby("finca")["kilos_cosechados"].sum()
maiz["kilos_cosechados"] = pd.to_numeric(maiz["kilos_cosechados"], errors="coerce")
maiz_por_finca = (
    maiz.dropna(subset=["finca", "kilos_cosechados"])
    .groupby("finca")["kilos_cosechados"]
    .sum()
    .sort_values(ascending=False)
)

# TODO 6: guarda el resultado en reportes/reto_maiz_por_finca.csv.
maiz_por_finca.to_csv(
    REPORT_DIR / "reto_maiz_por_finca.csv",
    encoding="utf-8",
    header=["kilos_cosechados"],
)


print("Reto completado.")
print("Se generaron:")
print("- reportes/reto_ventas_por_producto.csv")
print("- reportes/reto_maiz_por_finca.csv")


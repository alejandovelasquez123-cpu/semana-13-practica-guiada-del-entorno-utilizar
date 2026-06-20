"""
03_generar_reporte.py

Objetivo del archivo:
Generar un reporte técnico consolidado a partir de varios archivos CSV.

Este script representa una automatización: en vez de calcular manualmente en hojas de cálculo,
el programa lee datos, calcula indicadores y escribe un archivo de reporte automáticamente.
"""

# BLOQUE 1: importaciones.
from pathlib import Path
import pandas as pd

# BLOQUE 2: rutas de trabajo.
# Se separan datos originales y reportes generados para mantener el proyecto organizado.
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reportes"
REPORT_DIR.mkdir(exist_ok=True)

# BLOQUE 3: carga de archivos CSV.
# Cada variable almacena un DataFrame distinto.
leche = pd.read_csv(DATA_DIR / "produccion_leche.csv")
maiz = pd.read_csv(DATA_DIR / "cosecha_maiz.csv")
ventas = pd.read_csv(DATA_DIR / "ventas_productos.csv")
clima = pd.read_csv(DATA_DIR / "clima_vereda.csv")

# BLOQUE 4: conversiones seguras a número.
# Este paso evita que los cálculos fallen si algún dato viene como texto o vacío.
leche["litros"] = pd.to_numeric(leche["litros"], errors="coerce")
maiz["kilos_cosechados"] = pd.to_numeric(maiz["kilos_cosechados"], errors="coerce")
ventas["precio_unitario_cop"] = pd.to_numeric(ventas["precio_unitario_cop"], errors="coerce")
ventas["cantidad"] = pd.to_numeric(ventas["cantidad"], errors="coerce")
clima["lluvia_mm"] = pd.to_numeric(clima["lluvia_mm"], errors="coerce")

# BLOQUE 5: creación de una nueva columna calculada.
# El valor total de una venta es cantidad por precio unitario.
ventas["valor_total_cop"] = ventas["cantidad"] * ventas["precio_unitario_cop"]

# BLOQUE 6: filtros de calidad.
# Se eliminan valores imposibles o poco confiables antes de calcular indicadores.
leche_valida = leche[leche["litros"].between(0, 35, inclusive="both")]
maiz_valido = maiz[maiz["kilos_cosechados"].between(0, 800, inclusive="both")]
ventas_validas = ventas[(ventas["precio_unitario_cop"] > 0) & (ventas["cantidad"] > 0)]

# BLOQUE 7: ventas por producto.
# groupby agrupa por producto y sum suma el valor total vendido por cada uno.
ventas_por_producto = ventas_validas.groupby("producto")["valor_total_cop"].sum().sort_values(ascending=False)
ventas_por_producto.to_csv(REPORT_DIR / "ventas_por_producto.csv", encoding="utf-8")

# BLOQUE 8: construcción del reporte como lista de líneas.
# Usar una lista facilita agregar secciones y luego unirlas en un solo texto.
reporte = []
reporte.append("REPORTE TÉCNICO SEMANA 13")
reporte.append("Análisis de datos rurales y entorno de programación")
reporte.append("=" * 60)
reporte.append("")

# BLOQUE 9: resumen de archivos.
reporte.append("1. RESUMEN DE ARCHIVOS")
reporte.append(f"Registros de leche: {len(leche):,}")
reporte.append(f"Registros de maíz: {len(maiz):,}")
reporte.append(f"Registros de ventas: {len(ventas):,}")
reporte.append(f"Registros de clima: {len(clima):,}")
reporte.append("")

# BLOQUE 10: indicadores principales.
reporte.append("2. INDICADORES PRINCIPALES")
reporte.append(f"Total válido de leche: {leche_valida['litros'].sum():,.2f} litros")
reporte.append(f"Promedio de leche por registro válido: {leche_valida['litros'].mean():.2f} litros")
reporte.append(f"Total válido de maíz: {maiz_valido['kilos_cosechados'].sum():,.2f} kg")
reporte.append(f"Promedio de lluvia registrada: {clima['lluvia_mm'].mean():.2f} mm")
reporte.append(f"Valor total de ventas válidas: ${ventas_validas['valor_total_cop'].sum():,.0f} COP")
reporte.append("")

# BLOQUE 11: productos con mayor valor en ventas.
reporte.append("3. PRODUCTOS CON MAYOR VALOR EN VENTAS")
for producto, valor in ventas_por_producto.items():
    reporte.append(f"- {producto}: ${valor:,.0f} COP")
reporte.append("")

# BLOQUE 12: observación técnica para conectar con la comparación de entornos.
reporte.append("4. OBSERVACIÓN TÉCNICA")
reporte.append("El entorno de programación permitió leer datos, convertir tipos, detectar inconsistencias y generar archivos de salida.")
reporte.append("El estudiante debe complementar esta observación con su propia evaluación de funcionalidad, compatibilidad y costo.")

# BLOQUE 13: escritura del archivo final.
# write_text crea o reemplaza el archivo TXT con el contenido del reporte.
ruta_reporte = REPORT_DIR / "reporte_tecnico_semana13.txt"
ruta_reporte.write_text("\n".join(reporte), encoding="utf-8")

# BLOQUE 14: salida final en terminal.
print("Reporte generado correctamente:")
print(ruta_reporte)
print("\nTambién se generó: reportes/ventas_por_producto.csv")
print("Abre el reporte, revisa sus secciones y toma captura para tu informe.")

"""
04_comparar_entorno.py

Objetivo del archivo:
Registrar una evaluación técnica básica del entorno de programación usado durante el laboratorio.

Este script convierte la comparación técnica en una evidencia escrita. El archivo generado puede
copiarse al informe final o usarse como apoyo para completar la matriz de comparación.
"""

# BLOQUE 1: importaciones.
# platform permite consultar información básica del sistema operativo.
from pathlib import Path
import platform

# BLOQUE 2: rutas de trabajo.
BASE_DIR = Path(__file__).resolve().parents[1]
EVID_DIR = BASE_DIR / "evidencias"
EVID_DIR.mkdir(exist_ok=True)

# BLOQUE 3: instrucciones iniciales.
print("=== Comparación técnica del entorno ===")
print("Responde con información real de tu equipo y del entorno usado.")
print("Si no sabes un dato, escribe: no identificado")
print("\nEscala sugerida: 1 = muy bajo, 3 = aceptable, 5 = excelente.\n")

# BLOQUE 4: datos generales.
entorno = input("Nombre del entorno usado (ej: VS Code, PyCharm, Replit): ").strip()
sistema = input(f"Sistema operativo [{platform.system()} {platform.release()}]: ").strip()
if not sistema:
    sistema = f"{platform.system()} {platform.release()}"

# BLOQUE 5: criterios de evaluación.
# Cada tupla contiene el nombre del criterio y una pregunta guía.
criterios = [
    ("Funcionalidad", "¿Permite abrir carpetas, editar código, usar terminal, ejecutar scripts y revisar errores?"),
    ("Compatibilidad", "¿Funciona bien con tu equipo, Python, CSV y librerías instaladas?"),
    ("Costo", "¿Es gratuito o requiere pagos, internet constante o equipos potentes?"),
    ("Rendimiento", "¿Procesó los CSV grandes sin bloquearse?"),
    ("Facilidad de uso", "¿Fue fácil ubicar archivos, terminal, errores y resultados?"),
]

# BLOQUE 6: construcción del archivo de evidencia.
lineas = []
lineas.append("EVALUACIÓN TÉCNICA DEL ENTORNO")
lineas.append("=" * 50)
lineas.append(f"Entorno: {entorno}")
lineas.append(f"Sistema operativo: {sistema}")
lineas.append("")

# BLOQUE 7: captura de valoraciones.
# El while garantiza que el usuario escriba un número válido entre 1 y 5.
for nombre, pregunta in criterios:
    print(f"\n{nombre}: {pregunta}")
    while True:
        valor = input("Valoración de 1 a 5: ").strip()
        if valor in ["1", "2", "3", "4", "5"]:
            break
        print("Ingresa un número entre 1 y 5.")
    justificacion = input("Justificación técnica: ").strip()
    lineas.append(f"{nombre}: {valor}/5")
    lineas.append(f"Justificación: {justificacion}")
    lineas.append("")

# BLOQUE 8: recomendación final.
recomendacion = input("Recomendación final sobre el entorno: ").strip()
lineas.append("RECOMENDACIÓN FINAL")
lineas.append(recomendacion)

# BLOQUE 9: guardado de la evidencia.
ruta = EVID_DIR / "evaluacion_entorno.txt"
ruta.write_text("\n".join(lineas), encoding="utf-8")

print("\nEvaluación guardada en:")
print(ruta)
print("Puedes usar este archivo como base para tu conclusión final.")

# Bitácora técnica (resuelta)

> Copia y ajusta campos personales si lo necesitas.

## Datos del estudiante
- Nombre: [alejandro velasquez machado_everaldy ayala usuga_alejandra valencia villa]
- Grupo: [tu grupo]
- Fecha: [18/06/2026]
- Entorno utilizado: VS Code (Python)
- Sistema operativo: Windows 11
- Versión de Python: 3.14.3

---

## 1. Registro general de acciones

| Nº | Acción realizada | Comando usado | Resultado obtenido | Evidencia / captura | Observación técnica |
|---:|---|---|---|---|---|
| 1 | Abrí el proyecto en VS Code | No aplica | El proyecto cargó correctamente | Captura 1 | Identifiqué carpetas y paneles |
| 2 | Verifiqué Python | `python --version` | Python 3.14.3 | Captura 2 | confirma intérprete |
| 3 | Creé entorno virtual | `python -m venv .venv` | entorno creado | Captura 3 | aislamiento |
| 4 | Instalé dependencias | `pip install -r requirements.txt` | dependencias instaladas | Captura 4 | pandas/matplotlib |
| 5 | Ejecuté verificación | `python src/00_verificar_entorno.py` | OK: 5/5 CSV + libs | Captura 5 | evita errores de ruta |
| 6 | Exploré datos | `python src/01_explorar_datos.py` | mostró filas/columnas/faltantes | Captura 6 | detección de calidad |
| 7 | Analicé producción | `python src/02_analizar_produccion.py` | generó CSV y PNG | Captura 7 | identificó sospechosos (73) |
| 8 | Generé reporte | `python src/03_generar_reporte.py` | generó TXT + ventas_por_producto.csv | Captura 8 | reporte consolidado |
| 9 | Evalué el entorno | `python src/04_comparar_entorno.py` | requiere inputs | Captura 9 | depende de respuestas en consola |
| 10 | Depuré errores | `python src/05_script_con_errores.py` | corrección exitosa | Captura 10 | KeyError + SyntaxError |
| 11 | Completé el reto | `python src/06_reto_estudiante.py` | generó 2 CSV | Captura 11 | ventas por producto + maíz por finca |

---

## 2. Registro de errores y depuración

| Nº | Mensaje de error | Línea aproximada | Causa identificada | Solución aplicada | Resultado después de corregir |
|---:|---|---|---|---|---|
| 1 | KeyError: `litros_producidos` | ~línea 30 | columna no existe | usar `df["litros"]` | script ejecutó y calculó total |
| 2 | SyntaxError en `print(...` | última línea | falta `)` | agregar `)` | script terminó con promedio correcto |

---

## 3. Resultados principales encontrados
- Archivo con más registros: `produccion_leche.csv` (10,000)
- Finca con mayor producción de leche: `Los Guaduales` (mayor suma)
- Cantidad de registros sospechosos (leche): 73
- Producto con mayor valor de ventas: `maiz`
- Archivos generados en `reportes/`: `resumen_produccion_por_finca.csv`, `registros_sospechosos_leche.csv`, `grafico_produccion_por_finca.png`, `reporte_tecnico_semana13.txt`, `ventas_por_producto.csv`, `reto_ventas_por_producto.csv`, `reto_maiz_por_finca.csv`

---

## 4. Reflexión técnica final
1. Aprendí a ejecutar scripts en orden, validar dependencias y usar filtros de calidad antes de calcular.
2. El comando más importante fue `00_verificar_entorno.py` porque evita fallos por rutas o dependencias.
3. El error más difícil fue el KeyError porque exige confirmar nombres reales de columnas en el CSV.
4. Trabajar con CSV grandes permite aplicar agrupaciones, detectar faltantes/sospechosos y obtener indicadores reales.
5. Recomendaría VS Code + entorno virtual por su compatibilidad, organización y facilidad de depuración.


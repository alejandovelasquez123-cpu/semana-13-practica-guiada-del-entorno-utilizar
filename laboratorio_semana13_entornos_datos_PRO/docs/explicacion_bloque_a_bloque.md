# Explicación bloque a bloque del laboratorio

Este documento acompaña los archivos de la carpeta `src/`. Su función es explicar la lógica de cada script para que el estudiante no ejecute comandos de forma mecánica, sino que comprenda qué hace cada parte.

---

## 1. Bloques comunes en todos los scripts

### Docstring inicial

Es el texto encerrado entre triple comilla `"""`. Sirve para describir el objetivo general del archivo. No se ejecuta como instrucción principal, pero ayuda a documentar el código.

### Importaciones

Ejemplo:

```python
from pathlib import Path
import pandas as pd
```

Las importaciones cargan herramientas necesarias. `Path` permite trabajar con rutas y `pandas` permite manipular datos en tablas.

### Rutas del proyecto

Ejemplo:

```python
BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
REPORT_DIR = BASE_DIR / "reportes"
```

Este bloque evita escribir rutas fijas como `C:\Usuarios\...`. Así el proyecto puede funcionar en diferentes computadores.

### Carga de CSV

Ejemplo:

```python
df = pd.read_csv(DATA_DIR / "produccion_leche.csv")
```

Convierte un archivo CSV en un DataFrame. Un DataFrame es una tabla que Python puede filtrar, agrupar, ordenar y calcular.

### Conversión de tipos

Ejemplo:

```python
df["litros"] = pd.to_numeric(df["litros"], errors="coerce")
```

Convierte una columna a número. Si encuentra un dato inválido, lo cambia por `NaN`, que significa dato no disponible.

### Agrupación

Ejemplo:

```python
validos.groupby("finca")["litros"].sum()
```

Agrupa registros por finca y suma los litros. Es una operación clave para resumir miles de registros.

### Exportación

Ejemplo:

```python
resultado.to_csv(REPORT_DIR / "archivo.csv", encoding="utf-8")
```

Guarda una tabla procesada en un nuevo archivo. Esto permite conservar evidencias del análisis.

---

## 2. `00_verificar_entorno.py`

Este archivo comprueba si el laboratorio puede ejecutarse.

| Bloque | Qué hace | Qué evidencia produce |
|---|---|---|
| Importaciones | Usa `Path` y `sys`. | Permite consultar rutas y versión de Python. |
| Rutas | Ubica la carpeta principal y `data/`. | Muestra la ruta del laboratorio. |
| Librerías | Intenta importar pandas y matplotlib. | Confirma si las dependencias están instaladas. |
| Archivos | Revisa si existen los cinco CSV. | Muestra OK o FALTA por cada archivo. |
| Cierre | Resume la verificación. | Indica si se puede continuar. |

Pregunta clave: ¿qué problema evitarías al ejecutar este script antes de los demás?

---

## 3. `01_explorar_datos.py`

Este archivo permite conocer los datos antes de analizarlos.

| Bloque | Qué hace | Por qué importa |
|---|---|---|
| Diccionario de archivos | Relaciona nombres legibles con rutas reales. | Facilita recorrer varios CSV. |
| Lectura de CSV | Abre cada archivo con pandas. | Convierte datos en tablas. |
| Filas y columnas | Muestra el tamaño del archivo. | Ayuda a dimensionar la carga de datos. |
| Columnas | Lista los nombres disponibles. | Previene errores de nombres de columna. |
| Datos faltantes | Cuenta valores vacíos. | Ayuda a detectar problemas de calidad. |
| Muestra inicial | Enseña primeras filas. | Permite entender el contenido. |

Pregunta clave: ¿por qué no es recomendable calcular antes de explorar las columnas?

---

## 4. `02_analizar_produccion.py`

Este archivo realiza el análisis principal de leche.

| Bloque | Qué hace | Resultado |
|---|---|---|
| Carga | Lee `produccion_leche.csv`. | DataFrame con registros de leche. |
| Conversión | Convierte litros y fechas. | Datos listos para cálculo. |
| Sospechosos | Detecta valores vacíos, negativos o mayores a 35. | Tabla de registros problemáticos. |
| Válidos | Filtra datos confiables. | Base limpia para indicadores. |
| Indicadores | Calcula total y promedio. | Resultados en terminal. |
| Agrupación | Resume por finca. | Ranking de producción. |
| Reportes | Guarda CSV y gráfico. | Evidencia en carpeta `reportes`. |

Pregunta clave: ¿qué pasaría si se calculara el promedio usando registros negativos o exagerados?

---

## 5. `03_generar_reporte.py`

Este archivo automatiza la creación de un reporte técnico.

| Bloque | Qué hace | Resultado |
|---|---|---|
| Carga múltiple | Lee leche, maíz, ventas y clima. | Tablas disponibles. |
| Conversión | Prepara columnas numéricas. | Menos riesgo de error. |
| Columna calculada | Crea `valor_total_cop`. | Permite calcular ingresos. |
| Filtros | Conserva datos válidos. | Indicadores más confiables. |
| Reporte | Crea lista de líneas. | Estructura del informe. |
| Escritura | Guarda archivo TXT. | `reporte_tecnico_semana13.txt`. |

Pregunta clave: ¿por qué automatizar reportes puede ahorrar tiempo en una institución educativa o finca?

---

## 6. `04_comparar_entorno.py`

Este archivo convierte la reflexión técnica en evidencia escrita.

| Bloque | Qué hace | Resultado |
|---|---|---|
| Datos del entorno | Pregunta nombre del entorno y sistema operativo. | Contexto técnico. |
| Criterios | Evalúa funcionalidad, compatibilidad, costo, rendimiento y facilidad. | Valoraciones 1 a 5. |
| Justificación | Pide explicar cada valoración. | Argumentación técnica. |
| Archivo final | Guarda `evaluacion_entorno.txt`. | Evidencia para el informe. |

Pregunta clave: ¿por qué no basta con decir “me gustó VS Code” como justificación técnica?

---

## 7. `05_script_con_errores.py`

Este archivo enseña depuración. Contiene errores a propósito.

| Posible error | Qué debes hacer |
|---|---|
| Error de sintaxis | Revisar comillas, paréntesis y la línea marcada por la terminal. |
| Error de columna | Consultar `df.columns` para ver nombres reales. |
| Error de ejecución | Leer el último mensaje del traceback y corregir un problema a la vez. |

Regla importante: corrige un error, ejecuta, observa y documenta. No intentes cambiar todo el archivo al mismo tiempo.

---

## 8. `06_reto_estudiante.py`

Este archivo está incompleto. Debes aplicar lo aprendido.

| TODO | Qué debes lograr |
|---|---|
| TODO 1 | Convertir columnas económicas a número. |
| TODO 2 | Crear columna de valor total. |
| TODO 3 | Agrupar ventas por producto. |
| TODO 4 | Guardar CSV de ventas. |
| TODO 5 | Agrupar kilos de maíz por finca. |
| TODO 6 | Guardar CSV de maíz. |

Pregunta clave: ¿qué script anterior puedes usar como referencia para resolver este reto?

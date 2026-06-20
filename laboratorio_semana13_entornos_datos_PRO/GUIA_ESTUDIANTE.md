# Guía del estudiante
## Laboratorio avanzado Semana 13: entorno de programación, datos y comparación técnica

---

## 1. Propósito del laboratorio

En este laboratorio vas a usar un entorno de programación de manera técnica y documentada. No se trata solo de abrir VS Code y ejecutar código. La actividad busca que demuestres que puedes:

- abrir un proyecto organizado por carpetas;
- reconocer archivos, paneles, terminal, editor y salidas;
- ejecutar comandos desde la terminal integrada;
- instalar librerías necesarias;
- leer archivos CSV con miles de datos;
- analizar resultados y detectar inconsistencias;
- corregir errores controlados;
- registrar evidencias en una bitácora;
- comparar el entorno usado según funcionalidad, compatibilidad y costo.

Al finalizar, tendrás evidencias suficientes para argumentar si el entorno utilizado es adecuado para un proyecto rural basado en datos.

---

## 2. Competencias que vas a practicar

| Competencia | Cómo se evidencia |
|---|---|
| Navegación del entorno | Abres la carpeta completa, identificas paneles, menús, terminal y archivos. |
| Ejecución de comandos | Usas la terminal para verificar Python, instalar librerías y ejecutar scripts. |
| Interpretación de salidas | Lees resultados numéricos, errores y mensajes generados por los programas. |
| Manejo de datos | Cargas CSV grandes, revisas columnas, datos faltantes y registros sospechosos. |
| Depuración | Ejecutas un script con errores, interpretas el mensaje y corriges el problema. |
| Documentación técnica | Registras acciones, comandos, resultados y capturas en la bitácora. |
| Comparación de entornos | Evalúas funcionalidad, compatibilidad y costo con una matriz técnica. |

---

## 3. Datos del caso

El laboratorio incluye cinco archivos CSV simulados con fines educativos. Aunque los datos no pertenecen a una finca real, representan situaciones comunes de gestión rural.

| Archivo | Qué contiene | Para qué sirve |
|---|---|---|
| `produccion_leche.csv` | Registros de leche por fecha, finca, animal, turno y técnico. | Analizar producción, detectar datos sospechosos y generar reportes. |
| `cosecha_maiz.csv` | Registros de cosecha por finca, lote, kilos, humedad y estado del cultivo. | Comparar producción agrícola y analizar rendimiento por finca. |
| `inventario_animales.csv` | Código animal, raza, edad, peso, estado sanitario y vacuna. | Relacionar inventario ganadero con producción y control sanitario. |
| `ventas_productos.csv` | Producto, cantidad, unidad, precio, comprador y medio de pago. | Calcular ventas, ingresos y productos con mayor valor económico. |
| `clima_vereda.csv` | Fecha, zona, temperatura, lluvia, humedad y observación climática. | Relacionar clima con producción y condiciones rurales. |

---

## 4. Antes de empezar: cómo leer los bloques de código

Cada archivo Python está dividido en bloques. Un bloque es una parte del programa que cumple una función específica. Durante el laboratorio encontrarás bloques como estos:

| Bloque | Para qué sirve |
|---|---|
| Comentario inicial o docstring | Explica el propósito general del archivo. |
| Importaciones | Cargan herramientas externas, por ejemplo `pandas` para trabajar con datos. |
| Rutas del proyecto | Ubican carpetas como `data/`, `src/` y `reportes/` sin depender del computador. |
| Carga de datos | Lee archivos CSV y los convierte en tablas de trabajo llamadas DataFrames. |
| Limpieza o conversión | Convierte textos a números o fechas para evitar errores en los cálculos. |
| Análisis | Calcula totales, promedios, agrupaciones o registros sospechosos. |
| Salida en terminal | Muestra resultados para que puedas interpretarlos. |
| Reportes | Guarda resultados en archivos CSV, TXT o PNG. |

Cuando ejecutes un script, identifica qué bloque produjo cada resultado.

---

## 5. Fase 1: apertura del laboratorio

1. Descomprime el ZIP.
2. Abre VS Code.
3. Selecciona `Archivo > Abrir carpeta` o `File > Open Folder`.
4. Abre la carpeta `laboratorio_semana13_entornos_datos_PRO`.
5. Observa el explorador de archivos del lado izquierdo.
6. Ubica las carpetas `data`, `src`, `reportes`, `evidencias` y `docs`.
7. Toma una captura del proyecto abierto.

### Registro en bitácora

En la bitácora escribe:

- qué entorno abriste;
- qué carpetas encontraste;
- cuál carpeta contiene datos;
- cuál carpeta contiene scripts;
- cuál carpeta recibe reportes;
- qué paneles de VS Code identificaste.

---

## 6. Fase 2: preparación del entorno

Abre la terminal integrada de VS Code. Puedes hacerlo desde:

```text
Terminal > New Terminal
```

Luego ejecuta:

```bash
python --version
```

### Qué debes observar

El entorno debe mostrar una versión de Python. Por ejemplo:

```text
Python 3.12.0
```

Si aparece un error, significa que Python no está instalado o no está configurado en la variable PATH.

Crea un entorno virtual:

```bash
python -m venv .venv
```

### Qué significa este comando

| Parte del comando | Significado |
|---|---|
| `python` | Llama al intérprete de Python. |
| `-m venv` | Ejecuta el módulo que crea entornos virtuales. |
| `.venv` | Nombre de la carpeta donde quedará el entorno aislado. |

Activa el entorno virtual:

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Windows CMD:

```bash
.venv\Scripts\activate.bat
```

macOS o Linux:

```bash
source .venv/bin/activate
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

### Qué significa este comando

| Parte del comando | Significado |
|---|---|
| `pip` | Instalador de paquetes de Python. |
| `install` | Orden para instalar librerías. |
| `-r` | Indica que se leerá una lista de paquetes desde un archivo. |
| `requirements.txt` | Archivo que contiene las librerías necesarias. |

Toma capturas de la versión de Python y de la instalación de librerías.

---

## 7. Fase 3: verificación inicial

Ejecuta:

```bash
python src/00_verificar_entorno.py
```

Este script revisa tres cosas:

1. La versión de Python.
2. Si `pandas` y `matplotlib` están instalados.
3. Si los archivos CSV existen en la carpeta `data`.

### Preguntas para tu informe

- ¿Qué versión de Python aparece? **3.14.3**
- ¿Pandas está instalado correctamente? **Sí (3.0.3)**
- ¿Matplotlib está instalado correctamente? **Sí (3.10.8)**
- ¿Todos los archivos CSV fueron encontrados? **Sí (5 de 5)**
- ¿Qué error aparecería si faltara un archivo CSV? **FileNotFoundError**

---

## 8. Fase 4: exploración de datos

Ejecuta:

```bash
python src/01_explorar_datos.py
```

Este script abre cada archivo CSV y muestra información básica.

### Qué debes observar

| Elemento | Qué significa |
|---|---|
| Filas | Cantidad de registros del archivo. |
| Columnas | Variables disponibles en el archivo. |
| Datos faltantes | Valores vacíos que pueden afectar cálculos. |
| Primeras filas | Muestra inicial para entender la estructura del archivo. |

### Preguntas para tu informe

1. ¿Qué archivo tiene más registros? **produccion_leche.csv (10,000)**
2. ¿Qué columnas tiene `produccion_leche.csv`?
   **id_registro, fecha, finca, codigo_animal, turno, litros, temperatura_c, observacion, tecnico**
3. ¿Por qué es importante revisar datos faltantes antes de calcular? **Evita sesgos y evita fallos al convertir tipos o calcular**
4. ¿Qué ventaja tiene usar Python para explorar miles de registros? **Automatiza la exploración y permite detectar patrones y calidad de datos rápidamente**

---

## 9. Fase 5: análisis de producción

Ejecuta:

```bash
python src/02_analizar_produccion.py
```

Este script analiza la producción de leche. Además, genera archivos en la carpeta `reportes`.

### Qué hace el script por bloques

| Bloque | Función |
|---|---|
| Carga de datos | Abre `produccion_leche.csv`. |
| Conversión de tipos | Convierte litros a número y fecha a formato de fecha. |
| Detección de sospechosos | Busca registros vacíos, negativos o demasiado altos. |
| Filtrado de válidos | Conserva solo datos confiables para calcular. |
| Cálculo general | Obtiene total y promedio de litros. |
| Agrupación por finca | Resume producción por cada finca. |
| Generación de reportes | Guarda CSV y gráfico PNG en `reportes`. |

### Preguntas para tu informe

1. ¿Cuál fue la finca con mayor producción de leche?
2. ¿Cuántos registros sospechosos detectó el script?
3. ¿Por qué no se deben usar registros sospechosos en los cálculos finales?
4. ¿Qué archivo CSV se generó en la carpeta `reportes`?
5. ¿Qué representa el gráfico generado?

---

## 10. Fase 6: generación de reporte automático

Ejecuta:

```bash
python src/03_generar_reporte.py
```

Este script genera un reporte técnico consolidado con datos de leche, maíz, ventas y clima.

Verifica que exista el archivo:

```text
reportes/reporte_tecnico_semana13.txt
```

Ábrelo y revisa su contenido.

### Preguntas para tu informe

- ¿Qué indicadores principales aparecen en el reporte? **Leche (total y promedio), maíz (total), clima (promedio de lluvia) y valor total de ventas válidas (COP)**
- ¿Qué producto tuvo mayor valor en ventas? **maiz ($954,536,294 COP)**
- ¿Por qué es útil que un programa genere reportes automáticamente? **Estandariza, reduce errores y ahorra tiempo**
- ¿Cómo se relaciona esto con la automatización de tareas repetitivas? **Convierte carga/limpieza/cálculo/exportación en un flujo ejecutable con un solo comando**

---

## 11. Fase 7: comparación técnica del entorno

Ejecuta:

```bash
python src/04_comparar_entorno.py
```

El programa te pedirá datos sobre el entorno usado. Debes responder con información real.

También completa:

```text
docs/matriz_comparacion_entornos.md
```

### Criterios que debes analizar

| Criterio | Pregunta central |
|---|---|
| Funcionalidad | Sí: permitió abrir, editar, ejecutar, depurar y generar reportes (outputs en `reportes/` y depuración en `05_script_con_errores.py`). |
| Compatibilidad | Sí: funcionó en Windows 11 con Python 3.14.3 y librerías (pandas 3.0.3, matplotlib 3.10.8). |
| Costo | Sí: VS Code y librerías son gratuitas; no se requiere internet constante para ejecutar (solo para instalación). |
| Rendimiento | Sí: procesó CSV grandes (10,000 filas) sin bloqueos usando operaciones vectorizadas. |
| Facilidad de uso | Sí: terminal/tracebacks y estructura por carpetas (`data/`, `src/`, `reportes/`) facilitaron identificar errores y salidas. |

---

## 12. Fase 8: depuración de errores

Ejecuta:

```bash
python src/05_script_con_errores.py
```

Este archivo tiene errores intencionales. No es un fallo del laboratorio: es una parte de la actividad.

### Método de depuración recomendado

1. Ejecuta el archivo.
2. Lee el último mensaje de error.
3. Identifica el tipo de error.
4. Ubica la línea del problema.
5. Corrige solo ese error.
6. Ejecuta nuevamente.
7. Repite hasta que el programa funcione.
8. Documenta cada error en la bitácora.

### Tipos de error que puedes encontrar

| Tipo de error | Qué suele significar |
|---|---|
| `SyntaxError` | El código está mal escrito: falta paréntesis, comilla o dos puntos. |
| `KeyError` | Se intenta usar una columna que no existe en el CSV. |
| `FileNotFoundError` | La ruta del archivo es incorrecta o el archivo no existe. |
| `NameError` | Se usa una variable que no fue creada. |

Mínimo debes documentar dos errores corregidos.

---

## 13. Fase 9: reto del estudiante

Abre:

```text
src/06_reto_estudiante.py
```

Completa las secciones marcadas con `TODO`. El reto consiste en analizar ventas y cosecha de maíz.

### Resultado esperado

Cuando el reto esté completo, el script debe generar estos archivos:

```text
reportes/reto_ventas_por_producto.csv
reportes/reto_maiz_por_finca.csv
```

### Reglas del reto

- No borres los comentarios `TODO` hasta entender qué pide cada uno.
- Usa como referencia los scripts `02_analizar_produccion.py` y `03_generar_reporte.py`.
- Registra en tu bitácora qué partes completaste y qué dificultad encontraste.

---

## 14. Entregable final

Entrega un PDF en Moodle con:

1. Portada.
2. Captura del proyecto abierto en VS Code.
3. Captura de versión de Python.
4. Captura de instalación de dependencias.
5. Captura de ejecución de `00_verificar_entorno.py`.
6. Captura de ejecución de `01_explorar_datos.py`.
7. Captura de ejecución de `02_analizar_produccion.py`.
8. Captura del reporte generado por `03_generar_reporte.py`.
9. Evidencia del script con errores antes y después de corregir.
10. Bitácora técnica diligenciada.
11. Matriz de comparación técnica.
12. Conclusión final.

---

## 15. Conclusión esperada

Tu conclusión debe responder:

- ¿El entorno usado fue funcional para analizar datos grandes?
- ¿Fue compatible con el equipo y con Python?
- ¿El costo del entorno es adecuado para una institución educativa?
- ¿Qué problemas encontraste durante la ejecución?
- ¿Cómo los solucionaste?
- ¿Recomendarías este entorno para futuros proyectos rurales? ¿Por qué?

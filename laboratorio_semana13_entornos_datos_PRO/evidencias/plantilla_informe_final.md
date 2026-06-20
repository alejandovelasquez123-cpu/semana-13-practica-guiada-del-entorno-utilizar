# Plantilla de informe final
## Laboratorio avanzado Semana 13

## Portada

- Nombre del estudiante: [tu nombre]
- Grupo: [tu grupo]
- Fecha: [fecha]
- Entorno usado: VS Code
- Sistema operativo: Windows 11


---

## 1. Introducción

En el laboratorio ejecuté scripts Python para analizar datos rurales (leche, maíz, ventas y clima) almacenados en CSV. El objetivo técnico fue usar el entorno de programación de forma ordenada: verificar dependencias/rutas, explorar estructura del dataset, aplicar limpieza (detección de datos sospechosos) y generar reportes automáticos.

---

## 2. Evidencias de navegación del entorno

Incluí capturas de:

- Proyecto abierto en VS Code.
- Carpetas `data`, `src`, `reportes`, `evidencias` y `docs`.
- Terminal integrada.

Función de cada carpeta:

- `data/`: almacena los archivos CSV de entrada.
- `src/`: contiene los scripts Python del flujo del laboratorio (00 a 06).
- `reportes/`: genera salidas finales (CSV, PNG, TXT).
- `evidencias/`: contiene la bitácora e informe final.
- `docs/`: documentación del laboratorio (diccionario, guía docente, rúbrica, etc.).

---

## 3. Preparación del entorno

Incluí capturas de:

- `python --version` (3.14.3)
- creación/activación del entorno virtual
- `pip install -r requirements.txt`

Preparar el entorno antes de ejecutar scripts es clave para asegurar reproducibilidad, evitar errores por dependencias faltantes y garantizar que las rutas y versiones de librerías sean consistentes.

---

## 4. Exploración de datos

Incluí evidencia de `01_explorar_datos.py` y se exploraron 5 CSV:

- `produccion_leche.csv`
- `ventas_productos.csv`
- `cosecha_maiz.csv`
- `inventario_animales.csv`
- `clima_vereda.csv`

- El archivo con más registros fue `produccion_leche.csv` (10,000 filas).
- Columnas importantes: cantidades/medidas (p. ej. `litros`, `kg`), identificadores (p. ej. finca/vereda) y métricas económicas (p. ej. precios).
- Problemas/faltantes: se observaron valores nulos en columnas numéricas y/o inconsistencias que requerían filtrado antes de calcular indicadores.

---

## 5. Análisis y reportes

Ejecuté `02_analizar_produccion.py` y `03_generar_reporte.py`. En `reportes/` se generaron archivos como CSV, gráficos PNG y un reporte TXT consolidado.

Resultados principales (resumen del reporte TXT):

- Leche válida: 107,711.85 litros
- Promedio leche válida: 10.85 litros
- Maíz válido: 1,271,406.05 kg
- Lluvia promedio: 8.46 mm
- Valor total de ventas válidas: $4,030,132,882 COP

---

## 6. Depuración de errores

Se corrigieron errores en `05_script_con_errores.py`:

- Error: `KeyError` por una columna inexistente (ej. `litros_producidos`).
  - Solución: usar el nombre real de la columna (ej. `litros`) o ajustar el acceso al DataFrame.

- Error: `SyntaxError` en una instrucción `print`.
  - Solución: corregir la sintaxis (paréntesis/cierre de comillas).

(En el documento final se incluyen capturas del error antes y después de corregir, y la tabla de errores documentados.)

---

## 7. Comparación técnica del entorno

Matriz (resumen) basada en el desarrollo del laboratorio:

- Funcionalidad: alta (pandas para análisis, matplotlib para gráficos, scripts reproducibles).
- Compatibilidad: buena con CSV y estructura del proyecto (rutas relativas y generación automática de reportes).
- Costo: bajo (software libre y sin infraestructura adicional).
- Rendimiento: adecuado para datasets grandes; el uso de `pandas` permite operaciones vectorizadas y agregaciones eficientes.
- Facilidad de uso: buena en VS Code por la ejecución por scripts, la depuración y la organización de archivos.

---

## 8. Conclusión

- Sí, el entorno fue adecuado para trabajar con datos grandes porque permitió análisis y generación de reportes de forma automática y consistente.
- El criterio más importante fue la funcionalidad y compatibilidad (poder ejecutar el flujo completo sin fricción).
- Mejoraría: completar más evidencias capturando salidas relevantes de terminal y valores intermedios durante la exploración.
- Recomendaría este entorno para futuros proyectos, especialmente rurales, porque facilita la depuración, el control de versiones del código y la creación de indicadores a partir de múltiples CSV.

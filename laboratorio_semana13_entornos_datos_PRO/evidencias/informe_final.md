## Laboratorio avanzado Semana 13 (Informe resuelto)

### Portada
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

---

## 3. Preparación del entorno
Se realizó:
- `python --version` → 3.14.3
- Creación de entorno virtual (venv)
- Instalación de dependencias con `pip install -r requirements.txt`

Esto asegura reproducibilidad y evita fallos por dependencias faltantes.

---

## 4. Exploración de datos
Se exploraron 5 CSV. El archivo con más registros fue `produccion_leche.csv` (10,000 filas). Se observaron faltantes en columnas numéricas y la necesidad de validar/convertir tipos antes de calcular indicadores.

---

## 5. Análisis y reportes
Se ejecutaron `02_analizar_produccion.py` y `03_generar_reporte.py`. En la carpeta `reportes/` se generaron salidas como:
- CSV de indicadores (resúmenes)
- Gráficos PNG
- Un reporte técnico TXT consolidado

Indicadores principales (resumen del reporte TXT):
- Leche válida: 107,711.85 litros
- Promedio leche válida: 10.85 litros
- Maíz válido: 1,271,406.05 kg
- Lluvia promedio: 8.46 mm
- Valor total ventas válidas: $4,030,132,882 COP

---

## 6. Depuración de errores
Se corrigieron 2 errores en `05_script_con_errores.py`:
- **KeyError** por una columna inexistente (`litros_producidos`) → se usó el nombre real de la columna (`litros`).
- **SyntaxError** por una instrucción `print` mal escrita (paréntesis/comillas) → se corrigió la sintaxis.

---

## 7. Comparación técnica del entorno
A continuación se presenta la matriz (1 a 5) basada en lo ejecutado durante el laboratorio:

| Criterio | Valoración 1 a 5 | Justificación técnica | Evidencia usada |
|---|---:|---|---|
| Funcionalidad | 5 | VS Code permitió abrir la carpeta del proyecto, editar scripts, ejecutar en terminal integrada y revisar trazas de error; además soporta generación de reportes desde `src/` y evidencia en `reportes/`. | Capturas de ejecución y archivos en `reportes/`. |
| Compatibilidad | 5 | Funciona bien con Python y CSV grandes gracias a rutas relativas (Path) y uso de librerías (pandas/matplotlib) desde un entorno virtual. | `python --version`, `pip install -r requirements.txt`. |
| Costo | 5 | Es gratuito y no requiere infraestructura adicional (solo equipo local y acceso a archivos). | Análisis del software usado. |
| Rendimiento | 4 | Los CSV con miles de registros se procesaron adecuadamente usando operaciones vectorizadas en pandas; no hubo bloqueos. | Tiempo percibido y salidas en terminal. |
| Facilidad de uso | 4 | La organización por carpetas (`data/`, `src/`, `reportes/`) y la depuración por traceback facilitaron corregir errores. | Bitácora técnica y ejecución paso a paso. |
| Documentación | 4 | Los comentarios/estructura de los scripts y la documentación en `docs/` guiaron el flujo y ayudaron a entender errores de columnas y lógica. | `docs/explicacion_bloque_a_bloque.md` y `README`. |
| Recomendación final | 5 | Adecuado para contexto educativo rural: permite reproducir análisis, depurar errores y generar reportes consistentes con bajo costo. | Conclusión argumentada + resultados del laboratorio. |

---

## 8. Conclusión
- Sí, el entorno fue adecuado para trabajar con datos grandes porque permitió el análisis y la generación automática de reportes de forma consistente.
- El criterio más importante fue la **funcionalidad y compatibilidad**, ya que el flujo completo (verificar → explorar → analizar → reportar → depurar) se ejecutó sin fricción.
- Lo que mejoraría del proceso es reforzar las evidencias de terminal (salidas intermedias) para sustentar con más capturas cada decisión de limpieza/filtros.
- Recomendaría este entorno para futuros proyectos, especialmente rurales, porque facilita la depuración, la organización del código y la creación de indicadores a partir de múltiples CSV.


# Matriz de comparación técnica de entornos

Completa esta matriz después de ejecutar el laboratorio. Usa una valoración de 1 a 5.

| Criterio | Pregunta guía | Valoración 1 a 5 | Justificación técnica | Evidencia usada |
|---|---|---:|---|---|
| Funcionalidad | ¿El entorno permitió abrir carpetas, editar código, usar terminal, ejecutar scripts, revisar errores y generar reportes? | 5 | VS Code permitió abrir el proyecto, editar los scripts en `src/`, ejecutar en terminal, ver trazas/errores y generar archivos en `reportes/` (CSV/PNG/TXT). | Salida de ejecución de `00-03`, archivos generados en `reportes/` y depuración en `05`. |
| Compatibilidad | ¿Funcionó correctamente con tu equipo, sistema operativo, Python, CSV y librerías? | 5 | Se ejecutó con Python 3.14.3 y librerías de `requirements.txt`. Los CSV se leyeron y procesaron en pandas con rutas relativas usando `Path`. | `python src/00_verificar_entorno.py` + ejecuciones `01-03`. |
| Costo | ¿Es gratuito? ¿Requiere licencia, internet constante o equipo potente? | 5 | Herramientas y librerías son gratuitas; no se requiere infraestructura adicional más allá de equipo local e internet ocasional para instalación. | Análisis del software usado. |
| Rendimiento | ¿Procesó los CSV grandes sin bloquearse o demorarse demasiado? | 4 | `produccion_leche.csv` (10,000 filas) se procesó rápidamente con operaciones vectorizadas en pandas sin bloqueos. | Evidencias de ejecución y tiempos percibidos en terminal. |
| Facilidad de uso | ¿Fue fácil encontrar archivos, terminal, errores, extensiones y resultados? | 4 | La estructura por carpetas (`data/`, `src/`, `reportes/`) y la depuración por traceback facilitaron identificar problemas. | Organización del proyecto + correcciones en `05`. |
| Documentación | ¿La guía, comentarios del código y mensajes fueron suficientes para avanzar? | 4 | Los bloques y comentarios en cada script guiaron el flujo (rutas, carga CSV, conversiones, filtros, exportación). | `README.md`, `GUIA_ESTUDIANTE.md` y docstrings/bloques en `src/*.py`. |
| Recomendación final | ¿Recomendarías este entorno para una institución educativa rural? | 5 | Permite reproducir análisis, generar reportes automáticamente, y depurar errores con bajo costo y buena compatibilidad. | Conclusión basada en el laboratorio + resultado de reportes/errores. |

## Interpretación sugerida

- 1: Muy bajo o no cumple.
- 2: Cumple parcialmente con dificultades importantes.
- 3: Cumple de manera aceptable.
- 4: Cumple bien y con pocas dificultades.
- 5: Cumple de forma excelente para el contexto.


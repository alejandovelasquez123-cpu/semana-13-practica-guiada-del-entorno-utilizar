# Preguntas orientadoras para discusión o cierre



1. **¿Qué diferencia hay entre abrir un archivo suelto y abrir una carpeta completa de proyecto?**
   - Abrir un archivo suelto permite trabajar solo con ese contenido, pero pierdes el contexto del proyecto (estructura, rutas, configuraciones y archivos relacionados). Abrir la carpeta completa carga el *workspace*, habilita navegación/búsquedas globales, y aplica configuraciones y dependencias del proyecto.

2. **¿Por qué conviene usar terminal integrada dentro del entorno?**
   - Porque centraliza la ejecución y depuración sin salir del editor: mantiene la ruta de trabajo del proyecto, facilita crear/activar el entorno virtual, ejecutar scripts y revisar errores en el mismo lugar.

3. **¿Qué ventaja tiene un entorno virtual en Python?**
   - Aísla las dependencias por proyecto (versiones controladas). Así se evitan conflictos entre librerías de distintos trabajos y el laboratorio se puede reproducir con las mismas versiones.

4. **¿Qué pasaría si se ejecuta un script sin instalar sus dependencias?**
   - Fallará en los `import` con errores como `ModuleNotFoundError` (o errores por incompatibilidad de versiones si hay librerías pero en versiones incorrectas).

5. **¿Por qué los archivos CSV grandes son útiles para una práctica técnica?**
   - Permiten practicar lectura y tratamiento de datos “reales”: manejo de volumen, carga a estructuras (p. ej., DataFrames), limpieza/validación y análisis con tiempos razonables, además de enseñar a pensar en rendimiento.

6. **¿Qué diferencia hay entre dato faltante, dato sospechoso y dato válido?**
   - **Faltante**: no hay valor (vacío/NA/Null).
   - **Sospechoso**: hay valor pero es inconsistente o raro (p. ej., negativos donde no aplica, fechas fuera de rango, formatos/etiquetas extrañas).
   - **Válido**: cumple reglas y rangos esperados, consistente con el resto de la información.

7. **¿Qué criterio técnico pesa más en una institución rural: funcionalidad, compatibilidad o costo? Justifica.**
   - En general pesa más **funcionalidad y costo de forma conjunta**: debe resolver el problema y además ser sostenible (instalación/mantenimiento/recursos limitados). La **compatibilidad** es esencial para que el sistema realmente se pueda usar, pero si no es viable por costo o falta de infraestructura, no se adopta.

8. **¿Por qué la depuración sistemática es mejor que cambiar código al azar?**
   - Porque reduce el tiempo de solución: se identifica el error, se reproduce, se aísla la causa (logs/validaciones), y se prueba cada cambio. Cambiar al azar suele ocultar el problema o introducir nuevos errores.

9. **¿Qué evidencias demuestran que el entorno sí fue funcional?**
   - Que al instalar requisitos y ejecutar los scripts principales no aparecen errores de dependencias/importación, y que se generan los resultados esperados (reportes/archivos/outputs) según el flujo del laboratorio.

10. **¿Qué mejoras propondrías para una segunda versión del laboratorio?**
   - Validaciones más explícitas (columnas esperadas, tipos/rangos), mensajes de error más claros, automatización de ejecución (comandos listos), y evidencias/logs mejor estructurados para facilitar la reproducibilidad y la corrección de fallos.


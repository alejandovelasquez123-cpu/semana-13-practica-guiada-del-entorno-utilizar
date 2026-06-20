# Laboratorio avanzado Semana 13
## Análisis de datos rurales y comparación técnica de entornos de programación

Este laboratorio está diseñado para que el estudiante abra una carpeta completa en **Visual Studio Code** u otro entorno compatible con Python, navegue por sus archivos, ejecute comandos en la terminal, procese archivos CSV con miles de registros, interprete salidas, corrija errores y evalúe técnicamente el entorno usado.

La actividad fortalece tres criterios técnicos:

| Criterio | Qué se evalúa en el laboratorio |
|---|---|
| Funcionalidad | Si el entorno permite abrir carpetas, editar código, ejecutar scripts, usar terminal, instalar librerías, revisar errores y generar reportes. |
| Compatibilidad | Si funciona con el equipo disponible, el sistema operativo, Python, librerías externas y archivos CSV grandes. |
| Costo | Si el entorno es gratuito, si exige internet constante, si requiere equipos potentes y si es sostenible para una institución educativa. |

---

## 1. Contexto del reto

La comunidad educativa de la vereda **El Progreso** necesita analizar información productiva de varias fincas: producción de leche, cosecha de maíz, inventario de animales, ventas y clima. El equipo técnico debe comprobar si el entorno de programación permite trabajar con datos grandes, generar reportes y solucionar errores de manera eficiente.

El objetivo no es solamente obtener resultados numéricos. El objetivo principal es que el estudiante aprenda a **usar el entorno con criterio técnico**, documentando cada paso mediante capturas, bitácora y comparación final.

---

## 2. Estructura del proyecto

```text
laboratorio_semana13_entornos_datos_PRO/
├── data/                    # Archivos CSV con miles de registros simulados
├── src/                     # Scripts Python del laboratorio
├── reportes/                # Aquí se generan archivos de salida automáticamente
├── evidencias/              # Plantillas para bitácora e informe final
├── docs/                    # Rúbrica, checklist, matriz y explicación bloque a bloque
├── README.md                # Guía rápida para abrir y ejecutar el proyecto
├── GUIA_ESTUDIANTE.md       # Guía completa del laboratorio paso a paso
└── requirements.txt         # Librerías necesarias para ejecutar los scripts
```

### Qué significa cada carpeta

| Carpeta | Función |
|---|---|
| `data/` | Contiene la información base. El estudiante no debe borrar ni modificar estos archivos. |
| `src/` | Contiene los programas Python que se ejecutan desde la terminal. |
| `reportes/` | Recibe los resultados generados por los scripts. Al inicio puede estar vacía. |
| `evidencias/` | Incluye plantillas para documentar el proceso y preparar la entrega. |
| `docs/` | Incluye material de apoyo: matriz de comparación, rúbrica, checklist y explicación de bloques. |

---

## 3. Instalación rápida

Abre la carpeta completa en VS Code. Luego abre la terminal integrada y ejecuta:

```bash
python --version
```

Si Python aparece correctamente, crea un entorno virtual:

```bash
python -m venv .venv
```

Activa el entorno virtual según tu sistema operativo:

### Windows PowerShell

```bash
.venv\Scripts\Activate.ps1
```

### Windows CMD

```bash
.venv\Scripts\activate.bat
```

### macOS o Linux

```bash
source .venv/bin/activate
```

Instala las librerías:

```bash
pip install -r requirements.txt
```

---

## 4. Orden recomendado de ejecución

Ejecuta los scripts en este orden:

```bash
python src/00_verificar_entorno.py
python src/01_explorar_datos.py
python src/02_analizar_produccion.py
python src/03_generar_reporte.py
python src/04_comparar_entorno.py
python src/05_script_con_errores.py
python src/06_reto_estudiante.py
```

El archivo `05_script_con_errores.py` contiene errores intencionales. Su objetivo es que el estudiante practique diagnóstico y depuración. No debe saltarse esa fase.

---

## 5. Entrega final

El estudiante debe entregar en Moodle un PDF con:

1. Portada.
2. Captura del proyecto abierto en VS Code.
3. Captura de la versión de Python.
4. Captura de la instalación de dependencias.
5. Captura de la exploración de CSV.
6. Captura del análisis de producción.
7. Captura del reporte generado.
8. Evidencia del script con errores antes y después de corregir.
9. Bitácora técnica diligenciada.
10. Matriz de comparación técnica.
11. Conclusión final.

---

## 6. Recomendación importante

Antes de ejecutar cada script, lee los comentarios internos del archivo. Están escritos por bloques para que entiendas qué hace cada sección: rutas, carga de datos, validación, cálculo, agrupación, generación de reportes y salida en terminal.

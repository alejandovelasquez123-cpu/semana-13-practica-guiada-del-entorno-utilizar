# Diccionario de datos del laboratorio

Este documento explica las columnas principales de cada archivo CSV. Úsalo cuando aparezcan errores de columna o cuando necesites interpretar resultados.

## `produccion_leche.csv`

| Columna | Significado |
|---|---|
| `id_registro` | Identificador único del registro. |
| `fecha` | Día en que se registró la producción. |
| `finca` | Nombre de la finca. |
| `codigo_animal` | Identificador del animal asociado al registro. |
| `turno` | Momento del registro: mañana o tarde. |
| `litros` | Litros de leche registrados. |
| `temperatura_c` | Temperatura aproximada durante el registro. |
| `observacion` | Comentario del registro. |
| `tecnico` | Persona responsable del registro. |

## `cosecha_maiz.csv`

| Columna | Significado |
|---|---|
| `id_cosecha` | Identificador de la cosecha. |
| `fecha` | Fecha de cosecha o registro. |
| `finca` | Finca donde se reporta la cosecha. |
| `lote` | Lote o zona de producción. |
| `kilos_cosechados` | Cantidad cosechada en kilogramos. |
| `humedad_grano_pct` | Humedad del grano en porcentaje. |
| `estado_cultivo` | Estado del cultivo. |
| `lluvia_ultimos_7_dias_mm` | Lluvia acumulada reciente. |

## `ventas_productos.csv`

| Columna | Significado |
|---|---|
| `id_venta` | Identificador de venta. |
| `fecha` | Fecha de venta. |
| `finca` | Finca que realizó la venta. |
| `producto` | Producto vendido. |
| `cantidad` | Cantidad vendida. |
| `unidad` | Unidad de medida. |
| `precio_unitario_cop` | Precio por unidad en pesos colombianos. |
| `comprador` | Comprador o canal de venta. |
| `medio_pago` | Forma de pago. |

## `inventario_animales.csv`

| Columna | Significado |
|---|---|
| `codigo_animal` | Identificador del animal. |
| `finca` | Finca donde está registrado. |
| `raza` | Raza del animal. |
| `edad_meses` | Edad en meses. |
| `peso_kg` | Peso aproximado en kilogramos. |
| `estado_sanitario` | Estado de salud o control sanitario. |
| `ultima_vacuna` | Fecha de última vacuna registrada. |
| `responsable` | Persona encargada. |

## `clima_vereda.csv`

| Columna | Significado |
|---|---|
| `id_clima` | Identificador del registro climático. |
| `fecha` | Fecha de observación. |
| `zona` | Zona de la vereda. |
| `temperatura_promedio_c` | Temperatura promedio en grados Celsius. |
| `lluvia_mm` | Lluvia registrada en milímetros. |
| `humedad_relativa_pct` | Humedad relativa en porcentaje. |
| `observacion_climatica` | Estado general del clima. |

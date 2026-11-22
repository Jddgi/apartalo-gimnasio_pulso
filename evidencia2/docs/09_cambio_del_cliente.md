# 9. El cliente cambió de opinión
> Evidencia 2 · Ejercicio 1 · Temas 5, 6 y 7 · 🎩 PO

**El aviso de mi cliente (cópialo tal cual):** Mariana: "Cerca hay una universidad. Quiero un plan para estudiantes."

Nuevo plan Estudiante: 8 clases al mes incluidas y $60 por cada clase extra. Los otros planes siguen igual.

**Regla que cambia:** R1 

## 9.1 La historia del cambio

- Issue nuevo: #22
- Historia original: #6

## 9.2 Análisis de impacto

| Elemento (historia, `.feature`, prueba, función, documento) | ¿Cambia, se queda igual o hay que revisarlo? | Por qué |
|---|---|---|
|Historia original R1 |Hay que revisarlo |La regla original sigue existiendo, pero ahora se agrega un nuevo plan Estudiante. |
|Historia nueva: Plan Estudiante |Cambia |Implementa el cambio solicitado por el cliente. |
|Archivo .feature de R1 |Cambia |Deben agregarse escenarios para el plan Estudiante. |
|Tabla FIT de R1 |Cambia |Deben añadirse casos del nuevo plan. |
|Pruebas unitarias de R1 |Cambia |Deben validarse las nuevas reglas del plan Estudiante. |
|Pruebas de aceptación de R1 |Cambia |Deben agregarse ejemplos para el nuevo plan. |
|calcular_cobro_extra() en reglas.py |Cambia |Debe soportar el nuevo plan Estudiante. |
|procesar_cancelacion() en reglas.py |Se queda igual |El cambio no afecta la regla R2. |
|Documentación de R1 |Hay que revisarlo |Debe reflejar el nuevo comportamiento del sistema. |
|Escenarios y pruebas de R2 |Se queda igual |La cancelación de clases no fue modificada. |

## 9.3 Refinamiento

- **Prioridad (MoSCoW):**
- **Puntos:**
- **¿Cabe en mi carga máxima actualizada?** (ver `10_sprint2_planeacion.md`)
- **Si la dividí:** subhistorias #, #

## 9.4 Escenarios actualizados

Archivo modificado: `features/<archivo>.feature`

Valores límite nuevos que agregué:

## 9.5 Tabla FIT: antes y después

> Llena la última columna con tu **predicción** antes de tocar el código. En el Ejercicio 3 agrega la columna "Resultado real".

| (entrada) | (entrada) | Esperado antes del aviso | Esperado ahora | ¿Mi código actual pasaría? (predicción) | Resultado real |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |
| | | | | | |

## 9.6 Reflexión: ¿por qué en cascada sería caro?


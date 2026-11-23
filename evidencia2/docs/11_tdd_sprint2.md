# 11. TDD del Sprint 2
> Evidencia 2 · Ejercicio 3 · Temas 8 y 9 · 🎩 desarrollador

## 11.1 Una regresión de verdad

**Commit ROJO** (pruebas con la regla nueva): ROJO: pruebas con la regla nueva de plan estudiante

**Commit VERDE** (código corregido): VERDE: agrega soporte para plan estudiante

Salida de pytest en ROJO:

```text
================== FAILURES ==================

test_cobro_extra[Estudiante-8-0]

E   ValueError: plan desconocido

test_cobro_extra[Estudiante-9-60]

E   ValueError: plan desconocido

test_cobro_extra[Estudiante-10-120]

E   ValueError: plan desconocido

test_cobro_extra[Estudiante-12-240]

E   ValueError: plan desconocido

============================
4 failed, 12 passed
============================
```

- **¿Cuántas pruebas fallaron y cuáles?** Fallaron 4 pruebas: las correspondientes al nuevo plan Estudiante con 8, 9, 10 y 12 clases. Todas fallaron porque el código de la Evidencia 1 todavía no reconocía ese plan.
- **¿Acerté en mi predicción de la tabla FIT?** Sí. En la tabla FIT predije que todas las filas asociadas al plan Estudiante fallarían porque el código todavía no contemplaba ese plan. El resultado real coincidió con la predicción.
- **¿El defecto estaba en la prueba o en el código?** El defecto estaba en el código. Las pruebas reflejaban correctamente la nueva necesidad del cliente, mientras que la implementación todavía respondía a la regla anterior.
- **¿Qué pasaría si "arreglara" la prueba sin hablar con el PO?** Estaría ignorando el nuevo requisito del cliente y ocultando el problema real. Las pruebas dejarían de validar la necesidad actual del negocio y el sistema seguiría entregando un comportamiento incorrecto para los usuarios.

## 11.2 R3 con TDD

Función: `reglas.<nombre>()`

| Ciclo | Commit ROJO | Commit VERDE | Commit REFACTOR (si hubo) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |

Decisiones de PO sobre dudas de R3:

## 11.3 R3 de escenario a prueba

- `.feature`: `features/<archivo>.feature`
- Prueba de aceptación: `tests/aceptacion/<archivo>.py`

## 11.4 Un requisito no funcional más

- **Restricción:** #
- **Por qué esta y no otra:**
- **Prueba:** `tests/rnf/<archivo>.py`
- **Cómo quedó mi DoD:**

## 11.5 Cobertura de R3

- **Caminos** (cada `return` y cada `raise`):
- **Caminos que recorren mis pruebas:**
- **Cobertura:**
- **Resultado final de `pytest`:** ___ passed

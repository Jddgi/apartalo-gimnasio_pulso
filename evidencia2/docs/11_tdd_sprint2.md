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

Función: `reglas.procesar_cancelacion()`

| Ciclo | Commit ROJO | Commit VERDE | Commit REFACTOR (si hubo) |
|---|---|---|---|
| 1 |ROJO: prueba cancelación con 3 horas |VERDE: permite cancelar con 3 horas sin penalización |REFACTOR: simplifica condiciones de cancelación |
| 2 |ROJO: prueba horas negativas |VERDE: valida horas negativas con ValueError |REFACTOR: mejora validación de entradas |

Decisiones de PO sobre dudas de R3: Se decidió que exactamente 3 horas antes de la clase cuentan como una cancelación válida y la clase no cuenta como tomada.

También se decidió que cualquier cantidad negativa de horas es un dato inválido y debe producir un ValueError, ya que una cancelación después del inicio de la clase no tiene sentido para la operación del gimnasio.

## 11.3 R3 de escenario a prueba

- `.feature`: `features/r3_cancelacion.feature`
- Prueba de aceptación: `tests/aceptacion/test_r3_aceptacion.py`

## 11.4 Un requisito no funcional más

- **Restricción:** ##RNF-01 Rendimiento de reservas en hora pico
- **Por qué esta y no otra:** Se eligió esta restricción porque el nuevo plan Estudiante puede incrementar el número de usuarios utilizando la aplicación. Por ello resulta importante verificar que el sistema siga respondiendo correctamente bajo una alta carga de reservas.
- **Prueba:** `tests/rnf/test_rnf_rendimiento.py`
- **Cómo quedó mi DoD:** Una historia no puede considerarse terminada hasta que:
1.Cumpla sus criterios de aceptación.
2.Las pruebas unitarias y de aceptación pasen correctamente.
3.La cobertura de caminos identificados sea satisfactoria.
4.Las pruebas RNF de rendimiento pasen correctamente.
5.La documentación asociada esté actualizada.

## 11.5 Cobertura de R3

- **Caminos** (cada `return` y cada `raise`): La función procesar_cancelacion() tiene 3 caminos:

raise ValueError cuando las horas son negativas.
return cuando la cancelación ocurre con 3 horas o más de anticipación.
return cuando la cancelación ocurre con menos de 3 horas de anticipación.
- **Caminos que recorren mis pruebas:** Las pruebas recorren:

Cancelación con 5 horas → camino 2 ✅
Cancelación con 3 horas → camino 2 ✅
Cancelación con 2 horas → camino 3 ✅
Cancelación con 0 horas → camino 3 ✅
Horas negativas (-1) → camino 1 ✅
- **Cobertura:** Caminos totales: 3

Caminos recorridos por las pruebas: 3

Cobertura = 3 / 3 × 100 = 100 %
- **Resultado final de `pytest`:** 20 passed

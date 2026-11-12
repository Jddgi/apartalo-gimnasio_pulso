# 7. Requisitos no funcionales
> Ejercicio 7 · Tema 9 · 🎩 PO y 🎩 desarrollador
> Cada restricción va como **issue** (formulario "Requisito no funcional"). Aquí va el resumen.

| Issue | Restricción SMART | Externa / interna | Cualidad | Historia (T) | Prueba práctica (Tabla 2) o práctica (Tabla 4) |
|---|---|---|---|---|---|
| #RNF-01 |El sistema debe procesar hasta 200 solicitudes de reserva en un periodo de 5 minutos durante la apertura diaria de reservas, manteniendo un tiempo de respuesta menor a 2 segundos por solicitud. |Interna |Desempeño |#HU-01 |Prueba de carga simulando 200 solicitudes de reserva en 5 minutos y verificando que el tiempo de respuesta permanezca por debajo de 2 segundos. |
| #RNF-02 |El sistema debe mantener una disponibilidad mínima del 99 % durante el horario de apertura de reservas (6:00 a.m. a 7:00 a.m.). |Interna |Disponibilidad |#HU-01|Prueba de disponibilidad monitoreando el sistema durante la apertura de reservas y verificando que permanezca disponible al menos el 99 % del tiempo. |
| #RNF-03 |Las funciones que implementan las reglas R1 y R2 deberán mantener una cobertura del 100 % de los caminos identificados mediante pruebas unitarias y de aceptación. |Interna |Mantenibilidad |#HU-06|Desarrollo guiado por pruebas (TDD), pruebas automatizadas y revisión de cobertura de caminos antes de considerar terminada una funcionalidad. |

## 7.3 La que compruebo con código

- **Restricción:** #RNF-03 Mantenibilidad de las reglas de negocio (#número_real_del_issue)
- **Prueba:** `tests/rnf/test_rnf_robustez.py`

## 7.4 Una por sprint

- **La que agrego a mi DoD en el Sprint 1:** RNF-03 Mantenibilidad de las reglas de negocio. Se agrega al DoD porque está directamente relacionada con el trabajo realizado en este sprint. Además, ya se implementaron pruebas unitarias, pruebas de aceptación, cobertura de caminos y una prueba RNF que permiten verificar su cumplimiento de manera objetiva.
- **Las que dejo para después y por qué:**RNF-01 Rendimiento de reservas en hora pico y RNF-02 Disponibilidad del sistema de reservas se dejan para sprints posteriores porque requieren pruebas de carga, monitoreo y simulación de múltiples usuarios concurrentes. En este sprint el enfoque estuvo en implementar y validar las reglas de negocio R1 y R2, por lo que aún no se cuenta con una aplicación completa que permita medir esas características de forma realista.

# 14. Cierre de la versión 1.0
> Evidencia 2 · Ejercicio 6 · Temas 4 y 11

## Parte A — Métricas: Sprint 1 contra Sprint 2

Fecha de la segunda fotografía (`metricas/tablero_s2.tsv`): 23.11.2026

| Consulta | Resultado |
|---|---|
| a) Comprometidos y entregados de cada sprint | Sprint 1: comprometidos 21, entregados 18. Sprint 2: comprometidos 18, entregados 18. |
| b) Velocidad del periodo de cada sprint y del periodo completo |Sprint 1: 18 ÷ 21 = 0.86 (86%). Sprint 2: 18 ÷ 18 = 1.00 (100%). Periodo completo: 36 ÷ 39 = 0.92 (92%). |
| c) Tiempo de ciclo promedio de cada sprint |Sprint 1: 4 días. Sprint 2: 3 días. |
| d) Historias que pasaron del Sprint 1 al Sprint 2 |R3 e implementación de documentación asociada a R3. |
| e) Puntos que quedan y sprints que faltan |Restan 12 puntos. Con velocidad de 18 puntos por sprint se requiere aproximadamente 1 sprint adicional. |

**Interpretación:**
- ¿Mejoré del Sprint 1 al Sprint 2? Sí. En el Sprint 1 se entregó el 86% de los puntos comprometidos, mientras que en el Sprint 2 se entregó el 100%. Además, el tiempo de ciclo promedio bajó de 4 a 3 días, indicando una mejora en la capacidad de entrega y en la planificación.
- ¿El pronóstico del Ejercicio 2 se parece al de la consulta e)? ¿Por qué? Sí. Ambos pronósticos indican que el trabajo restante puede completarse aproximadamente en un sprint adicional. Esto ocurre porque utilizan como referencia la velocidad real observada durante el Sprint 2, que representa mejor el desempeño actual del equipo.

## Parte B — Revisión del Sprint 2 · 🎩 PO

| Historia | ¿Cumple sus criterios? | ¿Aceptada? | Evidencia |
|---|---|---|---|
| # - Nuevo plan Estudiante |Si |Si |Commit VERDE: agrega soporte para plan estudiante + salida de pytest en verde |
| # – Implementar R3|Si |Si |Commit VERDE: permite cancelación de reservas según R3 + prueba test_r3_aceptacion.py |
| # – Requisito no funcional de rendimiento|Si |Si |Archivo tests/rnf/test_rnf_rendimiento.py ejecutado correctamente |
| # – Actualización de escenarios y documentación |Si |Si |Captura del archivo .feature actualizado y tabla FIT corregida |

**Reacción de mi cliente → historia nueva para el Sprint 3:** #23 “Me gusta el nuevo plan Estudiante. Creo que también sería útil ofrecer promociones especiales para estudiantes durante periodos de inscripción o inicio de semestre.”

## Parte C — Retrospectiva del Sprint 2 · 🎩 SM

- **¿Funcionaron las acciones del Sprint 1?** Sí. Las dos acciones definidas en la retrospectiva anterior ayudaron a mejorar el resultado del Sprint 2. Se actualizaron las pruebas antes de modificar el código y se mantuvieron los escenarios y la documentación sincronizados con los cambios solicitados por el cliente. Esto redujo errores y permitió entregar todas las historias comprometidas.
- **¿Qué salió bien?** La incorporación del nuevo plan Estudiante se realizó sin afectar las funcionalidades existentes. También mejoró la cobertura de pruebas, el Sprint 2 cumplió el 100% de los puntos comprometidos y la documentación se mantuvo actualizada durante el desarrollo.
- **¿Qué hay que mejorar?** Las métricas y el seguimiento del burndown todavía dependen de actividades manuales. Además, algunas tareas técnicas fueron más difíciles de estimar de lo esperado, por lo que conviene mejorar la planeación y automatizar parte del seguimiento.
- **Acciones para un Sprint 3:**
  1. Automatizar la recopilación de métricas y reportes para reducir trabajo manual durante el cierre de cada sprint.
  2. Incrementar la cobertura de pruebas de requisitos no funcionales para identificar problemas de rendimiento y calidad antes de liberar cambios.

## Parte D — La versión 1.0 · 🎩 desarrollador

- `CHANGELOG.md` actualizado
- Tag: `v1.0`
- Tag: v1.0
- Comando utilizado:
git tag -a v1.0 -m "Versión 1.0: Sprint 2 de Apártalo"
git push origin v1.0

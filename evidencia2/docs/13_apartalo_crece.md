# 13. Apártalo crece
> Evidencia 2 · Ejercicio 5 · Tema 10 · 🎩 SM de toda la empresa

## 13.1 La estructura

¿Figura 1, Figura 2 o una combinación? Por qué: Usaría una combinación de la Figura 1 y la Figura 2. El núcleo común (reservas, pagos y cancelaciones) se administraría con un backlog compartido y equipos coordinados mediante Scrum de Scrums. Las funcionalidades específicas de cada cliente tendrían sus propios backlogs, priorizados por Product Owners distintos y coordinados por un Product Manager.
<img width="767" height="567" alt="image" src="https://github.com/user-attachments/assets/fcc4ca49-1a07-495e-9e65-7cdc1d091ed4" />

Mi variante: Gimnasio Pulso
→ Equipo Cliente A
Núcleo común:
→ Reservas
→ Pagos
→ Cancelaciones

![Estructura de Apártalo](img/estructura_apartalo.png)

| Equipo | Integrantes (devs, testers, otros) | Backlog | PO | Qué construye |
|---|---|---|---|---|
|Equipo Núcleo |8 devs, 2 testers, 1 DBA |Backlog Núcleo |PO Núcleo |Reservas, pagos y cancelaciones compartidas |
|Equipo Cliente A |7 devs, 2 testers, 1 diseñador |Backlog Cliente A |PO Cliente A |Gimnasio Pulso y clientes similares |
|Equipo Cliente B |7 devs, 2 testers, 1 diseñador |Backlog Cliente B |PO Cliente B |Resto de clientes y personalizaciones |

¿Hay *Product Manager*? ¿Quién?
Sí. Existe un Product Manager encargado de coordinar los Product Owners de cada línea de producto, priorizar iniciativas globales y resolver conflictos entre los distintos backlogs.

## 13.2 Los tamaños, justificados

- Regla de Deloitte 1 (más de 10 se divide): Apártalo tiene 34 personas en total. Siguiendo la regla de Deloitte, un equipo con más de 10 integrantes debe dividirse. Por ello se organizaron tres equipos de entre 10 y 12 personas aproximadamente, evitando grupos demasiado grandes que dificulten la coordinación.
- Regla de Deloitte 2 (un par de testers por cada 4 o 5 desarrolladores): La empresa cuenta con 22 desarrolladores y 6 testers. Esto permite asignar aproximadamente 2 testers por cada equipo de 7 u 8 desarrolladores, manteniendo una proporción cercana a la recomendada de un par de testers por cada 4 o 5 desarrolladores.
- Otra cifra del Tema 10: También se consideró que los equipos Scrum funcionan mejor con entre 5 y 9 personas dedicadas al desarrollo principal. Mantener equipos pequeños reduce la complejidad de coordinación y mejora la comunicación diaria.
- Qué hago con los 2 DBA y los 2 diseñadores: Los 2 DBA y los 2 diseñadores no se asignan permanentemente a un solo equipo porque son recursos especializados insuficientes para cubrir todos los equipos al mismo tiempo. Trabajan como especialistas compartidos (visitantes), participando en los equipos que los requieran durante cada sprint. Los DBA apoyan el núcleo común y las necesidades de bases de datos, mientras que los diseñadores colaboran en las funcionalidades específicas de los clientes cuando se requiere trabajo de experiencia de usuario o diseño visual.

## 13.3 Scrum de scrums

- **Quién va:** Asisten los Scrum Masters de cada equipo, el Product Manager cuando es necesario y los responsables de componentes compartidos del núcleo común.
- **Cada cuánto:** Dos veces por semana durante 15 a 30 minutos, además de reuniones extraordinarias cuando exista un cambio importante que afecte a varios equipos.
- **Qué se coordina:** Dependencias entre equipos, bloqueos compartidos, cambios en el núcleo común, fechas de entrega, integraciones, riesgos técnicos y prioridades que afectan a más de un backlog.
- **Ejemplo con el cambio de mi cliente:** Mi cliente del Gimnasio Pulso solicitó la creación del nuevo plan Estudiante con reglas especiales para el cálculo de clases incluidas y clases extra. Aunque el cambio surgió en una sola aplicación, la lógica de membresías y cobros forma parte del núcleo común utilizado por otras aplicaciones de Apártalo.

Este cambio debe discutirse en el Scrum de Scrums porque puede afectar funcionalidades compartidas de reservas, pagos y facturación. Los equipos deben acordar cómo modificar el núcleo sin romper las demás aplicaciones que utilizan las mismas funciones comunes.

## 13.4 La colaboración, con mis datos

| Medición | Operación | Resultado |
|---|---|---|
| Velocidad del periodo, Sprint 1 | 18 ÷ 21 |0.86 (86%) |
| Velocidad del periodo, Sprint 2 |18 ÷ 18 |1.00 (100%) |
| Velocidad del periodo completo | (18 + 18) ÷ (21 + 18) |36 ÷ 39 = 0.92 (92%) |
| PO–cliente (0 a 10) | — |9 |
| Equipo–cliente (1 a 10) | — |8 |

Justificación de las calificaciones de mi cliente: La relación PO–cliente se califica con 9 porque existió comunicación constante durante los dos sprints. El cliente pudo solicitar cambios importantes, como el nuevo plan Estudiante, y estos fueron atendidos e incorporados al backlog sin conflictos.

La relación equipo–cliente se califica con 8 porque el trabajo entregado cumplió los criterios de aceptación y se respondieron los cambios solicitados. Sin embargo, la comunicación normalmente ocurrió a través del Product Owner y no directamente entre el cliente y el desarrollo.

**La relación más débil y qué cambiaría primero:** La relación más débil es equipo–cliente. Para mejorarla, incorporaría demostraciones más frecuentes y sesiones de retroalimentación directa con los usuarios finales durante cada Sprint Review. Esto permitiría validar antes las funcionalidades y detectar expectativas incorrectas con mayor rapidez.

## 13.5 Las estrategias

| Característica | ¿La protege mi diseño? | Cómo |
|---|---|---|
| | Sí | |
| | Sí | |
| | Sí | |
| | No del todo | Cómo reduzco el riesgo: |

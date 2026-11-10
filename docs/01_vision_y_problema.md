# 1. Visión y problema correcto
> Ejercicio 1 · Temas 1, 2 y 5 · 🎩 PO
> La visión va en el `README.md`. Aquí van los puntos 2 a 6.

## 1.2 ¿Por qué no cascada?

| Causa de falla de cascada | Cómo se vería en mi proyecto |
|---|---|
|Los requisitos cambian o no están completamente definidos|Mariana aún no está segura de si implementar una lista de espera o mantener el sistema de "primer llegado, primer servido". Esto demuestra que existen requisitos que todavía necesitan validarse y podrían cambiar durante el desarrollo.|
|Necesidad de retroalimentación temprana del usuario |Funciones como el ranking con medallas o la integración con relojes inteligentes podrían no satisfacer las expectativas de los usuarios en el primer intento. Se requiere recibir retroalimentación frecuente para realizar ajustes. |

¿Usaría prototipos? ¿En qué momento y para qué?

Sí utilizaría prototipos al inicio del proyecto para validar el proceso de reservas, la lista de espera y la visualización del ranking. Esto permitiría obtener retroalimentación temprana de Mariana y de los socios antes de desarrollar la solución completa.

## 1.3 El manifiesto en mi proyecto

| Valor o principio | Decisión concreta en mi proyecto |
|---|---|
| Valor: Individuos e interacciones sobre procesos y herramientas|Realizar reuniones semanales con Mariana para revisar el avance y resolver dudas sobre las reglas de negocio en lugar de depender únicamente de documentación extensa.|
| Valor: Software funcionando sobre documentación exhaustiva|Entregar al final del Sprint 1 una versión funcional de reservas y control de cupos en lugar de producir únicamente documentos de análisis.|
| Principio: Nuestra mayor prioridad es satisfacer al cliente mediante la entrega temprana y continua de software con valor.|Implementar primero la reserva de clases y el control de clases disponibles, ya que son las funciones más importantes para el negocio. |
| Principio:Los requisitos pueden cambiar incluso en etapas tardías del desarrollo. |Diseñar el sistema de reservas de forma flexible para poder cambiar entre lista de espera y primer llegado sin rehacer toda la aplicación. |

## 1.4 Frameworks

| Framework | Lo que tomo de él |
|---|---|
| Scrum |Product Backlog, Sprint Planning, Sprints de duración fija, Sprint Review, Sprint Retrospective.|
| Kanban |Tablero visual de tareas, Límites WIP (Work In Progress), Flujo continuo de trabajo, Monitoreo del avance mediante columnas. |
| XP |Desarrollo guiado por pruebas (TDD), Refactorización continua, Integración frecuente, Código simple.|

La combinación de Scrum y Kanban se llama:

La combinación de Scrum y Kanban se conoce como Scrumban.

## 1.5 Requisito o solución

| # | Lo que dijo mi cliente | ¿Requisito o solución? | Si es solución: el requisito que hay detrás |
|---|---|---|---|
| 1 |"Las clases de las 7 de la mañana se llenan y la gente se pelea por el lugar." |Requisito |El sistema debe gestionar la reserva de lugares limitados de forma justa y ordenada. |
| 2 |"Quiero que la app tenga un ranking de quién va más, con medallas." |Solución |El sistema debe incentivar la asistencia y participación de los socios. |
| 3 |"Que el socio vea cuántas clases le quedan en el mes." |Requisito |El usuario debe poder consultar sus clases disponibles según su plan. |
| 4 |"Quiero que se integre con el reloj inteligente de cada socio." |Solución |El sistema debe registrar o consultar información de actividad física del usuario de manera automática. |
| 5 |"No sé si hacer lista de espera o dejar que se apunte el primero que llegue." |Solución |El sistema debe administrar la alta demanda de clases cuando se agoten los lugares disponibles. |
**Profe, no entendí mucho si solo son los requisitos los que se ponen en la última columna, pero por si acaso porgo ambos casos.

## 1.6 Incertidumbre

- **Incertidumbre del *qué*:** alta, porque la cliente aún no decide cómo gestionar la alta demanda de las clases cuando se llenan los cupos. En particular, no sabe si usar una lista de espera o permitir que se registre únicamente quien llegue primero.
- **Incertidumbre del *cómo*:** baja, porque la implementación técnica de reservas, control de cupos (20 lugares), lista de espera (5 personas), ranking de usuarios, control de planes e integración con dispositivos es conocida y existen tecnologías para desarrollarla.
- **Zona del diagrama:** Qué desconocido / Cómo conocido (alta incertidumbre en el qué y baja incertidumbre en el cómo).
- **Qué haré en este sprint para bajar la incertidumbre del *qué*:** crearé un prototipo de las dos alternativas (lista de espera y primer llegado, primer servido), lo revisaré con Mariana y recopilaré retroalimentación para determinar cuál satisface mejor la necesidad de administrar la alta demanda de las clases de las 7:00 a.m. y las horas pico de reservas.

# 2. El product backlog
> Ejercicio 2 · Tema 6 · 🎩 PO
> Las historias van como **issues** (formulario "Historia de usuario"). Aquí va lo demás.

## 2.1 Roles

| Rol | Quién es | Qué desea |
|---|---|---|
|Socio |Cliente del gimnasio que reserva y asiste a clases. |Entrenar diariamente |
|Instructor |Responsable de impartir las clases y registrar asistencia. |Brindar el mejor servicio posible |
|Reloj Inteligente (rol no humano) |Dispositivo externo que comparte información de actividad física con la aplicación. |aclarar dudas del usuario |

## 2.4 Plantilla invertida: historias que me faltaban

`Para poder <beneficio>, como <rol>, quiero <deseo>`

| Beneficio que revisé | Historia que encontré | Issue |
|---|---|---|
|Que el socio no olvide sus clases reservadas |Como socio, quiero recibir recordatorios antes del inicio de una clase, para asistir puntualmente a mis reservas. | #5 |
|Administrar mejor la demanda de los horarios |Como administradora Mariana, quiero identificar las clases con mayor demanda, para tomar decisiones sobre horarios y capacidad. | #8 |

¿Cómo me ayudó ordenar por beneficio?

Pensar primero en el beneficio permitió identificar necesidades que no eran evidentes al revisar únicamente las funcionalidades existentes. Al analizar qué beneficios esperaba obtener cada usuario, descubrí la necesidad de enviar recordatorios de clases y generar estadísticas sobre la demanda de horarios. Estas historias complementan el backlog porque aportan valor tanto para los socios como para la administración del gimnasio.

## 2.5 Glosario (lenguaje ubicuo)

| Término | Qué significa para mi cliente |
|---|---|
|Socio |Cliente inscrito en el gimnasio. |
|Reserva Registro anticipado de un lugar en una clase.|Registro anticipado de un lugar en una clase. |
|Cupo |Número máximo de participantes permitidos en una clase (20). |
|Lista de espera |Cola de máximo 5 personas cuando el cupo está lleno. |
|Clase extra |Clase tomada por encima de las incluidas en la membresía mensual. |

## 2.6 El iceberg

- **En la punta:** Las historias relacionadas con reservar clases, consultar clases disponibles, cancelar reservas, controlar los cupos de 20 lugares, gestionar la lista de espera y visualizar las clases restantes del mes. Estas funcionalidades cubren las reglas de negocio principales (R1, R2 y R3) y son esenciales para el funcionamiento del gimnasio.
- **En el fondo:** Las épicas de integración con relojes inteligentes y el sistema de recompensas con ranking y medallas. También se encuentran las funcionalidades avanzadas de análisis y gamificación que requieren mayor definición.
- **Por qué:** Los elementos de la punta aportan el mayor valor al negocio y tienen requisitos más claros, por lo que deben desarrollarse primero. En cambio, las épicas del fondo son más grandes, tienen mayor incertidumbre y necesitan dividirse en historias más pequeñas antes de poder implementarse adecuadamente.

# language: es

Característica: Cancelación de una clase

  Esquema del escenario: Determinar consecuencia de una cancelación

    Dado que un socio cancela una clase con <horas> horas de anticipación
    Y el socio <asistencia>

    Cuando el sistema procesa la cancelación

    Entonces el resultado es "<resultado>"

    Ejemplos:
      | horas | asistencia      | resultado                         |
      | 3     | se presenta      | Clase devuelta                    |
      | 2.99  | se presenta      | Clase tomada                      |
      | 0     | se presenta      | Clase tomada                      |
      | 5     | no se presenta   | Clase tomada y multa de 50 pesos  |

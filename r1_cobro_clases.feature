# language: es

Característica: Cobro de clases extra del mes

  Esquema del escenario: Calcular cobro por clases excedentes

    Dado que un socio tiene el plan <plan>
    Y ha tomado <clases> clases en el mes

    Cuando el sistema calcula el cobro extra

    Entonces el cobro extra es de <cobro> pesos

    Ejemplos:
      | plan       | clases | cobro |
      | Basico     | 8      | 0     |
      | Basico     | 9      | 90    |
      | Plus       | 16     | 0     |
      | Plus       | 17     | 70    |
      | Ilimitado  | 30     | 0     |

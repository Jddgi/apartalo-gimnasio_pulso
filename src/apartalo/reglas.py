"""Reglas de negocio de mi variante (Ejercicio 6).

Aquí van las funciones de R1 y R2. Escríbelas con TDD:
primero una prueba que falle (ROJO), luego el código mínimo para que pase (VERDE),
y después mejora el código sin romper las pruebas (REFACTOR).

Si una entrada no tiene sentido (horas negativas, un servicio que no existe, etc.),
la función debe lanzar ValueError.
"""
def calcular_cobro_extra(plan, clases_tomadas):
    """
    R1 - Cobro de clases extra del mes
    """

    if clases_tomadas < 0:
        raise ValueError("Las clases tomadas no pueden ser negativas")

    plan = plan.lower()

    if plan == "basico":
        clases_incluidas = 8
        precio_extra = 90

    elif plan == "plus":
        clases_incluidas = 16
        precio_extra = 70

    elif plan == "ilimitado":
        return 0

    else:
        raise ValueError("Plan no válido")

    clases_extra = max(0, clases_tomadas - clases_incluidas)

    return clases_extra * precio_extra


def procesar_cancelacion(horas_anticipacion, no_se_presento=False):
    """
    R2 - Cancelación de una clase
    """

    if horas_anticipacion < 0:
        raise ValueError("Las horas no pueden ser negativas")

    if no_se_presento:
        return {
            "clase_devuelta": False,
            "cuenta_como_tomada": True,
            "multa": 50
        }

    if horas_anticipacion >= 3:
        return {
            "clase_devuelta": True,
            "cuenta_como_tomada": False,
            "multa": 0
        }

    return {
        "clase_devuelta": False,
        "cuenta_como_tomada": True,
        "multa": 0
    }

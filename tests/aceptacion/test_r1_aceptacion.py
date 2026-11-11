import pytest

from apartalo.reglas import calcular_cobro_extra


@pytest.mark.aceptacion
@pytest.mark.parametrize(
    "plan,clases,cobro",
    [
        ("basico", 8, 0),
        ("basico", 9, 90),
        ("plus", 16, 0),
        ("plus", 17, 70),
        ("ilimitado", 30, 0),
    ]
)
def test_cobro_extra(plan, clases, cobro):

    # Dado
    # un socio con un plan y cierta cantidad de clases tomadas

    # Cuando
    resultado = calcular_cobro_extra(plan, clases)

    # Entonces
    assert resultado == cobro

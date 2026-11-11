import pytest

from apartalo.reglas import procesar_cancelacion


@pytest.mark.aceptacion
@pytest.mark.parametrize(
    "horas,no_show,esperado",
    [
        (3, False, "devuelta"),
        (2.99, False, "tomada"),
        (0, False, "tomada"),
        (5, True, "multa"),
    ]
)
def test_cancelacion(horas, no_show, esperado):

    # Dado
    # una cancelación de clase

    # Cuando
    resultado = procesar_cancelacion(
        horas,
        no_show
    )

    # Entonces
    if esperado == "devuelta":
        assert resultado["clase_devuelta"]

    elif esperado == "tomada":
        assert resultado["cuenta_como_tomada"]

    else:
        assert resultado["multa"] == 50

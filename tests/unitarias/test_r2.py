from apartalo.reglas import procesar_cancelacion


def test_cancelacion_menos_de_3_horas():
    resultado = procesar_cancelacion(2)

    assert resultado["cuenta_como_tomada"] is True

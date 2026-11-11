from apartalo.reglas import procesar_cancelacion


def test_cancelacion_menos_de_3_horas():

    resultado = procesar_cancelacion(2)

    assert resultado["cuenta_como_tomada"] is True


def test_cancelacion_con_3_horas():

    resultado = procesar_cancelacion(3)

    assert resultado["clase_devuelta"] is True


def test_no_show():

    resultado = procesar_cancelacion(
        5,
        no_se_presento=True
    )

    assert resultado["multa"] == 50

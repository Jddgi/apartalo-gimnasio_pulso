from apartalo.reglas import calcular_cobro_extra


def test_basico_sin_extras():

    assert calcular_cobro_extra(
        "basico",
        8
    ) == 0


def test_basico_con_extra():

    assert calcular_cobro_extra(
        "basico",
        9
    ) == 90


def test_plus_con_extra():

    assert calcular_cobro_extra(
        "plus",
        17
    ) == 70


def test_ilimitado():

    assert calcular_cobro_extra(
        "ilimitado",
        30
    ) == 0

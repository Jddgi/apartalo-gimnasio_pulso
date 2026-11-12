import pytest

from apartalo.reglas import procesar_cancelacion


@pytest.mark.rnf
def test_horas_negativas_lanzan_error():

    with pytest.raises(ValueError):
        procesar_cancelacion(-1)

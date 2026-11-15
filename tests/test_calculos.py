def calcular_energia(potencia, tempo):
    return potencia * tempo


def test_calcular_energia():
    assert calcular_energia(10, 2) == 20
    
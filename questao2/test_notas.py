import pytest
from notas import validar_nota, calcular_media


@pytest.mark.parametrize("nota", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
def test_validar_notas_validas(nota):
    assert validar_nota(nota)


@pytest.mark.parametrize("nota", [-1, -100, -200, -2, 100, 11, 12, 120])
def test_validar_notas_invalidas(nota):
    assert not validar_nota(nota)


@pytest.mark.parametrize(
    "n1, n2, n3, resultado", [(7, 8, 7, 7.33), (7.5, 8.5, 6, 7.33), (7.5, 6.5, 8, 7.33)]
)
def test_calcular_media_notas_validas(n1, n2, n3, resultado):
    assert calcular_media(n1, n2, n3) == resultado


@pytest.mark.parametrize(
    "n1, n2, n3", [(-1, 10, 8), (10, 12, 11), (100, -10, 11), (10, 80, 9), (0, 3, -1)]
)
def test_calcular_media_notas_invalidas(n1, n2, n3):
    with pytest.raises(ValueError, match="Invalid grades were detected."):
        calcular_media(n1, n2, n3)

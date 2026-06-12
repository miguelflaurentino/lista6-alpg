import pytest
from main import calculator
from sum import sum
from subtraction import subtraction
from multiply import multiply
from division import division
from result import result


@pytest.mark.parametrize(
    "value, esperado",
    [
        (4.0, 4),
        (3.5, 3.5),
        (1.333333, 1.33),
        (0.0, 0),
        (-2.0, -2),
        (-1.5, -1.5),
    ],
)
def test_result(value, esperado):
    assert result(value) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (1.5, 1.5, 3),
        (1.1, 2.2, 3.3),
        (-3, -2, -5),
    ],
)
def test_sum(a, b, esperado):
    assert sum(a, b) == pytest.approx(esperado, rel=1e-2)


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (5, 3, 2),
        (0, 0, 0),
        (1, 1, 0),
        (3.5, 1.5, 2),
        (1.0, 3.0, -2),
        (-2, -5, 3),
    ],
)
def test_subtraction(a, b, esperado):
    assert subtraction(a, b) == pytest.approx(esperado, rel=1e-2)


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (3, 4, 12),
        (0, 100, 0),
        (-2, 3, -6),
        (-2, -3, 6),
        (1.5, 2, 3),
        (2.5, 4, 10),
    ],
)
def test_multiply(a, b, esperado):
    assert multiply(a, b) == pytest.approx(esperado, rel=1e-2)


# --- division ---


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 2, 5),
        (7, 2, 3.5),
        (-6, 3, -2),
        (1, 3, 0.33),
        (0, 5, 0),
        (9, 4, 2.25),
    ],
)
def test_division(a, b, esperado):
    assert division(a, b) == pytest.approx(esperado, rel=1e-2)


def test_division_por_zero():
    with pytest.raises(ZeroDivisionError):
        division(10, 0)


@pytest.mark.parametrize(
    "operacao, a, b, esperado",
    [
        (1, 3, 2, 5),
        (2, 10, 4, 6),
        (3, 3, 4, 12),
        (4, 10, 2, 5),
        (4, 7, 2, 3.5),
    ],
)
def test_calculator_operacoes_validas(operacao, a, b, esperado):
    assert calculator(operacao, a, b) == pytest.approx(esperado, rel=1e-2)


def test_calculator_divisao_por_zero():
    resultado = calculator(4, 10, 0)
    assert resultado == "Você não pode dividir um número por zero.\nTente novamente."


def test_calculator_sair():
    assert calculator(5, 0, 0) == "Fim do programa!"


@pytest.mark.parametrize("operacao_invalida", [0, 6, -1, 100])
def test_calculator_operacao_invalida(operacao_invalida):
    resultado = calculator(operacao_invalida, 1, 1)
    assert resultado == "Você digitou um valor inválido.\nTente novamente."

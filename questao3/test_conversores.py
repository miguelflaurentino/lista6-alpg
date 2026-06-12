import pytest
from conversores import celsius_para_fahrenheit, fahrenheit_para_celsius


@pytest.mark.parametrize("celsius, resultado", [(0, 32), (100, 212)])
def test_celsius_2_fahrenheit(celsius, resultado):
    assert celsius_para_fahrenheit(celsius) == pytest.approx(resultado)


@pytest.mark.parametrize("fahrenheit, resultado", [(32, 0), (212, 100)])
def test_fahrenheit_2_celsius(fahrenheit, resultado):
    assert fahrenheit_para_celsius(fahrenheit) == pytest.approx(resultado)

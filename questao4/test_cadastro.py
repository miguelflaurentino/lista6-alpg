import pytest
from cadastro import classificar_idade, validar_idade


@pytest.mark.parametrize(
    "idade, resultado_esperado",
    [
        (0, "Criança"),  # Limite inferior
        (11, "Criança"),  # Limite superior
        (12, "Adolescente"),
        (17, "Adolescente"),
        (18, "Adulto"),
        (59, "Adulto"),
        (60, "Idoso"),
        (120, "Idoso"),
    ],
)
def test_classificacoes_idade(idade, resultado_esperado):
    assert classificar_idade(idade) == resultado_esperado


@pytest.mark.parametrize("idade_invalida", [-1, -50, 121, 200])
def test_validar_idade_invalida_limites(idade_invalida):
    with pytest.raises(ValueError, match="Idade inválida"):
        validar_idade(idade_invalida)


# def test_validar_idade_valida():
#     assert validar_idade(20)
#
#
# def test_validar_idade_invalida_negativa():
#     with pytest.raises(ValueError, match="Idade inválida"):
#         validar_idade(-1)
#
#
# def test_validar_idade_invalida_acima_limite():
#     with pytest.raises(ValueError, match="Idade inválida"):
#         validar_idade(121)
#
#
# def test_classificar_idade_crianca():
#     assert classificar_idade(2) == "Criança"
#
#
# def test_classificar_idade_adolescente():
#     assert classificar_idade(12) == "Adolescente"
#
#
# def test_classificar_idade_adulto():
#     assert classificar_idade(20) == "Adulto"
#
#
# def test_classificar_idade_idoso():
#     assert classificar_idade(120) == "Idoso"
#
#
# def test_classificar_idade_invalida():
#     with pytest.raises(ValueError, match="Idade inválida"):
#         classificar_idade(-19)

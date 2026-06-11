def validar_idade(idade: int) -> bool:
    if idade < 0 or idade > 120:
        raise ValueError("Idade inválida")

    return True


def classificar_idade(idade: int) -> str:
    validar_idade(idade)

    if 0 <= idade <= 11:
        return "Criança"
    elif 12 <= idade <= 17:
        return "Adolescente"
    elif 18 <= idade <= 59:
        return "Adulto"
    else:
        return "Idoso"

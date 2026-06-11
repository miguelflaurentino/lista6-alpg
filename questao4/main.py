from cadastro import classificar_idade


def main():
    try:
        idade = int(input("Digite a idade para validar: "))

        return f"Classificação: {classificar_idade(idade)}"
    except ValueError:
        return "Erro: Idade deve ser um número inteiro entre 0 e 120."


print(main())

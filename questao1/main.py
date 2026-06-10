from tabulate import tabulate
from sum import sum
from subtraction import subtraction
from multiply import multiply
from division import division


def exibir_mensagem():
    print("Calculadora simples em Python")


exibir_mensagem()
print()


def values():
    a = float(input("Digite o primeiro número para a operação: "))
    b = float(input("Digite o segundo número para a operação: "))
    return (a, b)


def calculator(operation, a, b):
    try:
        if operation < 1 or operation > 5:
            raise ValueError()

        match operation:
            case 1:
                return sum(a, b)
            case 2:
                return subtraction(a, b)
            case 3:
                return multiply(a, b)
            case 4:
                try:
                    if b == 0:
                        raise ZeroDivisionError()

                    return division(a, b)
                except ZeroDivisionError:
                    return "Você não pode dividir um número por zero.\nTente novamente."
            case 5:
                return "Fim do programa!"
            case _:
                raise ValueError()

    except ValueError:
        return "Você digitou um valor inválido.\nTente novamente."


def main() -> None:

    data = [
        ["1", "Soma"],
        ["2", "Subtração"],
        ["3", "Multiplicação"],
        ["4", "Divisão"],
        ["5", "Sair"],
    ]

    while True:
        try:
            print(tabulate(data, headers=[" ", "Opção"], tablefmt="simple"))
            opcao = int(input("Qual operação deseja fazer? "))

            if opcao < 1 or opcao > 5:
                raise ValueError()

        except ValueError:
            print("Você digitou um valor inválido.\nTente novamente.")
            print()
            continue

        if opcao == 5:
            print("Fim do programa.")
            break

        if opcao in (1, 2, 3, 4):
            a, b = values()
            print(calculator(opcao, a, b))
        else:
            print("Você digitou um valor inválido.\nTente novamente.")

        print()


main()

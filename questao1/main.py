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
                print(sum(a, b))
                print()
            case 2:
                print(subtraction(a, b))
                print()
            case 3:
                print(multiply(a, b))
                print()
            case 4:
                try:
                    if b == 0:
                        raise ZeroDivisionError()

                    print(division(a, b))
                except ZeroDivisionError:
                    print()
                    print("=-" * 15 + "=")
                    print("Você não pode dividir um número por zero.\nTente novamente.")
                    print("=-" * 15 + "=")
                finally:
                    print()
            case 5:
                return print("Fim do programa!")
            case _:
                raise ValueError()

    except Exception:
        print()
        print("=-" * 15 + "=")
        print("Você digitou um valor inválido.\nTente novamente.")
        print("=-" * 15 + "=")
        print()


def main() -> None:

    data = [
        ["1", "Soma"],
        ["2", "Subtração"],
        ["3", "Multiplicação"],
        ["4", "Divisão"],
        ["5", "Sair"],
    ]

    print(tabulate(data, headers=[" ", "Opção"], tablefmt="simple"))
    opcao = int(input("Qual operação deseja fazer? "))

    if opcao == 5:
        return print("Fim do programa.")

    a, b = values()
    calculator(opcao, a, b)

    main()


main()

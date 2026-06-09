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


def main() -> None:

    data = [
        ["1", "Soma"],
        ["2", "Subtração"],
        ["3", "Multiplicação"],
        ["4", "Divisão"],
        ["5", "Sair"],
    ]

    try:
        print(tabulate(data, headers=[" ", "Opção"], tablefmt="simple"))
        opcao = int(input("Qual operação deseja fazer? "))

        if opcao < 1 or opcao > 5:
            raise ValueError()

        match opcao:
            case 1:
                a, b = values()
                print(sum(a, b))
                print()
                main()
            case 2:
                a, b = values()
                print(subtraction(a, b))
                print()
                main()
            case 3:
                a, b = values()
                print(multiply(a, b))
                print()
                main()
            case 4:
                try:
                    a, b = values()
                    if b == 0:
                        raise ZeroDivisionError()

                    print(division(a, b))
                except ZeroDivisionError:
                    print("Você não pode digitar um número por zero.\nTente novamente.")
                finally:
                    print()
                    main()
            case 5:
                return print("Fim do programa!")
            case _:
                raise ValueError()

    except Exception as e:
        print()
        print("=-" * 15 + "=")
        print("Você digitou um valor inválido.\nTente novamente.")
        print("=-" * 15 + "=")
        print()

        main()


main()

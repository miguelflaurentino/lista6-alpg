from tabulate import tabulate


def exibir_mensagem():
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
    except Exception as e:
        print(e)


exibir_mensagem()

def validar_nota(nota: float) -> bool:
    if nota < 0 or nota > 10:
        return False

    return True


def calcular_media(n1: float, n2: float, n3: float) -> float:
    if not validar_nota(n1) or not validar_nota(n2) or not validar_nota(n3):
        raise ValueError("Invalid grades were detected.")

    return round((n1 + n2 + n3) / 3, 2)


def main():
    try:
        print("Type the three grades separated between spaces.")
        print("The grades must be between 0 and 10.")
        n1, n2, n3 = input("Type here: ").split(" ")
        n1 = float(n1)
        n2 = float(n2)
        n3 = float(n3)

        media = calcular_media(n1, n2, n3)
        print(round(media, 2) if media - int(media) > 0 else round(media, 1))
    except ValueError:
        print("You've typed a wrong value. Try again.")


if __name__ == "__main__":
    main()

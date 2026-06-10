def validar_nota(nota):
    try:
        if nota < 0 or nota > 10:
            raise ValueError()
        
        return True
    except ValueError:
        return False
    except Exception:
        print("An error has occured.")
        return False


def calcular_media(n1, n2, n3):
    try:
        if not validar_nota(n1) or not validar_nota(n2) or not validar_nota(n3):
            raise ValueError()

        return round((n1 + n2 + n3) / 3, 2)
    except ValueError:
        return "You've typed a wrong value. Try again."
    
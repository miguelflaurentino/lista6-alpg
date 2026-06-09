def result(value: float):
    if value - int(value) != 0:
        return round(value, 2)

    return int(value)


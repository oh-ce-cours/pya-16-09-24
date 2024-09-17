def is_multiple(nombre, dividende):
    return nombre % dividende == 0


def regle_fizz_buzz(nombre):
    res = ""
    if is_multiple(nombre, 3):
        res += "fizz"
    if is_multiple(nombre, 5):
        res += "buzz"
    if not res:
        res = str(nombre)
    return res


def main():
    for nombre in range(1, 16):
        res = regle_fizz_buzz(nombre)
        print(res)

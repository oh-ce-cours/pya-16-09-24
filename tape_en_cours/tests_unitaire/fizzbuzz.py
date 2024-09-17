def is_multiple(nombre, dividende):
    return nombre % dividende == 0


def regle_fizz_buzz(nombre):
    res = ""
    if nombre % 3 == 0:
        res = "fizz"
    if nombre % 5 == 0:
        res = "buzz"
    if not res:
        res = str(nombre)
    return res


# for nombre in range(1, 16):
#     res = regle_fizz_buzz(nombre)
#     print(res)

def is_multiple(nombre, dividende):
    return nombre % dividende == 0


def regle_fizz_buzz(nombre):
    res = None
    match is_multiple(nombre, 3), is_multiple(nombre, 5):
        case True, True:
            res = "fizzbuzz"
        case True, False:
            res = "fizz"
        case False, True:
            res = "buzz"
        case False, False:
            res = str(nombre)
    return res


for nombre in range(1, 16):
    res = regle_fizz_buzz(nombre)
    print(res)

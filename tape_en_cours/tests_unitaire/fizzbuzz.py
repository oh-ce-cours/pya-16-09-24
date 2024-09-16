def multiple(nombre, dividende):
    return nombre % dividende == 0


for nombre in range(1, 16):
    res = None
    match multiple(nombre, 3), multiple(nombre, 5):
        case True, True:
            res = "fizzbuzz"
        case True, False:
            res = "fizz"
        case False, True:
            res = "buzz"
        case False, False:
            res = str(nombre)
    print(res)

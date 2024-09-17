import random


def regle_du_jeu(nombre_propose: int, nombre_a_deviner: int) -> int:
    if nombre_propose > nombre_a_deviner:
        return 1
    elif nombre_propose < nombre_a_deviner:
        return -1
    return 0


def game():
    cible = random.randint(1, 100)
    print("triche (cible) :", cible)
    while True:
        termine = False
        nombre_propose = int(input("Entrez un nombre : "))
        resultat = regle_du_jeu(nombre_propose, cible)
        if termine:
            break

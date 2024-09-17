from enum import Enum
import random


class Position(Enum):
    PLUS = 1
    MOINS = -1
    EGAL = 0


def dis_la_phrase(position: int) -> str:
    if position == Position.PLUS:
        return "Le nombre a trouver est plus petit"
    if position == Position.MOINS:
        return "Le nombre a trouver est plus grand"
    return ""


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
        nombre_propose = int(input("Entrez un nombre : "))
        resultat = regle_du_jeu(nombre_propose, cible)
        print(dis_la_phrase(resultat))
        if resultat == 0:
            break


def main():
    game()


if __name__ == "__main__":
    main()

from enum import Enum
import random


class Position(Enum):
    PLUS = 1
    MOINS = -1
    EGAL = 0


class Phrases(Enum):
    PLUS = "Le nombre a trouver est plus petit"
    MOINS = "Le nombre a trouver est plus grand"
    INPUT = "Entrez un nombre : "
    TERMINE = "Bravo"


def dis_la_phrase(position: int) -> str:
    if position == Position.PLUS.value:
        return Phrases.PLUS.value
    if position == Position.MOINS.value:
        return Phrases.MOINS.value
    return ""


def regle_du_jeu(nombre_propose: int, nombre_a_deviner: int) -> int:
    if nombre_propose > nombre_a_deviner:
        return Position.PLUS.value
    elif nombre_propose < nombre_a_deviner:
        return Position.MOINS.value
    return Position.EGAL.value


def game():
    cible = random.randint(1, 100)
    print("triche (cible) :", cible)
    while True:
        nombre_propose = int(input())
        resultat = regle_du_jeu(nombre_propose, cible)
        ihm = dis_la_phrase(resultat)
        if resultat == 0:
            break
        print(ihm)
    print("Bravo")


def main():
    game()


if __name__ == "__main__":
    main()

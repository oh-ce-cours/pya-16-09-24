from enum import Enum
import random


class Position(Enum):
    PLUS = 1
    MOINS = -1
    EGAL = 0


class PhrasesFrancais(Enum):
    PLUS = "Le nombre a trouver est plus petit"
    MOINS = "Le nombre a trouver est plus grand"
    INPUT = "Entrez un nombre : "
    TERMINE = "Bravo"


class PhrasesEnglish(Enum):
    PLUS = "Le number a trouver is plus petit"
    MOINS = "Le number a trouver is plus grand"
    INPUT = "Enter a nombre : "
    TERMINE = "Congrats"


def dis_la_phrase(position: int, phrases) -> str:
    if position == Position.PLUS.value:
        return phrases.PLUS.value
    if position == Position.MOINS.value:
        return phrases.MOINS.value
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
    phrases_dans_la_langue = ...
    while True:
        nombre_propose = int(input(Phrases.INPUT.value))
        resultat = regle_du_jeu(nombre_propose, cible)
        ihm = dis_la_phrase(resultat)
        if resultat == 0:
            break
        print(ihm)
    print(Phrases.TERMINE.value)


def main():
    game()


if __name__ == "__main__":
    main()

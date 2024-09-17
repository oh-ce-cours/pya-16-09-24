def regle_du_jeu(nombre_propose: int, nombre_a_deviner: int) -> int:
    if nombre_propose > nombre_a_deviner:
        return 1
    elif nombre_propose < nombre_a_deviner:
        return -1
    return 0

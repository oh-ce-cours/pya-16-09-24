import plus_moins


def test_nombre_propose_plus_petit_que_cible():
    # arange
    nombre_propose = 4
    nombre_a_deviner = 10
    attendu = -1
    # act
    resultat = plus_moins.regle_du_jeu(nombre_propose, nombre_a_deviner)
    # assert
    assert resultat == attendu


def test_nombre_propose_plus_grand_que_cible():
    # arange
    nombre_propose = 40
    nombre_a_deviner = 11
    attendu = 1
    # act
    resultat = plus_moins.regle_du_jeu(nombre_propose, nombre_a_deviner)
    # assert
    assert resultat == attendu


def test_nombre_propose_egal_cible():
    # arange
    nombre_propose = 13
    nombre_a_deviner = 13
    attendu = 0
    # act
    resultat = plus_moins.regle_du_jeu(nombre_propose, nombre_a_deviner)
    # assert
    assert resultat == attendu


def test_dis_la_phrase_cest_plus():
    # arange
    position = 1
    attendu = "Le nombre a trouver est plus petit"
    # act
    resultat = plus_moins.dis_la_phrase(position)
    # assert
    assert resultat == attendu

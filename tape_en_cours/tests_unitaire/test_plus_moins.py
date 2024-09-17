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
    nombre_a_deviner = 10
    attendu = -1
    # act
    resultat = plus_moins.regle_du_jeu(nombre_propose, nombre_a_deviner)
    # assert
    assert resultat == attendu

from fizzbuzz import is_multiple, regle_fizz_buzz


def test_multiple():
    assert not is_multiple(3, 5)
    assert is_multiple(3, 3)
    assert is_multiple(25, 5)
    assert not is_multiple(5, 3)


def test_fizzbuzz_multiple_3_est_fizz():
    # arange
    nombre = 3
    attendu = "fizz"
    # act
    result = regle_fizz_buzz(nombre)
    # assert
    assert result == attendu

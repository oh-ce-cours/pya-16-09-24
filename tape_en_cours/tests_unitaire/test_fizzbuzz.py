from fizzbuzz import is_multiple


def test_multiple():
    assert is_multiple(3, 5) == False
    assert is_multiple(3, 3) == True
    assert is_multiple(5, 5) == True
    assert is_multiple(5, 3) == False

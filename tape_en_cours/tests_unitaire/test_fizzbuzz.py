from fizzbuzz import is_multiple


def test_multiple():
    assert not is_multiple(3, 5)
    assert is_multiple(3, 3)
    assert is_multiple(25, 5)
    assert not is_multiple(5, 3)

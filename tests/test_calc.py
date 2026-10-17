from calc import add, divide


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(6, 3) == 2


def test_subtract():
    from calc import subtract
    assert subtract(5, 3) == 2


def test_multiply():
    from calc import multiply
    assert multiply(4, 3) == 12

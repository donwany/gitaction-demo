from mathz.add import add, multiply, divide

def test_add():
    assert 2 == add(1, 1)

def test_multiply():
    assert 10 == multiply(2, 5)

def test_divide():
    assert 10 == divide(20, 2)
    assert 10 == divide(20, 0)
from mathz.add import add, multiply

def test_add():
    assert 2 == add(1, 1)

def test_multiply():
    assert 10 == multiply(2, 5)
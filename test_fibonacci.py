import pytest
from fibonacci import fibonacci

def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 1


def test_fibonacci_small_numbers():
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8


def test_fibonacci_large_numbers():
    assert fibonacci(10) == 55
    assert fibonacci(20) == 6765
    assert fibonacci(30) == 832040
    assert fibonacci(40) == 102334155


def test_fibonacci_negative_numbers():
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_fibonacci_float_numbers():
    with pytest.raises(TypeError):
        fibonacci(2.5)


def test_fibonacci_string_input():
    with pytest.raises(TypeError):
        fibonacci("5")

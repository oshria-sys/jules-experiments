import pytest
from calculator import add, subtract, multiply, divide, power, modulo

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_power():
    assert power(2, 3) == 8

def test_modulo():
    assert modulo(10, 3) == 1

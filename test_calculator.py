import pytest
from calculator import *
def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0   
def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(-1, -1) == 0   
def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 1) == -1
    assert multiply_numbers(0, 5) == 0   
def test_divide_numbers():
    assert divide_numbers(6, 3) == 2
    assert divide_numbers(5, 2) == 2.5
    assert divide_numbers(5, 0) == "Error: Division by zero is not allowed."   
def test_power_numbers():
    assert power_numbers(2, 3) == 8
    assert power_numbers(5, 0) == 1
    assert power_numbers(3, 2) == 9   
def test_modulo_numbers():
    assert modulo_numbers(5, 3) == 2
    assert modulo_numbers(10, 2) == 0
    assert modulo_numbers(7, 4) == 3        

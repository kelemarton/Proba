import pytest
from calculator import calculate_sum, calculate_sub, calculate_multi, calculate_div

def test_calculate_sum():
    assert calculate_sum(1, 2) == 3
    assert calculate_sum(-1, 2) == 1
    assert calculate_sum(-1, -2) == -3
    assert calculate_sum(0, 0) == 0

def test_calculate_sub():
    assert calculate_sub(5, 2) == 3
    assert calculate_sub(-1, 2) == -3
    assert calculate_sub(-1, -2) == 1
    assert calculate_sub(0, 0) == 0

def test_calculate_multi():
    assert calculate_multi(5, 2) == 10
    assert calculate_multi(-1, 2) == -2
    assert calculate_multi(-2, -5) == 10
    assert calculate_multi(0, 0) == 0

def test_calculate_div():
    assert calculate_div(10, 2) == 5
    assert calculate_div(-6, 3) == -2
    assert calculate_div(-10, -5) == 2
    assert calculate_div(0, 0) == "error: Division by zero is not allowed"
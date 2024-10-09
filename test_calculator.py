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
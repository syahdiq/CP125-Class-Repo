import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise3.py')
_spec = importlib.util.spec_from_file_location("exercise3_lab4", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
get_total_value = _module.get_total_value
find_low_stock = _module.find_low_stock
calculate_restock_cost = _module.calculate_restock_cost


def test_get_total_value():
    assert get_total_value([50, 5, 100, 3, 25], [10.00, 25.00, 5.00, 50.00, 15.00]) == 1450.00

def test_get_total_value_simple():
    assert get_total_value([10, 20], [5.00, 10.00]) == 250.00

def test_find_low_stock():
    assert find_low_stock([50, 5, 100, 3, 25], 10) == [1, 3]

def test_find_low_stock_none():
    assert find_low_stock([50, 100, 25], 10) == []

def test_find_low_stock_all():
    assert find_low_stock([5, 3, 8], 10) == [0, 1, 2]

def test_calculate_restock_cost():
    assert calculate_restock_cost([50, 5, 100, 3, 25], [10.00, 25.00, 5.00, 50.00, 15.00], 10, 20) == 1500.00

def test_calculate_restock_cost_none():
    assert calculate_restock_cost([50, 100, 25], [10.00, 5.00, 15.00], 10, 20) == 0.00

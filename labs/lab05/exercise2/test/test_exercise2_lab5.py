import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise2.py')
_spec = importlib.util.spec_from_file_location("exercise2_lab5", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
find_largest_drop = _module.find_largest_drop

def test_standard_drops():
    temps = (32.5, 31.0, 31.5, 28.0, 24.5)
    assert find_largest_drop(temps) == 3.5

def test_no_drops_increasing():
    temps = (20.0, 21.0, 22.0, 23.0)
    assert find_largest_drop(temps) == 0.0

def test_no_drops_stable():
    temps = (25.0, 25.0, 25.0)
    assert find_largest_drop(temps) == 0.0

def test_spike_up_then_down():
    temps = (20.0, 30.0, 25.0)
    assert find_largest_drop(temps) == 5.0

def test_multiple_equal_drops():
    temps = (30.0, 20.0, 25.0, 15.0)
    assert find_largest_drop(temps) == 10.0

def test_very_small_drop():
    temps = (25.0, 24.9, 25.1)
    assert abs(find_largest_drop(temps) - 0.1) < 1e-9

def test_drop_at_start():
    temps = (100.0, 50.0, 60.0, 70.0)
    assert find_largest_drop(temps) == 50.0

def test_drop_at_end():
    temps = (10.0, 20.0, 30.0, 5.0)
    assert find_largest_drop(temps) == 25.0

def test_minimum_readings():
    temps = (10.0, 5.0)
    assert find_largest_drop(temps) == 5.0

def test_large_numbers():
    temps = (1000.0, 999.0, 1000.0)
    assert find_largest_drop(temps) == 1.0

def test_all_decreasing():
    temps = (50, 40, 30, 20, 10)
    assert find_largest_drop(temps) == 10.0

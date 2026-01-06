import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise2.py')
_spec = importlib.util.spec_from_file_location("exercise2_lab4", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
calculate_average = _module.calculate_average
count_passing = _module.count_passing
get_class_summary = _module.get_class_summary


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90.0

def test_calculate_average_with_decimals():
    assert abs(calculate_average([85, 92, 58, 74, 66, 91]) - 77.67) < 0.1

def test_count_passing_all_pass():
    assert count_passing([80, 90, 100], 60) == 3

def test_count_passing_none_pass():
    assert count_passing([40, 50, 55], 60) == 0

def test_count_passing_some_pass():
    assert count_passing([85, 92, 58, 74, 66, 91], 60) == 5

def test_get_class_summary():
    summary = get_class_summary([85, 92, 58, 74, 66, 91], 60)
    assert abs(summary[0] - 77.67) < 0.1
    assert summary[1] == 5
    assert summary[2] == 1

import pytest
import importlib.util
import os

# Load exercise1.py from the parent directory using absolute path
_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise1.py')
_spec = importlib.util.spec_from_file_location("exercise1_lab4", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
find_score_range = _module.find_score_range

def test_basic_case():
    assert find_score_range([72, 85, 90, 68, 95, 78, 88]) == (95, 68)

def test_negative_numbers():
    assert find_score_range([-5, -2, -8, -1, -10]) == (-1, -10)

def test_all_same():
    assert find_score_range([50, 50, 50, 50]) == (50, 50)

def test_two_elements():
    assert find_score_range([10, 20]) == (20, 10)

def test_single_element():
    assert find_score_range([42]) == (42, 42)

def test_highest_at_start():
    assert find_score_range([100, 50, 75, 60]) == (100, 50)

def test_lowest_at_start():
    assert find_score_range([10, 50, 75, 60]) == (75, 10)

def test_highest_at_end():
    assert find_score_range([50, 75, 60, 100]) == (100, 50)

def test_lowest_at_end():
    assert find_score_range([50, 75, 60, 10]) == (75, 10)

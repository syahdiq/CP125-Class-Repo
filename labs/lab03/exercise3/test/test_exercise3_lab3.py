import pytest
import importlib.util
import os

# Load exercise3.py from the parent directory using absolute path
_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise3.py')
_spec = importlib.util.spec_from_file_location("exercise3_lab3", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
has_adjacent_seats = _module.has_adjacent_seats

def test_adjacent_at_start():
    assert has_adjacent_seats([0, 0, 1, 1, 1, 1, 1, 1]) == True

def test_adjacent_at_end():
    assert has_adjacent_seats([1, 1, 1, 1, 1, 1, 0, 0]) == True

def test_adjacent_in_middle():
    assert has_adjacent_seats([1, 0, 0, 1, 0, 1, 0, 0]) == True

def test_no_adjacent():
    assert has_adjacent_seats([1, 0, 1, 0, 1, 0, 1, 0]) == False

def test_all_empty():
    assert has_adjacent_seats([0, 0, 0, 0]) == True

def test_all_taken():
    assert has_adjacent_seats([1, 1, 1, 1]) == False

def test_two_empty_seats():
    assert has_adjacent_seats([0, 0]) == True

def test_two_taken_seats():
    assert has_adjacent_seats([1, 1]) == False

def test_single_seat():
    assert has_adjacent_seats([0]) == False

def test_empty_list():
    assert has_adjacent_seats([]) == False

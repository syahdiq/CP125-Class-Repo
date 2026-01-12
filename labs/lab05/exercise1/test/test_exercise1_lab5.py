import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise1.py')
_spec = importlib.util.spec_from_file_location("exercise1_lab5", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
was_backward_detected = _module.was_backward_detected

def test_backward_in_x():
    path = ((0, 0, 10), (5, 5, 12), (4, 6, 10))
    assert was_backward_detected(path) == True

def test_backward_in_y():
    path = ((0, 0, 0), (10, 10, 0), (11, 9, 0))
    assert was_backward_detected(path) == True

def test_staying_still():
    path = ((5, 5, 5), (5, 5, 5))
    assert was_backward_detected(path) == False

def test_forward_only():
    path = ((0, 0, 0), (1, 1, 1), (2, 2, 2))
    assert was_backward_detected(path) == False

def test_only_z_changes():
    path = ((10, 10, 10), (10, 10, 5), (10, 10, 15))
    assert was_backward_detected(path) == False

def test_backward_at_start():
    path = ((10, 10, 10), (9, 10, 10), (11, 11, 11))
    assert was_backward_detected(path) == True

def test_backward_at_end():
    path = ((0, 0, 0), (10, 10, 0), (9, 10, 0))
    assert was_backward_detected(path) == True

def test_large_jumps_forward():
    path = ((0, 0, 0), (1000, 1000, 1000), (2000, 2000, 2000))
    assert was_backward_detected(path) == False

def test_one_coordinate_backward_one_forward():
    # x increases, y decreases -> backward
    path = ((5, 5, 5), (10, 4, 10))
    assert was_backward_detected(path) == True

def test_minimum_waypoints():
    path = ((0, 0, 0), (0, 0, -1))
    assert was_backward_detected(path) == False

def test_diagonal_forward():
    path = ((0, 0, 0), (1, 2, 3), (2, 4, 6))
    assert was_backward_detected(path) == False

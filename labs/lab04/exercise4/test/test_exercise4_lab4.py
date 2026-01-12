import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise4.py')
_spec = importlib.util.spec_from_file_location("exercise4_lab4", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
analyze_performance = _module.analyze_performance


def test_faded_clear():
    """Second half clearly worse than first half."""
    laps = [60, 62, 61, 63, 65, 68, 70, 72]
    assert analyze_performance(laps) == True


def test_finished_strong_clear():
    """Second half clearly better than first half."""
    laps = [70, 68, 66, 64, 60, 58, 56, 54]
    assert analyze_performance(laps) == False


def test_equal_halves():
    """Both halves have same average - not faded."""
    laps = [60, 62, 58, 60, 60, 62, 58, 60]
    assert analyze_performance(laps) == False


def test_slight_fade():
    """Second half just slightly worse."""
    laps = [50, 50, 50, 50, 51, 51, 51, 51]
    assert analyze_performance(laps) == True


def test_four_laps():
    """Minimum case with 4 laps."""
    laps = [30, 32, 35, 38]
    assert analyze_performance(laps) == True


def test_six_laps():
    """Six laps - even split."""
    laps = [40, 42, 44, 43, 41, 39]
    assert analyze_performance(laps) == False


def test_odd_length_faded():
    """Odd length list - first half is larger. Athlete faded."""
    # 5 laps: first half [50, 55, 60], second half [65, 70]
    laps = [50, 55, 60, 65, 70]
    # First avg: 55.0, Second avg: 67.5 -> Faded
    assert analyze_performance(laps) == True


def test_odd_length_strong():
    """Odd length list - first half is larger. Finished strong."""
    # 5 laps: first half [70, 65, 60], second half [55, 50]
    laps = [70, 65, 60, 55, 50]
    # First avg: 65.0, Second avg: 52.5 -> Finished strong
    assert analyze_performance(laps) == False


def test_seven_laps_faded():
    """Seven laps - first half gets 4, second half gets 3."""
    laps = [40, 42, 44, 46, 50, 55, 60]
    # First half [40, 42, 44, 46] avg: 43.0
    # Second half [50, 55, 60] avg: 55.0 -> Faded
    assert analyze_performance(laps) == True

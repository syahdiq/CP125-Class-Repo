import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise5.py')
_spec = importlib.util.spec_from_file_location("exercise5_lab4", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
find_momentum_days = _module.find_momentum_days


def test_basic_momentum():
    """Standard case with multiple momentum days."""
    prices = [100, 102, 105, 107, 106, 108, 112, 114]
    # Changes: +2, +3, +2, -1, +2, +4, +2
    # Day 2: +3 > +2 -> momentum
    # Day 5: +2 > -1 -> momentum
    # Day 6: +4 > +2 -> momentum
    assert find_momentum_days(prices) == [2, 5, 6]


def test_no_momentum():
    """Steady increases but each smaller than previous."""
    prices = [100, 110, 118, 124, 128, 130]
    # Changes: +10, +8, +6, +4, +2 (decreasing)
    assert find_momentum_days(prices) == []


def test_all_momentum():
    """Each day accelerates."""
    prices = [100, 101, 103, 106, 110, 115]
    # Changes: +1, +2, +3, +4, +5 (always bigger)
    assert find_momentum_days(prices) == [2, 3, 4, 5]


def test_single_momentum():
    """Only one momentum day."""
    prices = [100, 105, 108, 110]
    # Changes: +5, +3, +2 (decreasing)
    assert find_momentum_days(prices) == []


def test_momentum_after_drop():
    """Momentum after a price drop."""
    prices = [100, 95, 97, 102]
    # Changes: -5, +2, +5
    # Day 2: +2 > -5 -> momentum
    # Day 3: +5 > +2 -> momentum
    assert find_momentum_days(prices) == [2, 3]


def test_minimum_list():
    """List with only 3 prices."""
    prices = [100, 102, 105]
    # Changes: +2, +3
    # Day 2: +3 > +2 -> momentum
    assert find_momentum_days(prices) == [2]

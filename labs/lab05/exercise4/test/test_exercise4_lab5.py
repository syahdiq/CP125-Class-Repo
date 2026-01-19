import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise4.py')
_spec = importlib.util.spec_from_file_location("exercise4_lab5", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
filter_query_times = _module.filter_query_times

def test_standard_outliers():
    """Standard case with one clear outlier."""
    query_times = [45, 52, 48, 180, 51, 47, 50, 12]
    assert filter_query_times(query_times) == [12, 45, 47, 48, 50, 51, 52]

def test_no_outliers_identical():
    """All values are same. Std dev is 0. No values exceed mean."""
    query_times = [10, 10, 10, 10]
    assert filter_query_times(query_times) == [10, 10, 10, 10]

def test_sorting_preservation():
    """Input is unsorted, output must be sorted."""
    query_times = [100, 50, 150, 75]
    result = filter_query_times(query_times)
    assert result == sorted(result)

def test_high_variance_removal():
    """A very large value should be stripped."""
    query_times = [10, 10, 1000]
    result = filter_query_times(query_times)
    assert 1000 not in result
    assert result == [10, 10]

def test_single_value():
    """Single value list. Mean is value, std dev is 0. Not removed (not > limit)."""
    query_times = [50]
    assert filter_query_times(query_times) == [50]

def test_two_values_boundary():
    """Two values. Higher is exactly mean + std_dev, not removed (must be >)."""
    query_times = [10, 100]
    assert filter_query_times(query_times) == [10, 100]

def test_multiple_outliers_removal():
    """Verify that values significantly above the group are removed."""
    query_times = [10, 11, 12, 100, 110]
    result = filter_query_times(query_times)
    assert 100 not in result
    assert 110 not in result

def test_result_is_sorted():
    """Regardless of filtering, result is always sorted."""
    query_times = [50, 10, 100, 20]
    result = filter_query_times(query_times)
    assert result == sorted(result)

def test_empty_list():
    """Empty list should return empty list."""
    assert filter_query_times([]) == []

def test_large_floats():
    """Handling floating point execution times."""
    query_times = [1.5, 2.3, 1.8, 10.5, 2.1]
    result = filter_query_times(query_times)
    assert 10.5 not in result

def test_near_zero_times():
    """Handling very small numbers (near zero)."""
    query_times = [0.001, 0.002, 0.0015, 0.1, 0.0012]
    result = filter_query_times(query_times)
    assert 0.1 not in result

import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise3.py')
_spec = importlib.util.spec_from_file_location("exercise3_lab5", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
find_bottleneck_index = _module.find_bottleneck_index

def test_standard_bottleneck():
    """Standard case with a clear jump in the middle."""
    traceroute = ((1, 5), (2, 8), (3, 45), (4, 48), (5, 50))
    assert find_bottleneck_index(traceroute) == 1

def test_jump_at_start():
    """Jump occurs between the first and second hop."""
    traceroute = ((1, 10), (2, 100), (3, 110), (4, 120))
    assert find_bottleneck_index(traceroute) == 0

def test_jump_at_end():
    """Jump occurs between the last two hops."""
    traceroute = ((1, 5), (2, 10), (3, 15), (4, 200))
    assert find_bottleneck_index(traceroute) == 2

def test_consistent_latencies():
    """All jumps are the same size. Should return the first one."""
    traceroute = ((1, 10), (2, 12), (3, 14), (4, 16))
    assert find_bottleneck_index(traceroute) == 0

def test_unstable_connection():
    """Multiple large jumps, find the single largest."""
    traceroute = ((1, 10), (2, 30), (3, 40), (4, 90), (5, 100))
    assert find_bottleneck_index(traceroute) == 2

def test_minimum_hops():
    """Minimum valid input: 2 hops."""
    traceroute = ((1, 10), (2, 50))
    assert find_bottleneck_index(traceroute) == 0

def test_decreasing_latency_is_not_bottleneck():
    """
    If logic uses absolute difference (change), a spike down is also a spike.
    Scenario: (10, 100, 10). Jumps are 90 (up) and 90 (down). 
    First largest jump is at 0.
    """
    traceroute = ((1, 10), (2, 100), (3, 10))
    assert find_bottleneck_index(traceroute) == 0

def test_zero_latency_start():
    """Hops starting with 0 latency."""
    traceroute = ((1, 0), (2, 0), (3, 50), (4, 50))
    assert find_bottleneck_index(traceroute) == 1

def test_large_number_handling():
    """Handling very large latency values."""
    traceroute = ((1, 1000), (2, 1005), (3, 5000), (4, 5010))
    assert find_bottleneck_index(traceroute) == 1

def test_identical_latencies():
    """No jumps at all (all jumps are 0)."""
    traceroute = ((1, 50), (2, 50), (3, 50), (4, 50))
    assert find_bottleneck_index(traceroute) == 0

def test_alternating_spikes():
    """Large increase followed by large decrease."""
    traceroute = ((1, 10), (2, 110), (3, 210), (4, 110), (5, 10))
    assert find_bottleneck_index(traceroute) == 0

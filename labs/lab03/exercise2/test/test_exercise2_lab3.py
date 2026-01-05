import pytest
import importlib.util
import os

# Load exercise2.py from the parent directory using absolute path
_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise2.py')
_spec = importlib.util.spec_from_file_location("exercise2_lab3", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
find_station = _module.find_station
count_stops = _module.count_stops

def test_basic_forward():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Marina", "Sentosa") == 3

def test_basic_backward():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Sentosa", "Marina") == 3

def test_same_station():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Marina", "Marina") == 0

def test_adjacent_stations():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Central", "Marina") == 1

def test_first_to_last():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Central", "Sentosa") == 4

def test_start_not_found():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Unknown", "Sentosa") == -1

def test_stop_not_found():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Marina", "Unknown") == -1

def test_both_not_found():
    stations = ["Central", "Marina", "Bukit", "Orchard", "Sentosa"]
    assert count_stops(stations, "Unknown1", "Unknown2") == -1

def test_find_station_exists():
    stations = ["Central", "Marina", "Bukit"]
    assert find_station(stations, "Marina") == 1

def test_find_station_not_exists():
    stations = ["Central", "Marina", "Bukit"]
    assert find_station(stations, "Unknown") is None

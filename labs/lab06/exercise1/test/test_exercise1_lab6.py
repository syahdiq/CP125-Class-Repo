import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise1.py')
_spec = importlib.util.spec_from_file_location("exercise1_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
get_legit_power_users = _module.get_legit_power_users

def test_standard_power_user():
    logs = [("10:01", "u1", "view"), ("10:02", "u2", "view"), ("10:05", "u1", "scroll")]
    bot_ids = {"u9"}
    assert get_legit_power_users(logs, bot_ids, 1) == ["u1"]

def test_bot_filtering():
    logs = [("10:12", "u9", "extract"), ("10:15", "u9", "view")]
    bot_ids = {"u9"}
    assert get_legit_power_users(logs, bot_ids, 0) == []

def test_threshold_boundary():
    # threshold 1 means > 1
    logs = [("10:01", "u1", "view"), ("10:02", "u1", "view")] # 1 unique
    assert get_legit_power_users(logs, set(), 1) == []

def test_sorting_result():
    logs = [("10:01", "z1", "v"), ("10:02", "z1", "s"), ("10:03", "a1", "v"), ("10:04", "a1", "s")]
    assert get_legit_power_users(logs, set(), 1) == ["a1", "z1"]

def test_empty_logs():
    assert get_legit_power_users([], set(), 1) == []

def test_threshold_zero():
    # threshold 0 means > 0
    logs = [("10:01", "u1", "view")]
    assert get_legit_power_users(logs, set(), 0) == ["u1"]

def test_multiple_bots():
    logs = [("10:01", "u1", "v1"), ("10:02", "u1", "v2"), ("10:03", "b1", "v1")]
    bot_ids = {"u1", "b1"}
    assert get_legit_power_users(logs, bot_ids, 0) == []

def test_many_unique_actions():
    logs = [("10:01", "u1", f"act{i}") for i in range(10)]
    assert get_legit_power_users(logs, set(), 5) == ["u1"]

def test_users_below_threshold():
    logs = [("10:01", "u1", "v"), ("10:02", "u2", "v")]
    assert get_legit_power_users(logs, set(), 1) == []

def test_complex_mix():
    logs = [
        ("1", "u1", "v"), ("2", "u1", "s"), # u1: 2 unique (Pass if T=1)
        ("3", "u2", "v"),                   # u2: 1 unique (Fail if T=1)
        ("4", "bot", "v"), ("5", "bot", "s"), ("6", "bot", "x"), # bot: ignore
        ("7", "u3", "v"), ("8", "u3", "s"), ("9", "u3", "x")     # u3: 3 unique (Pass if T=1)
    ]
    bot_ids = {"bot"}
    assert get_legit_power_users(logs, bot_ids, 1) == ["u1", "u3"]

def test_duplicate_actions_dont_count_extra():
    logs = [("10:01", "u1", "view") for _ in range(100)]
    assert get_legit_power_users(logs, set(), 0) == ["u1"]
    assert get_legit_power_users(logs, set(), 1) == []

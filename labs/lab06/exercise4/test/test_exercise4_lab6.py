import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise4.py')
_spec = importlib.util.spec_from_file_location("exercise4_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
synchronize_databases = _module.synchronize_databases

def test_basic_sync():
    legacy = [(1, "a@b.com"), (2, "c@d.com")]
    modern = {1, 3}
    lost, ghost = synchronize_databases(legacy, modern, set())
    assert lost == {2}
    assert ghost == {3}

def test_blacklist_filtering():
    legacy = [(1, "bad@mail.com"), (2, "good@mail.com")]
    lost, ghost = synchronize_databases(legacy, {2}, {"bad@mail.com"})
    assert lost == set()
    assert ghost == set()

def test_empty_inputs():
    assert synchronize_databases([], set(), set()) == (set(), set())

def test_all_blacklisted():
    legacy = [(i, f"b{i}@m.com") for i in range(5)]
    bl = {f"b{i}@m.com" for i in range(5)}
    lost, ghost = synchronize_databases(legacy, {1, 2, 3}, bl)
    # clean legacy is empty. moderno has 1,2,3.
    # lost = {} - {1,2,3} = {}
    # ghost = {1,2,3} - {} = {1,2,3}
    assert lost == set()
    assert ghost == {1, 2, 3}

def test_total_match():
    legacy = [(10, "10@m.com"), (20, "20@m.com")]
    modern = {10, 20}
    assert synchronize_databases(legacy, modern, set()) == (set(), set())

def test_duplicate_legacy_ids():
    # If same ID appears twice with different emails, and one is blacklisted?
    legacy = [(1, "good@m.com"), (1, "bad@m.com")]
    # Result depends on if any instance matches. "1" remains valid because "good@m.com" is ok.
    lost, ghost = synchronize_databases(legacy, set(), {"bad@mail.com"})
    assert lost == {1}

def test_ghost_only():
    assert synchronize_databases([], {1, 2, 3}, set()) == (set(), {1, 2, 3})

def test_lost_only():
    legacy = [(i, f"{i}@m.com") for i in range(5)]
    assert synchronize_databases(legacy, set(), set()) == ({0, 1, 2, 3, 4}, set())

def test_large_dataset():
    legacy = [(i, f"{i}@m.com") for i in range(1000)]
    modern = set(range(500, 1500))
    lost, ghost = synchronize_databases(legacy, modern, set())
    assert len(lost) == 500 # 0 to 499
    assert len(ghost) == 500 # 1000 to 1499

def test_case_sensitive_blacklist():
    legacy = [(1, "USER@m.com")]
    assert synchronize_databases(legacy, {1}, {"user@m.com"}) == (set(), set()) # USER != user

def test_return_type():
    res = synchronize_databases([], set(), set())
    assert isinstance(res, tuple)
    assert len(res) == 2
    assert isinstance(res[0], set)
    assert isinstance(res[1], set)

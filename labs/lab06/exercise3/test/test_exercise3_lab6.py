import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise3.py')
_spec = importlib.util.spec_from_file_location("exercise3_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
audit_blocklists = _module.audit_blocklists

def test_standard_categories():
    a, b, c = {"m", "v"}, {"v", "ad"}, {"v", "sp"}
    uni, red, uoa = audit_blocklists(a, b, c)
    assert uni == {"v"}
    assert red == {"v"}
    assert uoa == {"m"}

def test_redundant_logic():
    # Item in A&B, but not C
    a, b, c = {"shared"}, {"shared"}, set()
    uni, red, uoa = audit_blocklists(a, b, c)
    assert uni == set()
    assert red == {"shared"}
    assert uoa == set()

def test_redundant_all_pairs():
    # Case: x in AB, y in BC, z in AC
    a, b, c = {"x", "z"}, {"x", "y"}, {"y", "z"}
    uni, red, uoa = audit_blocklists(a, b, c)
    assert uni == set()
    assert red == {"x", "y", "z"}

def test_unique_a_isolation():
    a, b, c = {"u1", "u2"}, {"x"}, {"y"}
    uni, red, uoa = audit_blocklists(a, b, c)
    assert uoa == {"u1", "u2"}

def test_empty_lists():
    res = audit_blocklists(set(), set(), set())
    assert res == (set(), set(), set())

def test_all_identical():
    a = {"v1", "v2"}
    res = audit_blocklists(a, a, a)
    assert res == (a, a, set())

def test_one_empty_set():
    a, b, c = {"x"}, {"x"}, set()
    uni, red, uoa = audit_blocklists(a, b, c)
    assert uni == set()
    assert red == {"x"}
    assert uoa == set()

def test_unique_a_subset_of_others():
    a, b, c = {"x"}, {"x", "y"}, {"x", "z"}
    uni, red, uoa = audit_blocklists(a, b, c)
    assert uoa == set()
    assert uni == {"x"}

def test_large_sets():
    a = {f"u{i}" for i in range(100)}
    b = {f"u{i}" for i in range(50, 150)}
    c = {f"u{i}" for i in range(75, 175)}
    uni, red, uoa = audit_blocklists(a, b, c)
    assert len(uni) == 25 # 75 to 99
    assert len(uoa) == 50 # 0 to 49

def test_disjoint_sets():
    a, b, c = {"a"}, {"b"}, {"c"}
    uni, red, uoa = audit_blocklists(a, b, c)
    assert uni == set()
    assert red == set()
    assert uoa == {"a"}

def test_return_type():
    res = audit_blocklists(set(), set(), set())
    assert isinstance(res, tuple)
    assert len(res) == 3
    for s in res: assert isinstance(s, set)

import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise5.py')
_spec = importlib.util.spec_from_file_location("exercise5_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
audit_zero_trust = _module.audit_zero_trust

def test_standard_audit():
    baseline = {("u1", "1.1"), ("u2", "1.5")}
    logs = [("u1", "1.1"), ("u3", "9.9")]
    auth, alerts, inactive = audit_zero_trust(baseline, logs)
    assert auth == {("u1", "1.1")}
    assert alerts == {("u3", "9.9")}
    assert inactive == {("u2", "1.5")}

def test_empty_logs():
    baseline = {("a", "b")}
    auth, alerts, inactive = audit_zero_trust(baseline, [])
    assert auth == set()
    assert alerts == set()
    assert inactive == {("a", "b")}

def test_empty_baseline():
    logs = [("u", "p")]
    auth, alerts, inactive = audit_zero_trust(set(), logs)
    assert auth == set()
    assert alerts == {("u", "p")}
    assert inactive == set()

def test_total_success():
    b = {("u", "p")}
    assert audit_zero_trust(b, [("u", "p")]) == (b, set(), set())

def test_multiple_ips_one_user():
    baseline = {("u1", "ip1")}
    logs = [("u1", "ip1"), ("u1", "ip2")]
    auth, alerts, inactive = audit_zero_trust(baseline, logs)
    assert alerts == {("u1", "ip2")}

def test_duplicate_log_entries():
    baseline = {("u", "p")}
    logs = [("u", "p"), ("u", "p")]
    auth, alerts, inactive = audit_zero_trust(baseline, logs)
    assert auth == {("u", "p")}
    assert alerts == set()

def test_large_baseline():
    baseline = {(f"u{i}", "ip") for i in range(100)}
    logs = [(f"u{i}", "ip") for i in range(50, 150)]
    auth, alert, inact = audit_zero_trust(baseline, logs)
    assert len(auth) == 50
    assert len(alert) == 50
    assert len(inact) == 50

def test_complex_intrusion():
    baseline = {("admin", "127.0.0.1"), ("boss", "10.0.0.1")}
    logs = [("boss", "10.0.0.1"), ("hacker", "192.168.1.100")]
    auth, alert, inact = audit_zero_trust(baseline, logs)
    assert alert == {("hacker", "192.168.1.100")}
    assert inact == {("admin", "127.0.0.1")}

def test_mixed_tuple_order():
    # Tuples are ordered. ("a", "b") != ("b", "a")
    baseline = {("user", "10.0.0.1")}
    logs = [("10.0.0.1", "user")]
    auth, alert, inact = audit_zero_trust(baseline, logs)
    assert auth == set()
    assert alert == {("10.0.0.1", "user")}

def test_all_empty():
    assert audit_zero_trust(set(), []) == (set(), set(), set())

def test_return_types():
    res = audit_zero_trust(set(), [])
    assert isinstance(res, tuple)
    assert len(res) == 3
    for s in res: assert isinstance(s, set)

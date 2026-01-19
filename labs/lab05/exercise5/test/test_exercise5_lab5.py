import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise5.py')
_spec = importlib.util.spec_from_file_location("exercise5_lab5", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
clean_sessions = _module.clean_sessions

def test_standard_cleaning():
    """Basic removal of sessions from a dead server."""
    pool = ("srv-A", "srv-B", "srv-C", "srv-D")
    sessions = [("srv-B", "cli-1"), ("srv-A", "cli-2"), ("srv-B", "cli-3")]
    dead = ["srv-B"]
    assert clean_sessions(pool, sessions, dead) == [("srv-A", "cli-2")]

def test_unregistered_dead_server():
    """Dead server list contains a server not in the master pool (should be ignored)."""
    pool = ("srv-A", "srv-B")
    sessions = [("srv-A", "cli-1"), ("srv-B", "cli-2")]
    dead = ["srv-X"] # Not in pool
    assert clean_sessions(pool, sessions, dead) == [("srv-A", "cli-1"), ("srv-B", "cli-2")]

def test_sorting_output():
    """The result must be sorted by server ID."""
    pool = ("A", "B", "C")
    sessions = [("C", "1"), ("A", "1"), ("B", "1")]
    dead = []
    assert clean_sessions(pool, sessions, dead) == [("A", "1"), ("B", "1"), ("C", "1")]

def test_all_servers_dead():
    """All registered servers are dead, resulting in empty sessions."""
    pool = ("A", "B")
    sessions = [("A", "1"), ("B", "2"), ("A", "3")]
    dead = ["A", "B"]
    assert clean_sessions(pool, sessions, dead) == []

def test_no_dead_servers():
    """Empty dead list, sessions remain intact (but sorted)."""
    pool = ("srv-1", "srv-2")
    sessions = [("srv-2", "c1"), ("srv-1", "c2")]
    dead = []
    assert clean_sessions(pool, sessions, dead) == [("srv-1", "c2"), ("srv-2", "c1")]

def test_empty_sessions():
    """No active sessions to begin with."""
    pool = ("srv-A",)
    sessions = []
    dead = ["srv-A"]
    assert clean_sessions(pool, sessions, dead) == []

def test_duplicate_sessions_removal():
    """Remove multiple sessions for the same server-client pair."""
    pool = ("srv-A", "srv-B")
    sessions = [("srv-B", "cli-1"), ("srv-B", "cli-1")]
    dead = ["srv-B"]
    assert clean_sessions(pool, sessions, dead) == []

def test_dead_list_with_duplicates():
    """Dead servers list has duplicates, should still work correctly."""
    pool = ("srv-A", "srv-B")
    sessions = [("srv-A", "cli-1"), ("srv-B", "cli-2")]
    dead = ["srv-A", "srv-A", "srv-A"]
    assert clean_sessions(pool, sessions, dead) == [("srv-B", "cli-2")]

def test_case_sensitivity():
    """Server IDs are case-sensitive."""
    pool = ("SRV-A", "srv-a")
    sessions = [("SRV-A", "c1"), ("srv-a", "c2")]
    dead = ["SRV-A"]
    assert clean_sessions(pool, sessions, dead) == [("srv-a", "c2")]

def test_partial_registration():
    """Dead list has one valid and one invalid server."""
    pool = ("srv-A", "srv-B")
    sessions = [("srv-A", "c1"), ("srv-B", "c2")]
    dead = ["srv-A", "srv-Unknown"]
    assert clean_sessions(pool, sessions, dead) == [("srv-B", "c2")]



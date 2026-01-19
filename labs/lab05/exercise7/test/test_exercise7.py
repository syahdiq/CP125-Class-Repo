import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from exercise7 import find_conflicting_ports


def test_basic_conflicts():
    rules = [
        (1, 80, "ALLOW"), 
        (2, 443, "ALLOW"), 
        (3, 80, "BLOCK"),
        (4, 22, "BLOCK"), 
        (5, 443, "BLOCK"), 
        (6, 8080, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == [(80, 3), (443, 5)]


def test_no_conflicts():
    rules = [
        (1, 80, "ALLOW"), 
        (2, 80, "ALLOW"), 
        (3, 443, "BLOCK")
    ]
    assert find_conflicting_ports(rules) == []


def test_single_port_conflict():
    rules = [
        (1, 80, "ALLOW"),
        (2, 80, "BLOCK"),
        (3, 443, "ALLOW"),
        (4, 443, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == [(80, 2)]


def test_multiple_same_action():
    rules = [
        (1, 80, "ALLOW"),
        (2, 80, "ALLOW"),
        (3, 80, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == []


def test_first_conflict_rule():
    rules = [
        (1, 80, "ALLOW"),
        (2, 80, "BLOCK"),
        (3, 80, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == [(80, 2)]


def test_multiple_ports_sorted():
    rules = [
        (1, 443, "ALLOW"),
        (2, 22, "ALLOW"),
        (3, 80, "ALLOW"),
        (4, 443, "BLOCK"),
        (5, 22, "BLOCK"),
        (6, 80, "BLOCK")
    ]
    assert find_conflicting_ports(rules) == [(22, 5), (80, 6), (443, 4)]


def test_block_then_allow():
    rules = [
        (1, 80, "BLOCK"),
        (2, 80, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == [(80, 2)]


def test_three_ports_mixed():
    rules = [
        (1, 80, "ALLOW"),
        (2, 443, "BLOCK"),
        (3, 22, "ALLOW"),
        (4, 80, "BLOCK"),
        (5, 22, "BLOCK")
    ]
    assert find_conflicting_ports(rules) == [(22, 5), (80, 4)]


def test_allow_block_allow_pattern():
    rules = [
        (1, 80, "ALLOW"),
        (2, 443, "BLOCK"),
        (3, 80, "BLOCK"),
        (4, 443, "ALLOW")
    ]
    assert find_conflicting_ports(rules) == [(80, 3), (443, 4)]


def test_four_rules_one_port():
    rules = [
        (1, 80, "ALLOW"),
        (2, 80, "ALLOW"),
        (3, 80, "BLOCK"),
        (4, 80, "BLOCK")
    ]
    assert find_conflicting_ports(rules) == [(80, 3)]

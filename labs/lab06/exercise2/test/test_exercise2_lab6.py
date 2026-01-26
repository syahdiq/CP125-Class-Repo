import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise2.py')
_spec = importlib.util.spec_from_file_location("exercise2_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
match_specialists = _module.match_specialists

def test_standard_match():
    candidates = [
        ("Ali", {"Python", "Git"}), 
        ("Sara", {"Git", "Cloud", "COBOL"}), 
        ("Zaki", {"Git", "Cloud"})
    ]
    reqs = {"Git"} # Rare: Python(1), Cloud(2), COBOL(1)
    result = match_specialists(candidates, reqs)
    names = [r[0] for r in result]
    assert sorted(names) == ["Ali", "Sara", "Zaki"]

def test_rarity_logic():
    # Git(3)-Not Rare, COBOL(1)-Rare
    candidates = [("A", {"Git", "COBOL"}), ("B", {"Git"}), ("C", {"Git"})]
    reqs = {"Git"}
    result = match_specialists(candidates, reqs)
    assert len(result) == 1
    assert result[0] == ("A", {"COBOL"})

def test_missing_requirements():
    candidates = [("Ali", {"Python"})]
    reqs = {"Git"}
    assert match_specialists(candidates, reqs) == []

def test_no_rare_skills():
    # All skills held by 3 people
    candidates = [("A", {"G"}), ("B", {"G"}), ("C", {"G"})]
    reqs = {"G"}
    assert match_specialists(candidates, reqs) == []

def test_empty_candidates():
    assert match_specialists([], {"Git"}) == []

def test_empty_requirements():
    # If reqs empty, superset is always True. Any candidate with a rare skill wins.
    candidates = [("A", {"Rare"})] + [("B", {"Common"})] * 5
    # Rare skill count: 1 (< 3). Common skill count: 5.
    result = match_specialists(candidates, set())
    assert result == [("A", {"Rare"})]

def test_exact_rarity_threshold():
    # Skill held by exactly 2 people (Rare)
    candidates = [("A", {"R"}), ("B", {"R"})] + [("C", {"X"})] * 10
    # R: 2 (Rare), X: 10 (Not Rare)
    assert match_specialists(candidates, set()) == [("A", {"R"}), ("B", {"R"})]

def test_rarity_limit_three():
    # Skill held by exactly 3 people (NOT Rare)
    candidates = [("A", {"S"}), ("B", {"S"}), ("C", {"S"})]
    assert match_specialists(candidates, set()) == []

def test_candidate_with_only_requirements():
    # Needs requirement AND a rare skill
    candidates = [("A", {"Git"}) for _ in range(10)]
    assert match_specialists(candidates, {"Git"}) == []

def test_multiple_rare_skills():
    candidates = [("A", {"G", "R1", "R2"}), ("B", {"G"}), ("C", {"G"})]
    # G:3, R1:1, R2:1
    result = match_specialists(candidates, {"G"})
    assert result == [("A", {"R1", "R2"})]

def test_large_dataset_logic():
    # 100 people have "Common", 2 have "Unicorn"
    candidates = [("P"+str(i), {"Common"}) for i in range(100)]
    candidates.extend([("U1", {"Common", "Unicorn"}), ("U2", {"Common", "Unicorn"})])
    result = match_specialists(candidates, {"Common"})
    assert len(result) == 2
    assert result[0][1] == {"Unicorn"}

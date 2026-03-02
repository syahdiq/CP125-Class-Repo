import pytest
import importlib.util
import os
import tempfile
import shutil

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise1.py')
_spec = importlib.util.spec_from_file_location("exercise1_lab8", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
filter_passing_scores = _module.filter_passing_scores


def create_test_file(content):
    """Helper to create temporary test file"""
    temp_dir = tempfile.mkdtemp()
    input_file = os.path.join(temp_dir, "scores.txt")
    output_file = os.path.join(temp_dir, "passing.txt")

    with open(input_file, "w") as f:
        f.write(content)

    return temp_dir, input_file, output_file


def test_basic_filtering():
    """Test basic filtering of passing scores"""
    temp_dir, input_file, output_file = create_test_file("S001 85\nS002 75\nS003 90\n")
    result = filter_passing_scores(input_file, output_file)

    assert result == 2

    with open(output_file, "r") as f:
        lines = f.readlines()
    assert len(lines) == 2
    assert "S001 85" in lines[0]
    assert "S003 90" in lines[1]

    shutil.rmtree(temp_dir)


def test_all_passing():
    """Test when all students pass"""
    temp_dir, input_file, output_file = create_test_file("S001 85\nS002 90\nS003 95\n")
    result = filter_passing_scores(input_file, output_file)

    assert result == 3

    shutil.rmtree(temp_dir)


def test_none_passing():
    """Test when no students pass"""
    temp_dir, input_file, output_file = create_test_file("S001 75\nS002 70\nS003 65\n")
    result = filter_passing_scores(input_file, output_file)

    assert result == 0

    with open(output_file, "r") as f:
        lines = f.readlines()
    assert len(lines) == 0

    shutil.rmtree(temp_dir)


def test_exactly_80():
    """Test boundary case with score exactly 80"""
    temp_dir, input_file, output_file = create_test_file("S001 80\nS002 79\n")
    result = filter_passing_scores(input_file, output_file)

    assert result == 1

    with open(output_file, "r") as f:
        content = f.read()
    assert "S001 80" in content
    assert "S002" not in content

    shutil.rmtree(temp_dir)


def test_single_student_passing():
    """Test with single passing student"""
    temp_dir, input_file, output_file = create_test_file("S001 95\n")
    result = filter_passing_scores(input_file, output_file)

    assert result == 1

    shutil.rmtree(temp_dir)


def test_single_student_failing():
    """Test with single failing student"""
    temp_dir, input_file, output_file = create_test_file("S001 70\n")
    result = filter_passing_scores(input_file, output_file)

    assert result == 0

    shutil.rmtree(temp_dir)


def test_large_dataset():
    """Test with larger dataset"""
    content = "\n".join([f"S{i:03d} {60 + i % 40}" for i in range(1, 51)])
    temp_dir, input_file, output_file = create_test_file(content)
    result = filter_passing_scores(input_file, output_file)

    # Scores range from 61-99, so scores >= 80 are 80-99 (20 scores)
    assert result == 20

    shutil.rmtree(temp_dir)


def test_perfect_scores():
    """Test with perfect scores"""
    temp_dir, input_file, output_file = create_test_file("S001 100\nS002 100\nS003 100\n")
    result = filter_passing_scores(input_file, output_file)

    assert result == 3

    shutil.rmtree(temp_dir)


def test_mixed_scores():
    """Test with mixed passing and failing scores"""
    temp_dir, input_file, output_file = create_test_file("S001 95\nS002 45\nS003 82\nS004 76\nS005 88\n")
    result = filter_passing_scores(input_file, output_file)

    assert result == 3

    with open(output_file, "r") as f:
        content = f.read()
    assert "S001" in content
    assert "S003" in content
    assert "S005" in content
    assert "S002" not in content
    assert "S004" not in content

    shutil.rmtree(temp_dir)


def test_output_format():
    """Test that output has correct format"""
    temp_dir, input_file, output_file = create_test_file("S001 85\nS002 90\n")
    result = filter_passing_scores(input_file, output_file)

    with open(output_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        assert len(parts) == 2
        assert parts[0].startswith("S")
        int(parts[1])  # Should be convertible to int

    shutil.rmtree(temp_dir)


def test_actual_data_files():
    """Test with actual data files to verify output directory"""
    exercise_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(exercise_dir, "data", "scores.txt")
    output_file = os.path.join(exercise_dir, "data", "passing.txt")

    # Run the function
    result = filter_passing_scores(input_file, output_file)

    # Verify output file was created in correct location
    assert os.path.exists(output_file), "Output file should be created in data/ directory"
    assert result >= 0, "Should return a valid count"

    # Clean up the output file
    if os.path.exists(output_file):
        os.remove(output_file)

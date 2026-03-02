import pytest
import importlib.util
import os
import tempfile
import shutil

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise2.py')
_spec = importlib.util.spec_from_file_location("exercise2_lab8", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
merge_lists = _module.merge_lists


def create_test_files(content1, content2):
    """Helper to create temporary test files"""
    temp_dir = tempfile.mkdtemp()
    file1 = os.path.join(temp_dir, "list1.txt")
    file2 = os.path.join(temp_dir, "list2.txt")
    output_file = os.path.join(temp_dir, "merged.txt")

    with open(file1, "w") as f:
        f.write(content1)
    with open(file2, "w") as f:
        f.write(content2)

    return temp_dir, file1, file2, output_file


def test_basic_merge():
    """Test basic merging of two lists"""
    temp_dir, file1, file2, output_file = create_test_files("Alice\nBob\n", "Charlie\nDavid\n")
    result = merge_lists(file1, file2, output_file)

    assert result == 4

    with open(output_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    assert lines == ["Alice", "Bob", "Charlie", "David"]

    shutil.rmtree(temp_dir)


def test_with_duplicates():
    """Test removing duplicates from both files"""
    temp_dir, file1, file2, output_file = create_test_files("Alice\nBob\nAlice\n", "Bob\nDavid\n")
    result = merge_lists(file1, file2, output_file)

    assert result == 3

    with open(output_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    assert lines == ["Alice", "Bob", "David"]

    shutil.rmtree(temp_dir)


def test_alphabetical_sorting():
    """Test that output is sorted alphabetically"""
    temp_dir, file1, file2, output_file = create_test_files("Zoe\nAlice\n", "Bob\nYvonne\n")
    result = merge_lists(file1, file2, output_file)

    with open(output_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    assert lines == ["Alice", "Bob", "Yvonne", "Zoe"]

    shutil.rmtree(temp_dir)


def test_empty_file1():
    """Test when first file is empty"""
    temp_dir, file1, file2, output_file = create_test_files("", "Alice\nBob\n")
    result = merge_lists(file1, file2, output_file)

    assert result == 2

    shutil.rmtree(temp_dir)


def test_empty_file2():
    """Test when second file is empty"""
    temp_dir, file1, file2, output_file = create_test_files("Alice\nBob\n", "")
    result = merge_lists(file1, file2, output_file)

    assert result == 2

    shutil.rmtree(temp_dir)


def test_identical_files():
    """Test when both files have same content"""
    temp_dir, file1, file2, output_file = create_test_files("Alice\nBob\n", "Alice\nBob\n")
    result = merge_lists(file1, file2, output_file)

    assert result == 2

    with open(output_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    assert lines == ["Alice", "Bob"]

    shutil.rmtree(temp_dir)


def test_single_names():
    """Test with single name in each file"""
    temp_dir, file1, file2, output_file = create_test_files("Alice\n", "Bob\n")
    result = merge_lists(file1, file2, output_file)

    assert result == 2

    shutil.rmtree(temp_dir)


def test_large_dataset():
    """Test with larger dataset"""
    names1 = "\n".join([f"Name{i}" for i in range(1, 26)])
    names2 = "\n".join([f"Name{i}" for i in range(20, 51)])

    temp_dir, file1, file2, output_file = create_test_files(names1, names2)
    result = merge_lists(file1, file2, output_file)

    assert result == 50

    shutil.rmtree(temp_dir)


def test_case_sensitivity():
    """Test that names are case-sensitive"""
    temp_dir, file1, file2, output_file = create_test_files("alice\nALICE\n", "Alice\n")
    result = merge_lists(file1, file2, output_file)

    assert result == 3

    shutil.rmtree(temp_dir)


def test_output_format():
    """Test that output has correct format (one name per line)"""
    temp_dir, file1, file2, output_file = create_test_files("Alice\nBob\n", "Charlie\n")
    result = merge_lists(file1, file2, output_file)

    with open(output_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        assert line.strip() != ""
        assert len(line.strip().split()) == 1

    shutil.rmtree(temp_dir)


def test_actual_data_files():
    """Test with actual data files to verify output directory"""
    exercise_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file1 = os.path.join(exercise_dir, "data", "list1.txt")
    file2 = os.path.join(exercise_dir, "data", "list2.txt")
    output_file = os.path.join(exercise_dir, "data", "merged.txt")

    # Run the function
    result = merge_lists(file1, file2, output_file)

    # Verify output file was created in correct location
    assert os.path.exists(output_file), "Output file should be created in data/ directory"
    assert result >= 0, "Should return a valid count"

    # Clean up the output file
    if os.path.exists(output_file):
        os.remove(output_file)

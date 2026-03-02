import pytest
import importlib.util
import os
import tempfile
import shutil
import csv

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise4.py')
_spec = importlib.util.spec_from_file_location("exercise4_lab8", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
calculate_final_grades = _module.calculate_final_grades


def create_test_file(content):
    """Helper to create temporary test file"""
    temp_dir = tempfile.mkdtemp()
    input_file = os.path.join(temp_dir, "scores.csv")
    output_file = os.path.join(temp_dir, "grades.csv")

    with open(input_file, "w") as f:
        f.write(content)

    return temp_dir, input_file, output_file


def test_basic_grade_calculation():
    """Test basic final grade calculation"""
    content = "student_id,midterm,final\nS001,80,90\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = calculate_final_grades(input_file, output_file)
    
    # 80*0.4 + 90*0.6 = 32 + 54 = 86
    assert abs(result - 86.0) < 0.01
    
    shutil.rmtree(temp_dir)


def test_weighted_formula():
    """Test that weighted formula (40% midterm, 60% final) is correct"""
    content = "student_id,midterm,final\nS001,100,50\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = calculate_final_grades(input_file, output_file)
    
    # 100*0.4 + 50*0.6 = 40 + 30 = 70
    assert abs(result - 70.0) < 0.01
    
    shutil.rmtree(temp_dir)


def test_multiple_students():
    """Test average calculation with multiple students"""
    content = "student_id,midterm,final\nS001,80,90\nS002,90,80\nS003,70,70\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = calculate_final_grades(input_file, output_file)
    
    # S001: 86, S002: 84, S003: 70
    # Average: (86 + 84 + 70) / 3 = 80
    assert abs(result - 80.0) < 0.01
    
    shutil.rmtree(temp_dir)


def test_output_csv_format():
    """Test that output CSV has correct format"""
    content = "student_id,midterm,final\nS001,80,90\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = calculate_final_grades(input_file, output_file)
    
    with open(output_file, "r", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    assert len(rows) == 2  # header + 1 student
    assert rows[0] == ["student_id", "final_grade"]
    assert rows[1][0] == "S001"
    assert rows[1][1] == "86.00"
    
    shutil.rmtree(temp_dir)


def test_single_student():
    """Test with single student"""
    content = "student_id,midterm,final\nS001,75,85\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = calculate_final_grades(input_file, output_file)
    
    # 75*0.4 + 85*0.6 = 30 + 51 = 81
    assert abs(result - 81.0) < 0.01
    
    shutil.rmtree(temp_dir)


def test_perfect_scores():
    """Test with perfect scores"""
    content = "student_id,midterm,final\nS001,100,100\nS002,100,100\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = calculate_final_grades(input_file, output_file)
    
    assert abs(result - 100.0) < 0.01
    
    shutil.rmtree(temp_dir)


def test_low_scores():
    """Test with low scores"""
    content = "student_id,midterm,final\nS001,50,60\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = calculate_final_grades(input_file, output_file)
    
    # 50*0.4 + 60*0.6 = 20 + 36 = 56
    assert abs(result - 56.0) < 0.01
    
    shutil.rmtree(temp_dir)


def test_output_precision():
    """Test that output grades are formatted to 2 decimal places"""
    content = "student_id,midterm,final\nS001,85,90\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = calculate_final_grades(input_file, output_file)
    
    with open(output_file, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        row = next(reader)
    
    assert "." in row[1]
    decimal_part = row[1].split(".")[1]
    assert len(decimal_part) == 2
    
    shutil.rmtree(temp_dir)


def test_large_class():
    """Test with larger number of students"""
    lines = ["student_id,midterm,final\n"]
    for i in range(1, 11):
        lines.append(f"S{i:03d},{70 + i},{80 + i}\n")
    content = "".join(lines)
    
    temp_dir, input_file, output_file = create_test_file(content)
    result = calculate_final_grades(input_file, output_file)
    
    assert result > 0
    assert result <= 100
    
    shutil.rmtree(temp_dir)


def test_calculation_accuracy():
    """Test calculation accuracy with decimal values"""
    content = "student_id,midterm,final\nS001,77.5,82.3\nS002,88.2,91.7\n"
    temp_dir, input_file, output_file = create_test_file(content)

    result = calculate_final_grades(input_file, output_file)

    # S001: 77.5*0.4 + 82.3*0.6 = 31.0 + 49.38 = 80.38
    # S002: 88.2*0.4 + 91.7*0.6 = 35.28 + 55.02 = 90.30
    # Average: (80.38 + 90.30) / 2 = 85.34
    assert abs(result - 85.34) < 0.01

    shutil.rmtree(temp_dir)


def test_actual_data_files():
    """Test with actual data files to verify output directory"""
    exercise_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(exercise_dir, "data", "scores.csv")
    output_file = os.path.join(exercise_dir, "data", "grades.csv")

    # Run the function
    result = calculate_final_grades(input_file, output_file)

    # Verify output file was created in correct location
    assert os.path.exists(output_file), "Output file should be created in data/ directory"
    assert result >= 0, "Should return a valid average"

    # Clean up the output file
    if os.path.exists(output_file):
        os.remove(output_file)

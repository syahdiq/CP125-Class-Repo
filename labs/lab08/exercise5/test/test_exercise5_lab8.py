import pytest
import importlib.util
import os
import tempfile
import shutil

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise5.py')
_spec = importlib.util.spec_from_file_location("exercise5_lab8", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
summarize_sales = _module.summarize_sales


def create_test_file(content):
    """Helper to create temporary test file"""
    temp_dir = tempfile.mkdtemp()
    input_file = os.path.join(temp_dir, "sales.csv")
    output_file = os.path.join(temp_dir, "summary.txt")

    with open(input_file, "w") as f:
        f.write(content)

    return temp_dir, input_file, output_file


def test_basic_summary():
    """Test basic sales summary calculation"""
    content = "product,quantity,price\nLaptop,5,1200.00\nMouse,20,25.00\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = summarize_sales(input_file, output_file)
    
    assert len(result) == 4
    assert result[0] == 6500.00  # total
    assert result[1] == 3250.00  # average
    assert result[2] == 6000.00  # highest (Laptop)
    assert result[3] == 500.00   # lowest (Mouse)
    
    shutil.rmtree(temp_dir)


def test_return_tuple():
    """Test that function returns tuple of 4 values"""
    content = "product,quantity,price\nA,1,100\nB,2,200\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = summarize_sales(input_file, output_file)
    
    assert isinstance(result, tuple)
    assert len(result) == 4
    
    shutil.rmtree(temp_dir)


def test_file_output_format():
    """Test that output file has correct format with all 4 statistics"""
    content = "product,quantity,price\nItem,10,50.00\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = summarize_sales(input_file, output_file)
    
    with open(output_file, "r") as f:
        lines = f.readlines()
    
    assert len(lines) >= 4
    assert "Total Revenue:" in lines[0]
    assert "Average Revenue:" in lines[1]
    assert "Highest Revenue:" in lines[2]
    assert "Lowest Revenue:" in lines[3]
    
    shutil.rmtree(temp_dir)


def test_single_product():
    """Test with single product"""
    content = "product,quantity,price\nLaptop,5,1000.00\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = summarize_sales(input_file, output_file)
    
    assert result[0] == 5000.00  # total
    assert result[1] == 5000.00  # average (same as total for 1 item)
    assert result[2] == 5000.00  # highest
    assert result[3] == 5000.00  # lowest
    
    shutil.rmtree(temp_dir)


def test_multiple_products():
    """Test with multiple products"""
    content = "product,quantity,price\nA,10,100\nB,5,200\nC,20,50\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = summarize_sales(input_file, output_file)
    
    # A: 1000, B: 1000, C: 1000
    assert result[0] == 3000.00  # total
    assert result[1] == 1000.00  # average
    assert result[2] == 1000.00  # highest
    assert result[3] == 1000.00  # lowest
    
    shutil.rmtree(temp_dir)


def test_different_revenues():
    """Test with varying revenue amounts"""
    content = "product,quantity,price\nSmall,1,10\nMedium,5,100\nLarge,10,1000\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = summarize_sales(input_file, output_file)
    
    # Small: 10, Medium: 500, Large: 10000
    assert result[0] == 10510.00  # total
    assert abs(result[1] - 3503.33) < 0.01  # average
    assert result[2] == 10000.00  # highest (Large)
    assert result[3] == 10.00     # lowest (Small)
    
    shutil.rmtree(temp_dir)


def test_large_dataset():
    """Test with larger dataset"""
    products = ["product,quantity,price\n"]
    for i in range(1, 11):
        products.append(f"Product{i},{i},{i * 10}.00\n")
    content = "".join(products)
    
    temp_dir, input_file, output_file = create_test_file(content)
    result = summarize_sales(input_file, output_file)
    
    assert result[0] > 0  # total exists
    assert result[1] > 0  # average exists
    assert result[2] >= result[3]  # highest >= lowest
    
    shutil.rmtree(temp_dir)


def test_decimal_values():
    """Test with decimal price values"""
    content = "product,quantity,price\nA,3,25.50\nB,2,15.75\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = summarize_sales(input_file, output_file)
    
    assert result[0] == 108.00   # 76.50 + 31.50
    assert result[1] == 54.00    # average
    assert result[2] == 76.50    # highest
    assert result[3] == 31.50    # lowest
    
    shutil.rmtree(temp_dir)


def test_calculations_accuracy():
    """Test that calculations are accurate"""
    content = "product,quantity,price\nX,7,13.25\nY,4,22.50\n"
    temp_dir, input_file, output_file = create_test_file(content)
    
    result = summarize_sales(input_file, output_file)
    
    # X: 92.75, Y: 90.00
    assert abs(result[0] - 182.75) < 0.01  # total
    assert abs(result[1] - 91.375) < 0.01  # average
    assert abs(result[2] - 92.75) < 0.01   # highest
    assert abs(result[3] - 90.00) < 0.01   # lowest
    
    shutil.rmtree(temp_dir)


def test_output_values_match():
    """Test that file output matches returned values"""
    content = "product,quantity,price\nTest,5,100.00\n"
    temp_dir, input_file, output_file = create_test_file(content)

    result = summarize_sales(input_file, output_file)

    with open(output_file, "r") as f:
        content = f.read()

    # Check that returned values appear in file
    assert f"${result[0]:.2f}" in content  # total
    assert f"${result[1]:.2f}" in content  # average
    assert f"${result[2]:.2f}" in content  # highest
    assert f"${result[3]:.2f}" in content  # lowest

    shutil.rmtree(temp_dir)


def test_actual_data_files():
    """Test with actual data files to verify output directory"""
    exercise_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    input_file = os.path.join(exercise_dir, "data", "sales.csv")
    output_file = os.path.join(exercise_dir, "data", "summary.txt")

    # Run the function
    result = summarize_sales(input_file, output_file)

    # Verify output file was created in correct location
    assert os.path.exists(output_file), "Output file should be created in data/ directory"
    assert len(result) == 4, "Should return tuple of 4 values"

    # Clean up the output file
    if os.path.exists(output_file):
        os.remove(output_file)

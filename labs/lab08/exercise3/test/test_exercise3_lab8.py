import pytest
import importlib.util
import os
import tempfile
import shutil
import csv

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise3.py')
_spec = importlib.util.spec_from_file_location("exercise3_lab8", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
calculate_order_total = _module.calculate_order_total


def create_test_files(products_content, order_content):
    """Helper to create temporary test files"""
    temp_dir = tempfile.mkdtemp()
    products_file = os.path.join(temp_dir, "products.csv")
    order_file = os.path.join(temp_dir, "order.csv")
    output_file = os.path.join(temp_dir, "total.csv")

    with open(products_file, "w") as f:
        f.write(products_content)
    with open(order_file, "w") as f:
        f.write(order_content)

    return temp_dir, products_file, order_file, output_file


def test_basic_order():
    """Test basic order total calculation"""
    products = "product_id,product_name,price\nP001,Laptop,1000.00\nP002,Mouse,25.00\n"
    order = "product_id,quantity\nP001,2\nP002,4\n"
    
    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)
    
    assert result == 2100.00  # 2*1000 + 4*25
    
    shutil.rmtree(temp_dir)


def test_single_item():
    """Test with single item order"""
    products = "product_id,product_name,price\nP001,Item,100.00\n"
    order = "product_id,quantity\nP001,5\n"
    
    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)
    
    assert result == 500.00
    
    shutil.rmtree(temp_dir)


def test_output_csv_format():
    """Test that output CSV has correct format"""
    products = "product_id,product_name,price\nP001,Test,50.00\n"
    order = "product_id,quantity\nP001,2\n"
    
    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)
    
    with open(output_file, "r", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    assert len(rows) == 2  # header + 1 data row
    assert rows[0] == ["product_id", "total_cost"]
    assert rows[1][0] == "P001"
    assert rows[1][1] == "100.00"
    
    shutil.rmtree(temp_dir)


def test_multiple_products():
    """Test with multiple products in order"""
    products = "product_id,product_name,price\nP001,A,10\nP002,B,20\nP003,C,30\n"
    order = "product_id,quantity\nP001,5\nP002,3\nP003,2\n"
    
    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)
    
    assert result == 170.00  # 50 + 60 + 60
    
    shutil.rmtree(temp_dir)


def test_decimal_prices():
    """Test with decimal price values"""
    products = "product_id,product_name,price\nP001,Item,12.50\n"
    order = "product_id,quantity\nP001,7\n"
    
    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)
    
    assert abs(result - 87.50) < 0.01
    
    shutil.rmtree(temp_dir)


def test_large_order():
    """Test with large quantities"""
    products = "product_id,product_name,price\nP001,Widget,5.00\n"
    order = "product_id,quantity\nP001,1000\n"
    
    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)
    
    assert result == 5000.00
    
    shutil.rmtree(temp_dir)


def test_output_file_content():
    """Test that output file contains correct calculated values"""
    products = "product_id,product_name,price\nP001,A,100\nP002,B,200\n"
    order = "product_id,quantity\nP001,3\nP002,2\n"
    
    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)
    
    with open(output_file, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        rows = list(reader)
    
    total_from_file = sum(float(row[1]) for row in rows)
    assert abs(total_from_file - result) < 0.01
    
    shutil.rmtree(temp_dir)


def test_calculation_accuracy():
    """Test calculation accuracy with complex values"""
    products = "product_id,product_name,price\nP001,X,13.25\nP002,Y,27.50\n"
    order = "product_id,quantity\nP001,7\nP002,4\n"
    
    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)
    
    # 7*13.25 + 4*27.50 = 92.75 + 110.00 = 202.75
    assert abs(result - 202.75) < 0.01
    
    shutil.rmtree(temp_dir)


def test_output_format_precision():
    """Test that output values are formatted to 2 decimal places"""
    products = "product_id,product_name,price\nP001,Test,33.33\n"
    order = "product_id,quantity\nP001,3\n"
    
    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)
    
    with open(output_file, "r", newline="") as f:
        reader = csv.reader(f)
        next(reader)
        row = next(reader)
    
    # Check format has exactly 2 decimal places
    assert "." in row[1]
    decimal_part = row[1].split(".")[1]
    assert len(decimal_part) == 2
    
    shutil.rmtree(temp_dir)


def test_return_type():
    """Test that function returns a float"""
    products = "product_id,product_name,price\nP001,A,10\n"
    order = "product_id,quantity\nP001,1\n"

    temp_dir, products_file, order_file, output_file = create_test_files(products, order)
    result = calculate_order_total(products_file, order_file, output_file)

    assert isinstance(result, float)

    shutil.rmtree(temp_dir)


def test_actual_data_files():
    """Test with actual data files to verify output directory"""
    exercise_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    products_file = os.path.join(exercise_dir, "data", "products.csv")
    order_file = os.path.join(exercise_dir, "data", "order.csv")
    output_file = os.path.join(exercise_dir, "data", "total.csv")

    # Run the function
    result = calculate_order_total(products_file, order_file, output_file)

    # Verify output file was created in correct location
    assert os.path.exists(output_file), "Output file should be created in data/ directory"
    assert result >= 0, "Should return a valid total"

    # Clean up the output file
    if os.path.exists(output_file):
        os.remove(output_file)

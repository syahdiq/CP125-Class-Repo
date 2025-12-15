import pytest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from exercise5 import is_valid_triangle

def test_valid_triangle_345():
    # Classic 3-4-5 right triangle
    assert is_valid_triangle(3, 4, 5) == True

def test_valid_triangle_equilateral():
    # Equilateral triangle
    assert is_valid_triangle(5, 5, 5) == True

def test_valid_triangle_isosceles():
    # Isosceles triangle
    assert is_valid_triangle(5, 5, 6) == True

def test_invalid_triangle_straight_line():
    # Forms a straight line, not a triangle
    assert is_valid_triangle(1, 2, 3) == False

def test_invalid_triangle_one_side_too_long():
    # One side is longer than sum of other two
    assert is_valid_triangle(1, 2, 10) == False

def test_invalid_triangle_zero_side():
    # Zero-length side
    assert is_valid_triangle(0, 5, 5) == False

def test_invalid_triangle_negative_side():
    # Negative side length
    assert is_valid_triangle(-1, 5, 5) == False

def test_valid_triangle_large_numbers():
    # Large valid triangle
    assert is_valid_triangle(100, 150, 200) == True

def test_invalid_triangle_exact_sum():
    # Two sides exactly equal third (degenerate case)
    assert is_valid_triangle(5, 5, 10) == False

def test_valid_triangle_floats():
    # Valid triangle with decimal values
    assert is_valid_triangle(3.5, 4.5, 5.5) == True

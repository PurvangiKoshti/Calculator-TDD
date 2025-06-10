"""
Test module for the String Calculator implementation.

This module contains test cases for the StringCalculator class, covering:
- Empty string handling
- Single number addition
- Multiple number addition
- Newline delimiter support
- Custom delimiter support
- Negative number handling
"""

import pytest
from string_calculator import StringCalculator

def test_add_empty_string():
    calculator = StringCalculator()
    assert calculator.add("") == 0

def test_add_single_number():
    calculator = StringCalculator()
    assert calculator.add("1") == 1

def test_add_two_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,2") == 3

def test_add_multiple_numbers():
    calculator = StringCalculator()
    assert calculator.add("1,2,3,4,5") == 15
    assert calculator.add("10,20,30") == 60
    assert calculator.add("1,1,1,1,1,1,1,1,1,1") == 10

def test_add_numbers_with_newlines():
    """Test that numbers separated by newlines are added correctly."""
    calculator = StringCalculator()
    assert calculator.add("1\n2,3") == 6
    assert calculator.add("1\n2\n3") == 6
    assert calculator.add("1,2\n3,4") == 10

def test_add_numbers_with_custom_delimiter():
    """Test that numbers with custom delimiters are added correctly."""
    calculator = StringCalculator()
    assert calculator.add("//;\n1;2") == 3
    assert calculator.add("//.\n1.2.3") == 6
    assert calculator.add("//|\n1|2|3|4") == 10
    assert calculator.add("//*\n1*2*3*4*5") == 15

def test_add_negative_numbers():
    """Test that negative numbers throw appropriate exceptions with correct messages."""
    calculator = StringCalculator()
    with pytest.raises(ValueError) as exc_info:
        calculator.add("-1")
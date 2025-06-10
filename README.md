# String Calculator TDD Kata

This is an implementation of the String Calculator kata using Test-Driven Development (TDD) principles. The calculator can add numbers from a string input with various delimiter formats.

## Features

- Handles empty strings (returns 0)
- Adds single numbers
- Adds multiple numbers separated by commas
- Supports newlines as delimiters
- Supports custom delimiters
- Throws exceptions for negative numbers

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone git@github.com:PurvangiKoshti/Calculator-TDD.git
cd Calculator-TDD
```

2. Create and activate a virtual environment:

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The String Calculator can be used in the following ways:

```python
from string_calculator import StringCalculator

calculator = StringCalculator()

# Basic usage
calculator.add("")  # Returns 0
calculator.add("1")  # Returns 1
calculator.add("1,2")  # Returns 3
calculator.add("1,2,3,4,5")  # Returns 15

# Using newlines as delimiters
calculator.add("1\n2,3")  # Returns 6
calculator.add("1\n2\n3")  # Returns 6

# Using custom delimiters
calculator.add("//;\n1;2")  # Returns 3
calculator.add("//.\n1.2.3")  # Returns 6

# Handling negative numbers (raises ValueError)
try:
    calculator.add("-1")  # Raises: "negative numbers not allowed -1"
    calculator.add("1,-2,3,-4")  # Raises: "negative numbers not allowed -2,-4"
except ValueError as e:
    print(e)
```

## Running Tests

To run the test suite:
```bash
pytest
```

To run tests with verbose output:
```bash
pytest -v
```

To run tests with coverage report:
```bash
pytest --cov=.
```

## Project Structure

```
Calculator-TDD/
├── README.md
├── requirements.txt
├── string_calculator.py
└── test_string_calculator.py
```

## Requirements

- pytest==7.4.3
- pytest-cov==4.1.0


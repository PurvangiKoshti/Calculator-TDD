# String Calculator TDD Kata

This is an implementation of the String Calculator kata using Test-Driven Development (TDD) principles.

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Tests

To run the tests:
```bash
pytest
```

To run tests with coverage:
```bash
pytest --cov=.
```

## Current Implementation

The current implementation handles:
- Empty string returns 0
- Single number returns the number
- Two numbers separated by comma returns their sum

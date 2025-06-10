"""
String Calculator Module

This module implements a string calculator that can add numbers from a string input.
It supports various delimiters including commas, newlines, and custom delimiters.
The calculator follows specific rules for handling empty strings, negative numbers,
and different delimiter formats.
"""

class StringCalculator:
    """
    A calculator class that adds numbers from a string input.
    
    The calculator supports:
    - Empty strings (returns 0)
    - Single numbers
    - Multiple numbers separated by commas or newlines
    - Custom delimiters specified with //[delimiter] format
    - Throws exception for negative numbers
    
    Example:
        calculator = StringCalculator()
        calculator.add("1,2,3")  # Returns 6
        calculator.add("1\n2,3")  # Returns 6
        calculator.add("//;\n1;2")  # Returns 3
    """
    
    def add(self, numbers: str) -> int:
        """
        Add numbers from a string input.
        
        Args:
            numbers (str): A string containing numbers separated by delimiters.
                          Can be empty, contain single or multiple numbers.
                          Can use default delimiters (comma, newline) or custom delimiter.
        
        Returns:
            int: The sum of all numbers in the input string.
        
        Raises:
            ValueError: If the input contains negative numbers.
                      The error message includes all negative numbers found.
        """
        if not numbers:
            return 0
        
        # Check if custom delimiter is specified
        if numbers.startswith('//'):
            # Split the string at first newline to separate delimiter and numbers
            delimiter_part, numbers = numbers.split('\n', 1)
            # Extract the custom delimiter (remove '//' prefix)
            delimiter = delimiter_part[2:]
            # Replace newlines with the custom delimiter
            numbers = numbers.replace('\n', delimiter)
        else:
            # Use default delimiters (comma and newline)
            numbers = numbers.replace('\n', ',')
            delimiter = ','
        
        # Split the string by delimiter and convert to integers
        number_list = [int(num) for num in numbers.split(delimiter)]
        
        # Check for negative numbers
        negative_numbers = [num for num in number_list if num < 0]
        if negative_numbers:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negative_numbers))}")
        
        return sum(number_list) 
class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        # Split the string by comma and convert to integers
        number_list = [int(num) for num in numbers.split(',')]
        return sum(number_list) 
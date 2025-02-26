class Calculator:
    def __init__(self):
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '^': lambda x, y: x ** y,
            '%': lambda x, y: x % y
        }
    
    def calculate(self, num1, operator, num2):
        if operator not in self.operations:
            raise ValueError("Invalid operator")
            
        if operator == '/' and num2 == 0:
            raise ValueError("Cannot divide by zero")
            
        return self.operations[operator](num1, num2) 
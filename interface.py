class UserInterface:
    def __init__(self):
        self.valid_operators = ['+', '-', '*', '/', '^', '%']
    
    def get_input(self):
        print("\nAvailable operations:", ", ".join(self.valid_operators))
        
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator: ")
            num2 = float(input("Enter second number: "))
            return num1, operator, num2
        except ValueError:
            raise ValueError("Please enter valid numbers")
    
    def display_result(self, num1, operator, num2, result):
        print(f"\n{num1} {operator} {num2} = {result}")
    
    def continue_calculation(self):
        while True:
            response = input("\nDo you want to perform another calculation? (y/n): ").lower()
            if response in ['y', 'n']:
                return response == 'y'
            print("Please enter 'y' or 'n'") 
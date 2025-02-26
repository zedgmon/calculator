from operations import Calculator
from interface import UserInterface

def main():
    # Create instances of our calculator and UI
    calc = Calculator()
    ui = UserInterface()
    
    while True:
        # Get user input
        num1, operator, num2 = ui.get_input()
        
        # Perform calculation
        try:
            result = calc.calculate(num1, operator, num2)
            ui.display_result(num1, operator, num2, result)
        except ValueError as e:
            print(f"Error: {e}")
            
        # Ask if user wants to continue
        if not ui.continue_calculation():
            break
    
    print("Thank you for using the calculator!")

if __name__ == "__main__":
    main()
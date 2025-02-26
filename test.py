# Get input from user
print("Simple Calculator")
print("Operations: +, -, *, /")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform calculation based on operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero!")
        exit()
else:
    print("Invalid operator!")
    exit()

# Display result
print(f"{num1} {operator} {num2} = {result}")





# Stage 2

# Taking input from user
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Using if-elif-else to perform operation
if operator == "+":
    result = num1 + num2
    print("Result:", result)

elif operator == "-":
    result = num1 - num2
    print("Result:", result)

elif operator == "*":
    result = num1 * num2
    print("Result:", result)

elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
        result = None
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid operator! Please use +, -, *, or /.")
    result = None

# Check if result exists before analyzing
if result is not None:
    if result > 0:
        print("The result is Positive.")
    elif result < 0:
        print("The result is Negative.")
    else:
        print("The result is Zero.")
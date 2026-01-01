def calculator(a, b, operation):
    if operation == "Add":
        return a + b
    elif operation == "Subtract":
        return a - b
    elif operation == "Multiply":
        return a * b
    elif operation == "Divide":
        if b == 0:
            return "Error: Cannot divide by zero"
        return a / b
    else:
        return "Invalid operation"

print(calculator(10, 5, "add"))


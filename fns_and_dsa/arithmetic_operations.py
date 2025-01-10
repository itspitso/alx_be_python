def perform_operation(num1, num2, operation):
    if operation == 'add': 
        return float(num1 + num2)
    elif operation == 'subtract':
        return float(num1 - num2)
    elif operation == 'multiply':
        return float(num1 * num2)
    elif operation == 'divide':
        if num2 == 0:
            return "Cannot divide by zero"
        else:
            return float(num1 / num2)


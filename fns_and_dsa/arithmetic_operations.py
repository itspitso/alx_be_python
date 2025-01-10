def perform_operation(num1, num2, operation):
    if operation == 'add': 
        return float(num1 + num2)
    elif operation == 'subtract':
        return float(num1 - num2)
    elif operation == 'multiply':
        return float(num1 * num2)
    elif operation == 'divide':
        try:
            result = float(num1 / num2)
            return result
        except ZeroDivisionError:
            return "Cannot divide by zero"

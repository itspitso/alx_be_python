def perform_operation(num1, num2, operator):
    match operator:
        case 'add':
            return float(num1 + num2)
        case 'subtract':
            return float(num1 - num2)
        case 'multiply':
            return float(num1 * num2)
        case 'divide':
            try:
                result = float(num1 / num2)
                return result
            except ZeroDivisionError:
                return "Cannot divide by zero"

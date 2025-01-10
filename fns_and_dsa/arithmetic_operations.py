def perform_operation(num1, num2, operator):
    match operator:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            try:
                result = num1 / num2
                return result
            except ZeroDivisionError:
                return "Cannot divide by zero"

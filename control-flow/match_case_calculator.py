first_number = int(input('Enter the first number:'))
second_number = int(input('Enter the second number:'))
operation = input('Choose the operation (+, -, *, /):')

match operation:
    case '+': 
        print(f'The result is {first_number+second_number}.')
    case '-': 
        print(f'The result is {first_number-second_number}.')
    case '*': 
        print(f'The result is {first_number*second_number}.')
    case '/': 
        try:
            print(f'The result is {first_number/second_number}.')
        except:
            print('Cannot divide by zero')
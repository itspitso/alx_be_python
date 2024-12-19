task = input('Input a task description:')
priority = input("Enter the task's priority? (high/medium/low):")
time_bound = input("Is the task time-bound? (yes or no):")

match priority:
    case 'high':
        message = f'{task} is a high priority task'
    case 'medium':
        message = f'{task} is a medium priority task'
    case 'low':
        message = f'{task} is a low priority task'

if time_bound == 'yes':
    message += ' that requires immediate attention today!'
else:
    message += '. Consider completing it when you have free time.'
print(message)

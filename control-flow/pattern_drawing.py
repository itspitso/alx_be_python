size = int(input('Enter the size of the pattern:'))
symbol = '*'
i = 0
while i < size: 
    for j in range(1, size+1):
        print(symbol, end="")
    print('\n')
    i += 1

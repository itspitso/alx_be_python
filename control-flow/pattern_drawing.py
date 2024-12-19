size = input('Enter the size of the pattern:')
size_int = int(size)
symbol = '*'
i = 0
while i < size_int: 
    for j in range(1, size_int+1):
        print(symbol, end="")
    print('\n')
    i += 1

size = input('Enter the size of the pattern:')
size_int = int(size)
symbol = '*'
for i in range(1, size_int+1):
    print(f'{symbol*size_int}')
rows = int(input('Enter number of rows: '))
for i in range(rows):
    print(' ' * (rows - i), end=' ') 
    num = 1
    for j in range(i + 1):
        print(num, end='')
        num = num * (i - j) // (j + 1)
    print()

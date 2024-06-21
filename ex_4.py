number = int(input('Введите число до 100: '))
if number == 11 or number == 12 or number == 13 or number == 14:
    print(f'{number} попугаев')
elif number % 10 == 1 or number == 1:
    print(f'{number} попугай')
elif number % 10 == 2 or number == 2:
    print(f'{number} попугая')
elif number % 10 == 3 or number == 3:
    print(f'{number} попугая')
elif number % 10 == 4 or number == 4:
    print(f'{number} попугая')
else:
    print(f'{number} попугаев')

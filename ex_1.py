year = input('Введите год: ')
if year[-1] != 0 and year[-2] != 0:
    if int(year) % 4 == 0 and int(year) % 100 != 0:
        print('366')
    else:
        print('365')
else:
    if int(year) % 400 == 0:
        print('366')
    else:
        print('365')

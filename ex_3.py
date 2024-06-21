number = int(input('Введите четырехзначное число: '))
if number % 10 == int(number // 1000):
    if str(((number - (number % 10)) % 1000)) in ('000, 110, 220, 330, 440, 550, 660, 770, 880, 990'):
        print('настоящее')
    else:
        print('кривое')
else:
    print('кривое')


#немного видоизменила условие, сделала проще:
number = int(input('Введите четырехзначное число: '))
if number % 10 == int(number // 1000):
    if ((number - (number % 10)) % 1000) % 110 == 0:
        print('настоящее')
    else:
        print('кривое')
else:
    print('кривое')

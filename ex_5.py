weight = float(input('Введите свой вес в фунтах:'))
length = float(input('Введте свой вес в дюймах:'))
index = (round((weight * 0.453592) / ((length * 2.54) / 100) ** 2, 2))
if index < 16:
    print('выраженный дефицит массы тела')
elif 16 <= index <= 18.49:
    print('недостаточная масса тела ')
elif 18.5 <= index <= 24.99:
    print('норма')
elif 25 <= index <= 29.99:
    print('избыточная масса тела')
elif 30 <= index <= 34.99:
    print('ожирение первой степени')
elif 35 <= index <= 39.99:
    print('ожирение второй степени')
else:
    print('ожирение третьей степени')

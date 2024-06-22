pin_code = input('Введите PIN-код: ')
answer = 'OK'

if len(pin_code) != 4:
    answer = 'ERROR'

for i in pin_code:
    if pin_code.count(i) > 1:
        answer = 'ERROR'

if 1900 <= int(pin_code) <= 2050:
    answer = 'ERROR'

print(answer)

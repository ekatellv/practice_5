knuts = int(input('Введите количество кнатов: '))
galleons = knuts // (29 * 17)
sickles = (knuts - (galleons * 29 * 17)) // 29
knuts -= 29 * ((galleons * 17) + sickles)
if galleons != 0:
    print(galleons, 'галлеонов')
if sickles != 0:
    print(sickles, 'сиклей')
if knuts != 0:
    print(knuts, 'кнатов')

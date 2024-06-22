n, k, m = map(int, input('Введите количество станций, вашу станци, станцию назначения через пробел: ').split())
way_1 = abs(m - k) - 1
way_2 = count_counter = n - max(k, m) + min(k, m) - 1
if n < k or n < m:
    print('неверные данные')
elif k == m:
    print(0)
elif way_1 >= way_2:
    print(way_2)
else:
    print(way_1)

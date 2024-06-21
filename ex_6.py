f, s, t = map(int, input('Введите, сколько подданых видели улыбку за три дня через пробел: ').split())
if f != s and f != t:
    print(1)
elif f != s and f == t:
    print(2)
elif f == s and f != t:
    print(2)
else:
    print(3)

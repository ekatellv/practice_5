f, s, t = map(int, input('Введите значение трех вершин через пробел:').split())
sum = f + s + t
print(max(f, s, t), sum - max(f, s, t) - min(f, s, t), min(f, s, t))


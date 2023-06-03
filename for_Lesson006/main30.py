a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

progression = [a1 + (i - 1) * d for i in range(1, n+1)]
print(progression)
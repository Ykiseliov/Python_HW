# Задача 12
#  Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя
# помогает Кате по математике. Он задумывает два натуральных числа X и Y
# (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать
# задуманные Петей числа.

s = int(input("Введите число суммы: ")) # ввод суммы
p = int(input("Введите число произведения: ")) # ввод произведения

# перебор всех возможных значений x и y
for x in range(1, 1001):
    for y in range(1, 1001):
        if x+y == s and x*y == p: # проверка условий
            print(x,y) # вывод ответа
            break # прерываем цикл, если ответ найден
    else:
        continue # продолжаем цикл, если ответ не найден
    break # прерываем внешний цикл, если ответ найден
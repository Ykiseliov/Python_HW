# Задача 24

N = int(input("Кол-во кустов: "))
a = list(map(int, input("Кол-во ягод на каждом кусте (чпб): ").split()))

max_sum = 0

for i in range(N):
    sum_i = a[i] + a[(i-1)%N] + a[(i+1)%N]
    max_sum = max(max_sum, sum_i)

print("максимальное кол-во ягод", max_sum)

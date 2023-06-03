min = int(input("Min: "))
max = int(input("Max: "))
list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
index = []
for i in range(len(list_1)):
    if list_1[i] >= min and list_1[i] <= max:
        index.append(i)
print(index)
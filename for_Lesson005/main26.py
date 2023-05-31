def pow_recursive(a, b):
    if b == 0:
        return 1
    else:
        return a * pow_recursive(a, b-1)

a = int(input("Введите число А: "))
b = int(input("Введите число B: "))

rst = pow_recursive(a, b)
print(f"{a},{b} -> {rst}")

a,b = int(input("Введите A: ")), int(input("Введите B: "))

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a^b, (a&b)<<1)
    
result = sum(a, b)
print(f"{a},{b} -> {result}")

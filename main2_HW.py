num = int(input("введите трехзначное число: "))
digit1 = num // 100
digit2 = num % 100 // 10
digit3 = num % 10
sum = digit1 + digit2 + digit3
print (sum)
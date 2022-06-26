import random

a = random.randint(100, 999)
print(a)

a1 = a // 100
print(a1)
a2 = (a // 10) % 10
print(a2)
a3 = a % 10
print(a3)

print("Сумма чисел случайного числа: ", a1+a2+a3)
import random
from array import *

a = array('f', [1.5, 2.0, 3.5, 2.0, 7.1, 4.2, 2.0])
print(a)

# перше завдання
x = float(input("Введіть значення: "))
print("Індекси елементів, що дорівнюють", x, ":")
for i in range(len(a)):
    if a[i] == x:
        print(i)

# друге завдання
suma = 0
for i in range(0, len(a), 2):
    suma += a[i]
print("Сума елементів з парними індексами:", round(suma, 2))

# третє завдання
for i in range(3):
    y = random.randint(1, 10)
    a.append(y)
print(a)
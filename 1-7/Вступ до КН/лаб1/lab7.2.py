import numpy as np

mas = np.zeros((3, 3), dtype=int)

for i in range(3):
    for j in range(3):
        mas[i][j] = np.random.randint(0, 8)

print(mas)

# завдання 1
for j in range(3):
    suma = 0
    for i in range(3):
        suma += mas[i][j]
    print("Сума стовпчика", j + 1, ":", suma)

# завдання 2
mas[1][1] = -4
print(mas)
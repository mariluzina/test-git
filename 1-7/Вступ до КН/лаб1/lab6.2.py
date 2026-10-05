n = int(input("Введіть кількість рядків N: "))

lines = []
for i in range(n):
    lines.append(input("Введіть рядок: ").split())

# пошук найдовшого слова
max_i = 0
max_j = 0
for i in range(n):
    for j in range(len(lines[i])):
        if len(lines[i][j]) > len(lines[max_i][max_j]):
            max_i = i
            max_j = j

# зміна порядку символів на протилежний
lines[max_i][max_j] = lines[max_i][max_j][::-1]

for i in range(n):
    print(" ".join(lines[i]))
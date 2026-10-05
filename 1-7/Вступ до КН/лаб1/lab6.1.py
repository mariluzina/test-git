s = input("Введіть рядок: ")

upper = ""
lower = ""
count_upper = 0
count_lower = 0

for ch in s:
    if ch.isupper():
        upper = upper + ch
        count_upper = count_upper + 1
    elif ch.islower():
        lower = lower + ch
        count_lower = count_lower + 1

print("Великі літери:", upper)
print("Малі літери:", lower)
print("Кількість великих літер:", count_upper)
print("Кількість малих літер:", count_lower)
import math
x = float(input("Введіть x: "))
if x>25:
    f = math.sqrt(5+x) - math.sin(x)
elif 0 <= x <= 25:
    f = -4*x+math.exp(x)
else:
    f = -math.pi*x+math.cos(math.pi*x)

print("f(x) =", f)
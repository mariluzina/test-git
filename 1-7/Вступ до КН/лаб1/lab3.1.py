import math
a=float(input("Введіть сторону a: "))
b=float(input("Введіть сторону b: "))
c=float(input("Введіть сторону c: "))
p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
if a <= b and a <= c:
  h=2 * S / a
elif b <= a and b <= c:
  h = 2 * S / b
else:
  h = 2 * S / c

print("Найбільша висота:", h)
import math

a=float(input("Введіть нижню межу табулювання: "))
b=float(input("Введіть верхню межу табулювання: "))
h=float(input("Введіть крок табулювання: "))
x=a

for i in range(200):
    x=round(x,2)
    y=2*x+3*x**3-math.exp(x)
    y=round(y,2)
    print(i,'  ',x,'   ',y)
    if x>=b:
        break
    x+=h
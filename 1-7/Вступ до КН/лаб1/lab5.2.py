import math

a=float(input("Введіть нижню межу табулювання: "))
b=float(input("Введіть верхню межу табулювання: "))
h=float(input("Введіть крок табулювання: "))
x=a

while x<=b:
    x=round(x,2)
    
    if x==0:
        print(x,'   ','Помилка: ln(0) не визначений')
    else:
        y=0.7+2.24*math.exp(x+0.4)+math.log(abs(x))
        y=round(y,2)
        print(x,'   ',y)
    
    x+=h
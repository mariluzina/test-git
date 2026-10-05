def whole(x):
    a=int(x)
    print("Ціла частина =",a)
def fraction(x):
    b=x-int(x)
    print("Дробова частина =",round(b,2))
x=float(input("Введіть дійсне число: "))
whole(x)
fraction(x)
def potential(m,h):
    g=9.8
    Ep=m*g*h
    return(Ep)

def kinetic(m,v):
    Ek=m*v**2/2
    return(Ek)

m=float(input("Введіть масу тіла: "))
h=float(input("Введіть висоту: "))
v=float(input("Введіть швидкість: "))

ep=potential(m,h)
ek=kinetic(m,v)

print("Потенціальна енергія =",ep)
print("Кінетична енергія =",ek)
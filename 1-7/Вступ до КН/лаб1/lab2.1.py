import sys
import math
a=float(sys.argv[1])
S=math.sqrt(3)*a**2
V=a**3/(6*math.sqrt(2))
D=2*a/math.sqrt(3)
print("Повна площа тетраедра =",S)
print("Об'єм тетраедра =",V)
print("Діаметр описаного кола =",D)
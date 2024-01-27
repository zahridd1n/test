import math
a=float(input("a ni kiriting:"))
b=float(input("b ni kiriting:"))
x=float(input("x ni kiriting:"))
Z=((x**2+a**2)**(0.5))*math.atan(x/a)-(math.log10(b)/math.tan(x))
print(Z)
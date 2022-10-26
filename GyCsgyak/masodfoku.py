import math

a: int=None
b: int=None
c: int=None
x: int=None
x1: int=None
x2: int=None

print("Kérem adja meg az a értékét!")
a=int(input())

print("Kérem adja meg a b értékét!")
b=int(input())

print("Kérem adja meg a c értékét!")
c=int(input())

x1=(-b+math.sqrt(math.pow(b,2)-4*a*c))/(2*a)
x2=(-b-math.sqrt(math.pow(b,2)-4*a*c))/(2*a)

print(f"A másodfokó egyenlet két megoldása a/az {x1} és {x2}")
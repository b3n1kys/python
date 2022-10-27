from turtle import right


num1: int=None
num2: int=None

print("Kérem adjon meg egy számot")
num1=int(input())

print("Kérem adjon meg egy másik számot")
num2=int(input())

if (num1 > num2):
    print(f"{num1}")
elif (num2 > num1):
    print(f"{num2}")
else:
    print("A két szám egyenlő")
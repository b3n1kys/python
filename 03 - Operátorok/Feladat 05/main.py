from cgitb import reset


num1: int=None
num2: int=None
num3: int=None
num4: int=None
addition: int=None
subtraction: int=None
result: float=None

print("kérem az első számot")
num1=int(input())

print("Kérem a mnásodik számot")
num2=int(input())

print("Kérem a harmadik számot")
num3=int(input())

print("Kérem a negyedik számot")
num4=int(input())

addition=num1+num2
subtraction=num3-num4
result=addition/subtraction

print(f"AZ eredmény: {result}")
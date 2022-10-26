num1: int=None
num2: int=None
num3: int=None
addition: float=None
subtraction: float=None
result: float=None

print("Kérem az első számot")
num1=int(input())

print("Kérem a második számot")
num2=int(input())

print("Kérem a harmadik számot")
num3=int(input())

addition=num1+0.5
subtraction=num2-0.7
result=(addition*subtraction)%num3

print(f"Az eredmény: {result}")

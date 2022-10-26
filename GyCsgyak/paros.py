szam:int=None

print("Írjon be egy számot")
szam=int(input())

if szam%2==0:
    print(f"{szam} páros")
else:
    print(f"{szam} páratlan")
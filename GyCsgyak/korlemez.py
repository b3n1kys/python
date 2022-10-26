a:int=None
b:int=None
x:int=None
y:int=None
r:int=None

print("Kérem adja meg a kör adatait(x, y, r)!")
x=int(input())
y=int(input())
r=int(input())

print('"Kérem adja meg egy pontnak a kordinátáit!')
a=int(input())
b=int(input())

if (x-a)**2+(y-b)**2<=r**2:
    print("A pont a körlemezen van")
else:
    print("A pont nincs a körlemezen")
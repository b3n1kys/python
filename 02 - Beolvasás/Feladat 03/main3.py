from os import system

height: float=None
name: str=None

print("Kérem adja meg a nevét!")
name=str(input())
print("kérem adja meg a magasságát!")
height=float(input())

system('cls')

print(f"{name} az ön magassága {height}m!")
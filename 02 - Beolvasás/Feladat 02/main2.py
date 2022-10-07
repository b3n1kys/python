from os import system

name: str=None
date: int=None

print("Kérem adja meg a nevét, és a születési évét!")
name=str(input())
date=int(input())

system('cls')

print(f"{name} ön {date} született")

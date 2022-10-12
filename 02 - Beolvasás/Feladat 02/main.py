from os import system

name: str=None
date: int=None

print("Kérem adja meg a nevét!")
name=str(input())

print("Kérem adja meg a születési évét!")
date=int(input())

system('cls')

print(f"{name} ön {date} született")

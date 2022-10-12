from os import system

buttonPressed: str=None
name: str=None

print("Kérem adja meg a nevét!")
name=str(input())

print("Kérem nyomjon meg egy gombot a billentyűzeten!")
buttonPressed=str(input())

system('cls')

print(f"{name} ön a/az {buttonPressed} billentyűt nyomta meg")
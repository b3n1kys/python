from os import system

bandName: str=None
bestSong: str=None
trackLength: float=None

print("Kérem adja meg a kedvenc együttesének a nevét")
bandName=str(input())

print("Kérem adja meg a kedvenc együttesének a legjovbb számát")
bestSong=str(input())

print("Kérem adja meg az együttesnek legjobb számának hosszát")
trackLength=float(input())

system('cls')

print(f"Az ön kedvenc együttesének {bandName} a legjobb zeneszáma {bestSong} melynek hossza {trackLength} perc!")
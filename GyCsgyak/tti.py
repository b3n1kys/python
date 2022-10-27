height: float=None
weight: float=None
tti: float=None
squared: float=None

print("Kérem adja meg a testmagasságát")
height=float(input())

print("Kérem adja meg a testsúlyát")
weight=float(input())

squared=(height**2)
tti=(weight/squared)

print(f"A teströmeg indexe: {tti}")

if tti>=18.5 and tti<=25:
    print("Önnek normális a testsúlya")
elif tti<18.5 and tti>=17:
    print("Ön enyhény sovány")
elif tti<17 and tti>=16:
    print("Ön mérsékelten sovány")
elif tti< 16:
    print("Ön súlyosan sovány")
elif tti>=25 and tti<30:
    print("Ön túlsúlyos")
elif tti>=30 and tti<35:
    print("Ön 1.fokú elhízásban szenved")
elif tti>35 and tti<=40:
    print("Ön 2. fokó elhízásban szenved")
else:
    print("Ön súlyosan elhízott")
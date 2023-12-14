import random as r

a = r.randint(0,12)
b = r.randint(0,12)

print("Combien vaut", a, "+", b, "?")

c = int(input())

if c == a+b:
    print("Bravo")
else:
    print("Perdu")
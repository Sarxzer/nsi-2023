chaine = "test"

print("longueur =", len(chaine))

for carac in chaine:
    print(carac)
    chaine ="==>" + chaine
print(chaine)
print("longueur =", len(chaine))
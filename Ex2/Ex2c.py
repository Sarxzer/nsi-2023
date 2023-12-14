classe = input("Classe (A ou B):").lower()
groupe = int(input("Groupe (1 ou 2):"))

if classe=="a":
    if groupe==1:
        print("Salle 1")
    else:
        print("Groupe introuvable")
elif classe=="b":
    if groupe==1:
        print("Salle 2")
    elif groupe==2:
        print("Salle 3")
    else:
        print("Groupe introuvable")
else:
    print("Classe introuvable")

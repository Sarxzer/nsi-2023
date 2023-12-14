Pseuil = 1.2
Vseuil = 3.4

P = float(input("Préssion :"))
V = float(input("Volume :"))

if P > Pseuil and V > Vseuil:
    print("Arrêt Imédiat")
elif P > Pseuil and V <= Vseuil:
    print("Augmenté le volume de l'enceinte")
elif P <= Pseuil and V > Vseuil:
    print("Diminuer le volume de l'enceinte")
else:
    print("Tout va bien ☺")
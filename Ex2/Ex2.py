nom = input("Entre ton nom :")
age = int(input("Entre ton age :"))

print("Bonjour " + nom)
if age >= 18:
    print("Tu est majeur")
else:
    print("Tu est mineur")
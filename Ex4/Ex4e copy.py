def damier(n:int,e:int):
    a="" #text de fin qui se rempli grace au programe
    i = n #compteur de la hauteur
    while i!=0:
        for k in range(e): #epaiseur de 3 en hauteur
            j=n #compteur de la largeur
            while j!=0:
                if (j+i)%2==0:
                    print(e*"▯", end=' ')
                else:
                    print(e*"▮", end=' ')
                j-=1
            print("\n") #retour a la ligne
        i-=1

damier(int(input("taille damier?")),int(input("epaisseur?")))
#print("▯▮")

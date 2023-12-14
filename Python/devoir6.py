def recherche_naïf(chaine,mot):
    out = []
    for i in range(len(chaine)):
        if chaine[i:i+len(mot)] == mot:
            out.append([i+1, i+len(mot)])
    
    return "ce mot est en position " + str(out)

print(recherche_naïf("Un mot est recherché, ce mot est inconu", "ce"))
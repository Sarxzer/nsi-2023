def voyelle(chaine, pos=False):
    out = ""
    for i in chaine:
        if i in "aeiouyAEIOUY":
            out = out + i
            if pos:
                out = out + str(chaine.index(i))
                chaine = chaine.replace(chaine[chaine.index(i)], "#", 1)
            
    return(out)

print(voyelle("blabla",True))
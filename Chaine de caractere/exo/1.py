def voyelle(chaine: str):
    out = ""
    for i in chaine:
        if i in ["a","e","i","o","u","y","A","E","I","O","U","Y"]:
            out = out + i
    return(out)

print(voyelle("AzertyuiopmkhARhvSvNhsg,bdxBBcsHb"))
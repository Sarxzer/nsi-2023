import random

def rand_word(text:str,rand:int):
    temp = []
    out = ""
    list_text = text.split(" ")
    for i in list_text:
        if len(i) > 3:
            car = list(i)
            for j in range(1, len(i)-1):
                element = car.pop(j)
                car.insert(random.randint(1, len(i)-2), element)
        else:
            car=i
        temp.append("".join(car))
    for k in temp:
        out += ''.join(k)
        out += ' ' if k != len(temp) else ''
    return out



print(rand_word("La spécialité NSI est realisée au lycée cette année 2020",0))
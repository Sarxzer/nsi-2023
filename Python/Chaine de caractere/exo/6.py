def caesar_crypt(text:str,rot:int):
    letter = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for i in range(0, len(text)):
        out += (letter[letter.index(text[i])+rot-26*(int((i+rot)/26))] if text[i].islower() else letter[letter.index(text[i].lower())+rot-26*(int((i+rot)/26))].upper()) if text[i].lower() in letter else text[i]
    return out

print(caesar_crypt(input("text: "),int(input("rot: "))))
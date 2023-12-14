def caesar_crypt(text:str,rot:int):
    letter = "abcdefghijklmnopqrstuvwxyz"
    out = ""
    for i in range(1, len(text)+1):
        out += letter[i+rot-(26*int((i+rot)/26))-1]
    return out

print(caesar_crypt(input("text: "),int(input("rot: "))))
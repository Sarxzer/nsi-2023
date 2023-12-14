def letter_count(text,letter):
    out = 0
    for i in text:
        out += 1 if i == letter else 0
    return out

def letter_pos(text,letter):
    out = []
    for i in range(len(text)):
        out.append(i) if text[i] == letter else False
    return out


print(letter_count(input("input:"),input("letter:")))
print(letter_pos(input("input: "),input("letter: ")))
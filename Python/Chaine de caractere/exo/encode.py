def encode(text:str):
    out = '1'
    temp = [x for x in text]
    for i in temp:
        out += (3-len(str(ord(i)))==1)*'0'
        out += str(ord(i))
    return out

def decode(code):
    out = ''
    temp = str(code).replace(str(code)[0],'',1)
    temp = [temp[i:i+3] for i in range(0,len(temp),3)]
    for i in temp:
        out = out + chr(int(i))
    return out

print(encode('Bonjour, j\'ai encodé ce paragraph'))
print(decode(1066111110106111117114044032106039097105032101110099111100233032099101032112097114097103114097112104))
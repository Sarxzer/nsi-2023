def encode(text:str):
    out = '1'
    temp = [x for x in text]
    for i in temp:
        out += (6-len(str(ord(i))))*'0'
        out += str(ord(i))
    return out

def decode(code):
    out = ''
    temp = str(code).replace(str(code)[0],'',1)
    temp = [temp[i:i+6] for i in range(0,len(temp),6)]
    for i in temp:
        out = out + chr(int(i))
    return out

print(encode('Bonjour, j\'ai encodé ce paragraph'))
print(decode(1000066000111000110000106000111000117000114000044000032000106000039000097000105000032000101000110000099000111000100000233000032000099000101000032000112000097000114000097000103000114000097000112000104))
print(encode('您好，此文本为中文'))
print(decode(1024744022909065292027492025991026412020026020013025991))
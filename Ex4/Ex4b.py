def triangle(s: int,inver):
    if inver=="n":
        i = 1
        while i <= s:
            print(i*"*")
            i+=1
    elif inver=="y":
        i = s
        while i >= 1:
            print(i*"*")
            i-=1


triangle(int(input("taille triangle?")),input("inversé?(y/n)"))
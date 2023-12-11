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

def multi_triangle(s:int,n:int,inver,):
    while n!=0:
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
        n-=1


multi_triangle(int(input("taille triangle?")),int(input("nombre triangle?")),input("inversé?(y/n)"))
def damier(n:int):
    a=""
    i = n
    while i!=0:
        j=n
        while j!=0:
            if (j+i)%2==0:
                a=a+"▯"
            else:
                a=a+"▮"
            j-=1
        a=a+"\n"
        i-=1
    print(a)

damier(int(input("taille damier?")))
#print("▯▮")
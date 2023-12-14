for d in range(100):
    for u in range(10):
        n = 10*d+u
        n = (3-len(str(n)))*"0"+str(n)
       
        if n[-1]=="3" and int(n[-2])%2==0 and int(n[0])+int(n[1])+int(n[2])>=15:
            print(n)
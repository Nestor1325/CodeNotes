#CORREGIR

n = int(input(">"))
swa = False
swm = False
swb = False

def validar(x):
    if  x == "alto":
        return 0
    elif x == "medio":
        return 1
    elif x == "bajo":
        return 2
    else:
        return 3

for i in range(1, n +1 ,1):
    x = str(input(">"))
    res = ""
    for j in range(0, len(x) ,1):
        if x[j] != ",":
            res = res + x[j]
        else:
            if validar(res) == 0:
                swa = True
            elif validar(res) == 1:
                swm = True
            elif validar(res) == 2:
                swb = True
            else:
                print("error")
            res = ""
    if swa:
        print("1",end="")
    else:
        print("0",end="")
    if swm:
        print("1",end="")
    else:
        print("0",end="")
    if swb:
        print("1",end="")
    else:
        print("0",end="")
    print()

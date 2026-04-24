n = int(input("n: "))




for i in range(1, n + 1, 1):
    x = str(input(">"))

    ca,ce,ci,co,cu = 0,0,0,0,0

    for j in range(0, len(x), 1):
        if x[j] == "a":
            ca = ca + 1
        if x[j] == "e":
            ce = ce + 1
        if x[j] == "i":
            ci = ci + 1
        if x[j] == "o":
            co = co + 1
        if x[j] == "u":
            cu = cu + 1
    
    print(ca,ce,ci,co,cu)
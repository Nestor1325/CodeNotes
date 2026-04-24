x = str(input("cadena: "))

cc = int(input(">"))

for i in range(0 , len(x), 1):
    newc = ord(x[i]) + cc
    print(chr(newc),end="")
    
print("")
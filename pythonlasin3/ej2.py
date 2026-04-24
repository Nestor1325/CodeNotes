n = int(input("n: "))
cont = 0
for i in range(1, n + 1, 1):
    x = str(input(">"))

    if x[0] == x[len(x)-1]:
        cont = cont + 1
print(cont)



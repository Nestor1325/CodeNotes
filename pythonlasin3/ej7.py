n = int(input("n: "))

c = 0

for i in range(1, n + 1, 1):
    A = str(input(">"))
    nA = len(A)
    sw = False

    for k in range(0, nA, 1):
        if A[k] == "a" or A[k] == "A":
            sw = True
    if sw:
        c = c + 1
print(c)
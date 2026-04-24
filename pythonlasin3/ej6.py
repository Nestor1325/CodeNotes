n = int(input("n: "))

for i in range(1, n + 1, 1):
    x = str(input(">"))

    new = ""
    for j in range(0, len(x), 1):
        if x[j] == " ":
            print(new)
            j = j + 1
            new = ""
        new = new + x[j]
    print(new)
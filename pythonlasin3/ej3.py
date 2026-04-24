n = int(input("n: "))
new = ""
for i in range(1, n + 1, 1):
    x = str(input(">"))
    new = new + x[0]
print(new)
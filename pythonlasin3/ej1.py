n = int(input())

for i in range(1, n + 1, 1):
    x = str(input(">"))
    if len(x) % 2 == 0:
        print(x[(len(x) // 2) - 1] + x[len(x) // 2])
    else:
        print(x[len(x) // 2])
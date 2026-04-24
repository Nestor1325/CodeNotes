cad = str(input(">"))

def funcion(cad):
    for i in range(0, len(cad), 1):
        sw = True
        for j in range(10):
            if cad[i] == str(j):
                sw = False
        if sw and cad[i] == " ":
            print(f"{cad[i]} espacio")
        elif sw and cad[i] == cad[i].lower():
            print(f"{cad[i]} minuscula")
        elif sw and cad[i] == cad[i].upper():
            print(f"{cad[i]} Mayuscula")
        else:
            print(f"{cad[i]} no es una letra")

funcion(cad)
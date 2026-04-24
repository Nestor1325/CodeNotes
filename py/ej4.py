print(ord("A"), ord("Z"), ord("a"), ord("z"), ord("0"), ord("9"))

def validar(char):
    if ord(char) >= 65 and ord(char) <= 90:
        print("mayuscula")
    elif ord(char) >= 97 and ord(char) <= 122:
        print("minuscula")
    elif ord(char) >= 48 and ord(char) <= 57:
        print("numero")
    else:
        print(" ")

def clasificacion ():

    grados=int(input("Dime la temperatura en grados Celsius "))

    if grados >= 0 and grados <10:
        print("Está haciendo frio")
    elif grados >= 11 and grados <= 20:
        print("Está templado ")
    elif grados >= 22 and grados <= 25:
        print("Está calido ")
    elif grados >= 26 and grados <=36:
        print("Está muy calido ")
    else:
        print("Esta temperatura rompe los limites")

clasificacion()
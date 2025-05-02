def clasificacion ():
    numero=float(input("Dime un numero"))
    if numero %2 == 0:
        print("Este numero es par")
    elif numero %2 != 0:
        print("Este numero es impar")
    else: 
        print("Este numero es nulo")
clasificacion()
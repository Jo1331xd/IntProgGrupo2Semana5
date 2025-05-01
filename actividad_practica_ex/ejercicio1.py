def numeros (numero=0, numero2= 0):
    if numero < numero2:
        for i in range(numero, numero2 + 1):
            print(i, end=" ")
    else:
        for i in range(numero2, numero + 1):
            print(i, end=" ")


def main():
    numero = int(input("Ingrese un numero: "))
    numero2 = int(input("Ingrese otro numero: "))
    numeros(numero, numero2)

main()

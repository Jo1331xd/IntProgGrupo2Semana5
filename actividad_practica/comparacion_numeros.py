numero1=int(input("Dame primer numero: "))
numero2=int(input("Dame segundo numero: "))
numero3=int(input("Dame tercer numero: "))


print("="*30)

if numero1 > numero2 and numero1 > numero3:
    print("El numero mayor es: ", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("El numero mayor es: ", numero2)
elif numero3 > numero2 and numero3 > numero1:
    print("El numero mayor es: ", numero3)

if numero1 < numero2 and numero1 < numero3:
    print("El numero menor es: ", numero1)
elif numero2 < numero1 and numero2 < numero3:
    print("El numero menor es: ", numero2)
elif numero3 < numero2 and numero3 < numero1:
    print("El numero menor es: ", numero3)

elif numero1 == numero2 and numero2 == numero3:
    print("Todos los numeros son iguales")

print("="*30)

def suma(sumar):
    num=int(input("Ingrese el numero que desea sumar "))
    num2=int(input("Ingrese el otro "))    
    sumar_numeros=num + num2
    print(f"{num} + {num2} = {sumar_numeros}")

def resta(restar):
    num=int(input("Ingrese el numero que desea restar "))
    num2=int(input("Ingrese el otro "))
    resta_numeros= num - num2
    print(f"{num} - {num2} = {resta_numeros}")

def division(dividir):
    num=float(input("Ingrese su numerador "))
    num2=float(input("Ingrese su denominador "))
    division_numeros= num / num2
    print(f"{num} / {num2} = {division_numeros:.2f}")

def multiplicacion (multiplicar):
    num=float(input("Ingrese el numero a multiplicar "))
    num2=float(input("Ingrese el otro numero a multiplicar "))
    multiplicar_numeros= num * num2
    print(f"{num:.0f} x {num2:.0f} = {multiplicar_numeros:.2f}")

def tabla_multplicacion ():
     num=int(input("¿Cual es el numero que desea saber su tabla? "))
     for i in range (1,11):
         tabla= num * i
         print(f"{num} x {i} = {tabla}")

def menu ():
    print("="*45)
    print("Seleccione la opcion que desea usar")
    print("="*45)
    print("""  
          - SUMAR
          - RESTAR
          - DIVIDIR
          - MULTIPLICAR
          - TABLA DE MULTIPLICAR""")

    opcion=input("")

    if opcion== "SUMAR":
        suma(sumar=0)
    elif opcion== "DIVIDIR":
            division(dividir=0)
    elif opcion== "MULTIPLICAR":
            multiplicacion(multiplicar=0)
    elif opcion == "RESTAR":
            resta(restar=0)
    elif opcion == "TABLA DE MULTIPLICAR":
            tabla_multplicacion()

menu()
    
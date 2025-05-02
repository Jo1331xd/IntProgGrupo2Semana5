def dias ():
    print(""" días de la semana
    - 1 = Lunes
    - 2 = Martes
    - 3 = Miercoles
    - 4 = Jueves
    - 5 = Viernes
    - 6 = Sabado
    - 7 = Domingo""")

    dias=(input("Digame un día de la semana que desea saber: "))
    
    if dias in ["1", "2", "3", "4", "5"]:
        print ("Es día laboral ")
    elif dias in ["6", "7"]:
        print ("Es fin de Semana ")
    else: 
        print("Día invalido")
dias() 
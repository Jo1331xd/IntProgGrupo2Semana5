def pelicula ():

    print("="*60)
    print("Antes de comprar la un ticket a la pelicula Scary movie")
    print("="*60)

    edad=int(input("Dime tu edad "))

    if edad >=0 and edad <=14:
        print("No tienes permiso de ver la pelicula")
    elif edad >=15 and edad <=90:
        print("Permiso autorizado para reservar ")
pelicula()


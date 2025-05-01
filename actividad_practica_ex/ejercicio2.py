#tablamultiplicar
def tablamultiplicar (multi):
    num=int(input("Dame el numero que deseas multiplicar: "))
    for i in range (1,11):
        multi= num * i
        print(f"{num} x {i}={multi}")

    
tablamultiplicar(multi=0)

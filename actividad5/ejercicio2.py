sueldo=float(input("Ingrese su sueldo mensual: "))
bono= 0 

if sueldo > 3000:
    bono= sueldo * 0.1
    print(f"recibiras un bono del 10%: {bono:.2f}")
    salario= bono + sueldo
    print(f"Su salario total es de:  {salario:.2f}")
elif sueldo > 1500 and sueldo <=3000:                
    bono=sueldo * 0.05
    print(f"El bono de su sueldo será del 5%: {bono:.2f}")
    salario= bono + sueldo
    print(f"Su salario total es de:  {salario:.2f}")

elif sueldo <= 1500:
    bono
    print(f"Su sueldo no tendrá bono: {bono:.2f}")
    salario= bono + sueldo
    print(f"Su salario total es de:  {salario:.2f}")
    
lado_a=int(input("La distancia entre lado -a hacia b: "))
lado_b=int(input("La distancia entre lado -b hacia c: "))
lado_c=int(input("La distancia entre lado -c hacia b: "))


print("-"*26)
if lado_a == lado_b and lado_b == lado_c:
    print("Es un triangulo Equilátero")
elif lado_a == lado_b and lado_b != lado_c:
    print("Es un triangulo Isósceles")
elif lado_a != lado_b and lado_b != lado_c:
    print("Es un triangulo escaleno")
print("-"*26)

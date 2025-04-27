print("="*35)
print("""A continuación, seleccione la letrá que desea saber:
      - A
      - B
      - C
      - D
      - F""")
print("="*35)


calificacion=(input(""))


if calificacion=="A":
    print ("Muy buena nota")
elif calificacion=="B":
    print ("Buena nota")
elif calificacion== "C":
    print ("Nota intermedia")
elif calificacion== "D":
    print ("Mala nota")
elif calificacion == "F": 
    print ("Reprobrado")
inventario_inicial=int(input("Ingrese la cantidad de inventario inicial: "))
productos_recibidos=int(input("Ingrese la cantidad de productos recibidos: "))
productos_vendido=int(input("Ingrese la cantidad de productos vendidos: "))

suma=inventario_inicial + productos_recibidos

inventario_actual= suma - productos_vendido

print("="*35)


print(f"""El inventario inicial sería: {inventario_inicial}
productos recibido: {productos_recibidos} 
productos vendido: {productos_vendido} 
inventario final: {inventario_actual}""")


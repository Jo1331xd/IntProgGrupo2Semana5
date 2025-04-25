distancia_km= float(input("Ingrese cuantos kilometros ha recorrido en el viaje: "))
litros= float(input("Cuantos litros de gasolina ha consumido en el viaje: "))

rendimieto_kml= distancia_km / litros

precio_lt= 47.80

gasto_total= litros * precio_lt
print("="*50)
print(f"Usted recorrio una distancia en Km de {distancia_km:.2f}")
print(f"Consumio {litros:.2f}, litros")
print(f"El precio por litro es de {precio_lt:.2f}")
print(f"El rendimiento del vehiculo es de {rendimieto_kml:.2f}")
print(f"Tuvo un gasto total de {gasto_total:.2f}")
print("="*50)

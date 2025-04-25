litros=float(input("Ingrese cuantos litros se consumieron en el mes: "))
personas= float(input("¿Cuantas personas viven en su casa?: "))

mensual_por_persona= litros / personas

consumo_diario_por_persona= mensual_por_persona * 30

print("="*50)
print(f"En el mes se consumieron {litros:.2f}, litros")
print(f"En la casa viven {personas:.0f} personas")
print(f"El consumo por persona en el mes es de: {mensual_por_persona:.2f}")
print(f"El consumo diario por persona es de: {consumo_diario_por_persona:.2f}")
capital_inicial=float(input("Ingrese su capital inicial: "))
interes_anual=float(input("Ingrese la tasa de interes anual: "))
años=float(input("Ingrese la cantidad de años: "))

interes_decimal= interes_anual / 100

monto_final= ((1 + interes_decimal) ** años) * capital_inicial


interes_ganado= monto_final - capital_inicial

print(f"""Su capital inicial es de: {capital_inicial:.2f}
Tasa de interes anual: {interes_anual}
Años: {años}""")

print(f"""Su monton final es de: {monto_final:.2f}
Interes ganado: {interes_ganado:.2f}""")
      

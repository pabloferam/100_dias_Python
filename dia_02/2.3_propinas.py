# Calculadora de propinas y reparto de cuenta entre comensales
## Calculadora de propinas

# Instrucciones

# Si la cuenta fue de $150,00, dividir entre 5 personas, con 12% de propina.

# Cada persona debe pagar (150,00 / 5) * 1,12 = 33,6

# Formatee el resultado a 2 decimales = 33.60

# Por lo tanto, la parte de la cuenta total de cada uno es de $30,00 más una propina de $3,60.

print("Bienvenido a la calculadora de propinas \n")

cuenta = float(input("Introduce la cantidad de la cuenta: "))
propina = int( input("Introduce el porcentaje de propina (10%, 12%, 15%): "))
personas = int( input("Cuantos comensales hay: "))

reparto = (cuenta/personas) * (1 + (propina/100))
reparto_redondeado = "{:.2f}".format(reparto)

print(f"Cada comensal debe abonar: ${reparto_redondeado}")
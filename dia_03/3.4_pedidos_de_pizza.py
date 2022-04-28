# Instrucciones
'''
Felicidades, tienes un trabajo en Python Pizza. Su primer trabajo es construir un programa automático de pedidos de pizza.
Según el pedido de un usuario, calcule su factura final.

Pizza pequeña: $15
Pizza Mediana: $20
Pizza grande: $25

Pepperoni para Pizza Pequeña: +$2
Pepperoni para Pizza Mediana o Grande: +$3
Queso extra para pizza de cualquier tamaño: + $1
'''

print("Bienvenido a Pizzeria Python! Puedes realizar tu pedido.")

pizza = input("Cual es el tamaño de la pizza( S / M / L ): ")
peperoni = input("¿Añadimos peperonni a la pizza ( Y / N )?: ")
queso = input("¿Añadimos extra de queso ( Y / N )?: ")

precio = 0

if pizza == "S":
    precio += 15
    
elif pizza == "M":
    precio += 20
    
elif pizza == "L":
    precio += 25
    
else:
    print("Los siento, ese tamaño no es correcto")
    
if peperoni == "Y":
    if pizza == "S":
        precio += 2
    else:
        precio += 3
    
if queso == "Y":
    precio += 1
    
print(f"El precio final de su pizza es de {precio}€. Muchas gracias!!")
    

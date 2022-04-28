# Programa con numero aleatorio para elegir la cara o curuz de una moneda

import random

resultado = random.randint(1,2)
if  resultado == 1:
    moneda = "cara"
else:
    moneda = "cruz"
print(resultado)

eleccion = int(input("¿Que eliges, cara(1) o cruz(2) ? :"))

if eleccion == resultado:
    print(f"Enhorabuena, ha salido {moneda}. Has ganado")
else:
    print(f"Lo siento, ha salido {moneda}. Has perdido")
    

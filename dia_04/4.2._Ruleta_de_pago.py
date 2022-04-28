# Programa para escojer un elemento aleatorio de una lista no vacia

import random

print("¿Quien quieres que pague la factura? Te lo diré yo.")
nombres = input("Introduce el nombre de los componentes de la reunión, separados por una coma y espacio: ")

# Divide la variable en elementos para hacer una lista, dado un separador entre parentesis
lista_nombres = nombres.split(", ")

indice = len(lista_nombres) -1
num_aleatorio =random.randint(0, indice)

# Elige un elemento aleatorio de la lista
pagador = lista_nombres[num_aleatorio]
print(f"El afortunado que pagará la factura es: {pagador} !!  ")
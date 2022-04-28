# Comprobar si un numero es par o impar

print("Comprobador de numeros pares !! \n")

numero = int( input("Introduce un numero para comprobar: "))

resto = (numero % 2)

if resto != 0:
    print(f"Lo siento {numero} es impar")
else:
    print(f"Correcto !! \n{numero} es par !!")
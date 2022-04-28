#Proyecto Generador de password
import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
          's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("¡ Bienvenido al PyGenerador de Contraseñas !")
ns_letras = int(input("¿Cuantas letras quieres en la contraseña?\n"))
ns_numeros = int(input("¿Cuantos numeros quieres en la contraseña?\n"))
ns_simbolos = int(input("¿Cuantos simbolos quieres en la contraseña?\n"))


password = []
for elemento in range(1,ns_letras + 1):
    password.append(random.choice(letras))
    
for elemento in range(1, ns_numeros + 1):
    password.append(random.choice(numeros))
    
for elemento in range(1, ns_simbolos + 1):
    password.append(random.choice(simbolos))
    
string_password = "".join(password)
random.shuffle(password)
unorder_pass = "".join(password)


print(f"La contraseña generada ordenada es: {string_password}")
print(f"La contraseña aleatoria generada  es: {unorder_pass}")
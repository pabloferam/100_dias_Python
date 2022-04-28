# Suma de lo numeros pares en un rango entre 1 y 100

total = 0
for numero in range (2,101,2):
    total += numero
    
print (f"La suma total es:{total}")
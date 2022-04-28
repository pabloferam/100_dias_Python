# Calcular si un año es bisiesto.

# Si el año es divisible entre 4 y NO es divisible entre 100, es año BISIESTO
# Si el año es divisible entre 400 es BISIESTO

print("---- Calculadora de años bisiestos ---\n")
year = int(input("Introduce el año: "))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print(f"El año {year} es bisiesto")
        else:
            print(f"El año {year} NO es bisiesto")
    else:
        print(f"El año {year} es bisiesto")
    
else:
    print(f"El año {year} NO es bisiesto")
        

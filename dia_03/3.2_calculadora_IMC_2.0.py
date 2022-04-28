# Calculadora IMC 2.0 (Indicde de Masa corporal)

print("Bienvenidos a la calculadora de Indice Masa Corporal")

height = float(input("Introduce tu altura en  m: "))
weight = float(input("Introduce tu peso en kg: "))

imc = weight / (height**2)
imc_redondeado = round(imc, 2)

print(f"{weight} / ({height} x {height}) = {imc}")

if imc_redondeado < 18.5:
    print(f"Tu indice de masa corporal es {imc_redondeado}, tu estas por debajo del peso.")

elif imc_redondeado <= 24.9:
    print(f"Tu indice de masa corporal es {imc_redondeado}, tu tienes un eso normal.")

elif imc_redondeado <= 29.9:
    print(f"Tu indice de masa corporal es {imc_redondeado}, tu tiene ligeramente el peso elevado.")

elif imc_redondeado <= 34.9:
    print(f"Tu indice de masa corporal es {imc_redondeado}, tienes obesidad de grado I.")
    
elif imc_redondeado <= 39.9:
    print(f"Tu indice de masa corporal es {imc_redondeado}, tienes obesidad de grado II.")

else:
    print(f"Tu indice de masa corporal es {imc_redondeado}, tienes obesidad clínica. Deberias consultar a tu medico")
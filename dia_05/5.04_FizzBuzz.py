# Vamos a recrear el juego Fizz Buzz. Dado un rango del 1 al 100 se enumera la lista. Si el numero es divisible 
# entre 3, se dice Fizz. Si el numero es divisible entre 5, se dice Buzz.

print("Vamos a jugar a Fizz Buzz !!")

for numero in range (1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")    
    else:
        print(numero)
    
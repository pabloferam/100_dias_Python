# Para seguir el ejercicio se hará con las palabras originales TRUE y LOVE.
# Se introducen 2 nombres y se comprueba las veces que contienen las letras que forma TRUE (las decenas) y LOVE (las unidades). 
# Ranking: <10 o >90: "Tu puntaje es **x**, van juntos como la coca-cola y los mentos".
#          Entre 40 y 50 : "Su puntaje es **y**, están bien juntos".
#          Para el resto: "Su puntuación es de **z** "

from string import punctuation


print("Calculadora del Amor")
nombre_1 = input("Introduce el primer nombre: ")
nombre_2 = input("Introduce el segundo nombre: ")

pareja = nombre_1 + nombre_2
pareja = pareja.lower()

t = pareja.count("t")
r = pareja.count("r")
u = pareja.count("u")
e = pareja.count("e")

l = pareja.count("l")
o = pareja.count("o")
v = pareja.count("v")
e = pareja.count("e")

true = (t + r + u + e)
love = (l + o + v + e)
true = str(true)
love = str(love)

puntuacion = true + love
puntuacion = int(puntuacion)

if puntuacion <10 or puntuacion >90:
    print(f"Su puntuación es ** {puntuacion} **, van juntos como la Cola y los Mentos")

elif puntuacion >= 40 and puntuacion <= 50:
    print(f"Su puntuación es de ** {puntuacion} **, están bien juntos.")

else:
    print(f"Su puntuación es de ** {puntuacion} **.")
    

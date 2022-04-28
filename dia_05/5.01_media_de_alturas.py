# Obtener la media de la altura del alumnado. No se puede utilizar la funcion len() ni sum()

print("Vamos a calcular la media de las alturas del alumnado")
altura_estudiantes = input("Introduce la altura de los estudiantes en cm y separadas por un espacio:\n").split()

suma = 0
numero_alumnos = 0

for altura in altura_estudiantes:
    suma += int(altura)
    numero_alumnos += 1
    
media_altura = round(suma / numero_alumnos)

print(f"Se ha introducido la altura de {numero_alumnos} alumnos. La media de altura es de {media_altura} cm ")
    
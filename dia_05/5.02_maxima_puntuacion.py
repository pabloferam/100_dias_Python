# Obtener la máxima puntuación de una lista dada. No se puede utilizarla función max()

print("Vamos extraer la máxima puntuación de la materia")
notas = input("Introduce las notas de los estudiantes (0-100), separadas por un espacio:\n").split()
print(notas)

nota_maxima = 0

for nota in notas:
#    nota = int(nota)
    if nota > nota_maxima:
        nota_maxima = nota
        
print(f"La nota máxima de la materia es {nota_maxima}")

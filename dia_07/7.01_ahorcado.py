# Juego del ahorcado
# Podemos dar un listado de palabras o introducir una.

estado = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("Bienvenidos al juego del ahorcado")

palabra = input("Introduce la palabra secreta: ").lower()

lista_guiones = []
for caracter in palabra:
      lista_guiones.append("_")    
 
print(f"La palabra contiene {len(palabra)} letras.\n{lista_guiones}")

final_juego = False
vidas = 6
while not final_juego:
      print(estado[vidas])
      posicion= 0
      letra = input("Introduce una letra: ").lower()
      for consulta in palabra:
            posicion += 1
            if consulta == letra:
                  print(letra)
                  lista_guiones[posicion -1] = letra
           
      if letra not in palabra:
            vidas -= 1
                        
      print(lista_guiones)
      if "_" not in lista_guiones:
            final_juego = True
            print("Has ganado!!")
      if vidas == 0:
            final_juego = True
            print(estado[0])
            print("AHORCADO!!\nHas perdido.")
            print(f"La palabra correcta era {palabra.upper()}")


      

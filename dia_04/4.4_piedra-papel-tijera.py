# Juego de Piedra, papel, tijera. Jugamos con random
 
import random
piedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tijera = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("Bienvenido al mitico juego de PIEDRA, PAPEL, TIJERA !!")

mano =int(input("Elige tu jugada.| (0) Piedra | (1) Papel | (2) Tijera | :\n"))

if mano >= 3 or mano < 0 :
    print("No es una opcion válida.")
    
else:

    oponente = random.randint(0,2)

    jugada = [piedra, papel, tijera]
    print(jugada[mano])
    print("\n --------------------\n")
    print("Ordenador:")
    print(jugada[oponente])
        
    if mano == oponente:
        print("Hay un empate\n")
    elif (mano == 0 and oponente == 1) or (mano == 1 and oponente == 2) or (mano == 2 and oponente == 0):
        print("Has perdido!!\n")
    elif (mano == 0 and oponente == 2) or (mano == 1 and oponente == 0) or (mano == 2 and oponente == 1):
        print("Has ganado!!\n")

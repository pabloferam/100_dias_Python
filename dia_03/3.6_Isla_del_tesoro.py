print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bienvenido a la Isla del Tesoro.")
print("Tu misión es encontrar el tesoro.\n")

camino = input("""Te despiertas en la orilla, rodeado de restos de naufragio. Miras alrededor y ves un camino.
      Decides seguirlo. Llegas a una encrucijada. 
      ¿Tomas el camino de la (I)zquierda o el de la (D)erecha?:
      """).lower()
print("\n")

if camino == "i":
    # Continua el juego
    lago = input("""Continuas andando durante media jornada. De pronto, llegas a un claro en el que se encuentra un enorme lago.
                 Oteas y ve algo. No está demasiado lejos.
                 ¿(N)adas hacia lo que ves o (E)speras sentado en la orilla?
                 """).lower()
    print("\n")
    if lago == "e":
        # Continua el juego
        puerta = input("""Decides esperar en la orilla. Ya tuviste demasiada agua ayer. Es agua está tibia, más de lo normal, quizás
                      provenga de unas termas. Con los pies dentro de la orilla te quedas dormido del cansancio.
                      Un fuerte golpe te despierta. Estas de suerte. Es una gran madera que se puede utilizar a modo de balsa.
                      Te propulsas en dirección a lo que viste, que resulta que es una enorme isla.
                      Llegas en poco rato, o eso te ha parecido. Justo cuando comienza la vegetación hay una enorme cabaña.
                      Te acercas y parece desierta. Decides entrar.
                      Para tu sorpresa solo hay tres puertas. Una puerta (R)oja, una puerta (A)zul y otra puerta (V)erde.
                      Debes de entrar por una.
                      """).lower()
        print("\n")
        if puerta == "r":
            print("""Ya sabemos por qué el agua del lago estaba tibia. Abres la puerta y no tienes tiempo de reaccionar.
                  Los vapores de la lava te queman y tu reacción es soltarte de manos. Pierdes el equilibrio y caes a la lava.
                  GAME OVER !!\n""")
        elif puerta == "a":
            print("""Una cegadora luz azul te atrapa. Esa luz proviene de unos gigantescos Topacios que forman parte de un enorme tesoro.
                  Monedas y enseres de oro y plata, rubies, grandes joyas de piedras preciosas...
                  ¡¡ Enhorabuena, has encontrado el tesoro!!\n
                  """)
        elif puerta =="v":
            print("""Esto parece de locos. ¡¡ Hay una selva dentro de la cabaña !! Das media vuelta pero la puerta se cerro justo
                  cuando cuando pasaste. No hay pomo en este lado. Esto es un laberinto, pierdes la razón, chillas, pero no hay
                  nadie. Sucumbes y te dejas caer. Te conviertes en otro elemento de esta jungla.
                  GAME OVER !!\n""")
        else:
            print("""Parece que has intentado algo diferente. ¿Has intentado salir de la cabaña? Aqui no se admite la vuelta atras.
                  Un rayo de Zeus cáe sobre ti.
                  GAME OVER !!\n
                  """)    
        print("\n")
        
        
    else:
        print("""
              Fijas bien la vista y puedes verificar que hay una isla. Decides nadar hacia ella, realmente esta cerca.
              Tras unas pocas brazadas en el agua, notas que algo roza tu pie. Se te acelera el pulso y te pones muy nervioso.
              Sigues nadando muy rápido y la orilla está justo ahí. En ese justo momento algo te atrapa los pies y
              te arrastra a las profundidades del lago. Sucumbes en el fondo.
              GAME OVER !!\n""")
    
else:
    print("""Empiezas a caminar y justo cuando llevas 2 metros,sucumbes en unas arenas movedizas.
        GAME OVER !!\n""")
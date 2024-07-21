#Proyecto 4. Crea un juego donde el usuario debera adivinar un numero aleatorio
from random import randint

print("Bienvenido a mi juego! He pensando en un numero del 1 al 100. Crees poder adivinarlo?")
intentos = 8
numeroElegido = randint(1,100)

while intentos > 0:
    try:
        numeroUsuario = int(input("Ingrese el numero que pienses que sea: "))
    except ValueError as e:
        print("Dato no valido. Intente de nuevo")
        continue

    if numeroUsuario < 0 or numeroUsuario > 100:
        print("Recuerda que el numero es entre 1 y 100. Intenta de nuevo")
    elif numeroUsuario < numeroElegido:
        print("Numero equivocado D:\nEl numero ingresado es menor al elegido.")
    elif numeroUsuario > numeroElegido:
        print("Numero equivocado D:\nEl numero ingresado es mayor al elegido.")
    else:
        print(f"Felicidades! has acertado. El numero era: {numeroElegido}")
        print(f"Finalizaste el juego con {intentos} {' intento restante' if intentos == 1 else ' intentos restantes'}")
        break
    intentos -= 1
    print(f"Intentos restantes: {intentos}\n")

print("Fin del juego")
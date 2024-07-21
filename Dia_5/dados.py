from random import *

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)

    return dado1,dado2

def evaluar_jugada(dado1,dado2):
    resultado = dado1+dado2
    mensaje = f"La suma de tus dados es {resultado}."
    if resultado <= 6:
        return mensaje + " Lamentable"
    elif resultado > 6 and resultado < 10:
        return mensaje + " Tienes buenas chances"
    elif resultado >= 10:
        return mensaje + " Parece una jugada ganadora"

print(evaluar_jugada(*lanzar_dados()))
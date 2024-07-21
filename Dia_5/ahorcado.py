from random import choice
def main():
    palabras = ["Carro","Ferrocarril","Sonriente","Audifonos","Computadora","Avistamiento","Campana","Colectivo","Alegria",
                "Teclado","Pelota","Adhesivo","Cortinas","Sombrero","Monitor","Libertad","Cancion","Final","Perimetro","Panadero"]
    
    palabraAdivinar = choice(palabras).lower()
    print("Bienvenido! al juego del ahorcado. Adivina la palabra antes de perder todas tus vidas para ganar!\n")
    vidas = 6
    palabra_incompleta = iniciarJuego(palabraAdivinar)

    while vidas > 0:
        palabra_formandose = palabra_incompleta
        if palabra_formandose == palabraAdivinar:
            break
        print(f"Palabra Adivinar: {palabra_formandose}")
        caracter = input("Ingresa una letra: ")
        if validarCaracter(caracter,palabraAdivinar):
            palabra_incompleta = llenarPalabraIncompleta(caracter,palabra_formandose,palabraAdivinar)
            print(f"\nBien hecho. Adivinaste algunos caracteres!")
        else:
            print(f"\nLastima! La letra '{caracter}' no se encuentra en la palabra. Intenta de nuevo")
            vidas -= 1
            print(f"Vidas restantes: {vidas}")
    if vidas == 0:
        print(f"\nHas perdido :(\nLa palabra ha adivinar era: {palabraAdivinar}")
    else:
        print(f"\nFelicidades has ganado el juego!. \nCon {vidas} vidas {'restante' if vidas == 1 else 'restantes'}")
    print("Fin del juego")

def iniciarJuego(palabra):
    lista_incompleta = ['_' for _ in palabra]
    palabra_incompleta = ''.join(lista_incompleta)
    return palabra_incompleta

def validarCaracter(caracter,palabra):
     return caracter in palabra

def llenarPalabraIncompleta(caracter,palabra_formandose,palabraAdivinar):
    palabra_incompleta = list(palabra_formandose)
    for index,carac in enumerate(palabraAdivinar):
        if carac == caracter:
            palabra_incompleta[index] = caracter

    palabra_incompleta = ''.join(palabra_incompleta)
    return palabra_incompleta

main()
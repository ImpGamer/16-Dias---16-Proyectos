import pygame
from Jugador import *
import math
from pygame import mixer #Trabajar con sonido
#Inicializar pygame
pygame.init()
ALTO = 600
ANCHO = 800
puntaje =0
VELOCIDAD_ENEMIGOS = 0.4
fuente = pygame.font.Font("freesansbold.ttf",20)
texto_pos = {
    'x':600,
    'y':10
}

#Iniciar la pantalla
pantalla = pygame.display.set_mode((ANCHO,ALTO))
#Titulo e icono del juego
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("./Dia_10/assets/ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("./Dia_10/assets/fondo.jpg")
enemigos = []

#Creacion del objeto del jugador
"""
Operacion aritmetica para calcular la mitad de la pantalla con el jugador
(ANCHO/2)-(ANCHO_IMAGEN/2)
"""
jugador = Jugador(x=(ANCHO/2)-32,y=ALTO-100)
laser = Laser(jugador.x+16,jugador.y-20)
#Musica
mixer.music.load("./Dia_10/assets/MusicaFondo.mp3")
mixer.music.set_volume(0.5)
mixer.music.play(-1)

ejecutando = True

for i in range(0,11):
    enemigos.append(Enemigo(0,0,1,VELOCIDAD_ENEMIGOS))
    enemigos[i].generar()

def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_2-x_1,2)+math.pow(y_2-y_1,2))
    if distancia < 27:
        return True
    return False

def mostrar_puntaje():
    texto = fuente.render(f"Puntaje Actual: {puntaje}",True,(255,255,255))
    pantalla.blit(texto,(texto_pos["x"],texto_pos["y"]))

def terminar_juego():
    final = pygame.font.Font("freesansbold.ttf",42)
    fuente_final = final.render(f"JUEGO TERMINADO.",True,(255,0,0))
    pantalla.blit(fuente_final,(60,200))

#Loop del juego general (funcion update)
while ejecutando:
    pantalla.blit(fondo,(0,0))
    jugador.validarPosiciones(ANCHO,ALTO)
        
    #Color de la pantalla
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        jugador.disparar(evento,laser=laser)

    if laser.visible:
        pantalla.blit(laser.image,(laser.x,laser.y))
        laser.mover()
    else:
        #Seguimiento de la bala al jugador
        laser.x = jugador.x+16
        laser.y = jugador.y-20
    keys = pygame.key.get_pressed()
    jugador.mover(keys)
    #Instanciacion de objetos dentro del plano
    pantalla.blit(jugador.image,(jugador.x,jugador.y))
    mostrar_puntaje()
    for enemigo in enemigos:
        pantalla.blit(enemigo.image,(enemigo.x,enemigo.y))
        enemigo.mover(ANCHO)
        if enemigo.y > 400:
            terminar_juego()
            break
        #Validar si hay colisiones entre una bala y un enemigo
        if hay_colision(enemigo.x,enemigo.y,laser.x,laser.y):
            golpe = mixer.Sound("./Dia_10/assets/Golpe.mp3")
            golpe.play()
            laser.visible = False
            puntaje += 5
            enemigo.generar()
    #Actualizacion de la pantalla
    pygame.display.update()

pygame.quit()
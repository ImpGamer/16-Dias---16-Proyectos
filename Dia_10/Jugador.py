import pygame
import random
from pygame import mixer
class Jugador:
    def __init__(self,x,y):
        self.image = pygame.image.load("./Dia_10/assets/cohete.png")
        self.y = y
        self.x = x

    def mover(self,keys):
        if keys[pygame.K_a]:
            self.x -= 0.5
        elif keys[pygame.K_d]:
            self.x += 0.5
    
    def validarPosiciones(self,ANCHO,ALTO):
        if self.x > (ANCHO-64):
            self.x = ANCHO-64
        elif self.x < 1:
            self.x = 1
    
    def disparar(self,event,laser):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                disparo = mixer.Sound("./Dia_10/assets/disparo.mp3")
                disparo.play()
                laser.visible = True
                

class Enemigo(Jugador):
    def __init__(self,x, y,direccion,velocidad):
        super().__init__(x, y)
        self.image = pygame.image.load("./Dia_10/assets/enemigo.png")
        #Direccion. Derecha = 1, Izquierda = 2
        self.direccion = direccion
        self.velocidad = velocidad

    def generar(self):
        self.x = random.randint(1,736)
        self.y = random.randint(0,256)
    
    def mover(self,ANCHO):
        if self.x > (ANCHO-64):
            self.direccion = 2
            self.y += 20
            self.x = ANCHO-65
        elif self.x < 1:
            self.direccion = 1
            self.y += 20
            self.x = 1

        if self.direccion == 1:
            self.x += self.velocidad
        else:
            self.x -= self.velocidad

class Laser(Jugador):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("./Dia_10/assets/bala.png")
        self.visible = False
    
    def mover(self):
        if self.visible:
            self.y -= 1
        if self.y < 0:
            self.visible = False
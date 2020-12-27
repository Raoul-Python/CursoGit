import pygame, sys


class Game:
    #lista de corredores
    runners = []

    __startLine = 20
    __finishLine = 620

    def __init__(self):
        self.__pantalla = pygame.display.set_mode((640, 480))#Creo pantalla como atributo de la clase

"""
        #Fondo de pantalla
        self.__pantalla.fill((0,255,0))"""

        #Cargamos una imagen
        self.__imagenFondo = pygame.image.load("D:\dragonalnce.jpg")

        #Titulo de la pantalla
        pygame.display.set_caption("Tortugas en Pygame")


if __name__ == "__main__":
    juego = Game()



"""
width = 640
height = 480

#Creo la pantalla de mi juego

pantalla = pygame.display.set_mode((width, height))#El argumento de la función es una tupla
#Le pongo un fondo naranja a la pantalla con una tupla de 3 valores
pantalla.fill((246,147,48))

#Titulo de mi juego
pygame.display.set_caption("Ciclo bázico de pygame")

pygame.init()

#Iniciamos el ciclo (re)pintar pantalla-manejar eventos- modificar pantalla
gameOver = False

while not gameOver:
    #Cogemos eventos del buffer de eventos de pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    #Refrescamos la pantalla
    pygame.display.update()

pygame.quit()
sys.exit()

"""
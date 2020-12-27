import pygame
import sys

class Game:

    corredores = []

    def __init__(self):
        #Creamos la pantalla
        self.__screen = pygame.display.set_mode((640, 480)) #Indicamos tammaño de la pantalla en una tupla

        #Título de la pantsalla
        pygame.display.set_caption("Competición de Tortugas")

        #Cargamos imagen de fondo con un atributo
        self.background = pygame.image.load("D:\pistadecarreras.jpg")


        self.runner = pygame.image.load("D:\balonAmarillo2.jpg")

    
    def competir(self):

        x = 0

        hayGanador = False

        while not hayGanador:
            #Comprobación de los eventos....pygame está escuchando y cargando eventos continuamente
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.__screen.blit(self.background, (0,0)) #Vuelcas el contenido de la memoria en la coordenadas 0,0
            self.__screen.blit(self.runner, (x, 240))
            pygame.display.flip() #Refresca la pantalla

            x += 3

            if x >= 250:
                hayGanador = True


        pygame.quit()
        sys.exit()


if __name__ == "__main__":

    pygame.init()#Se pone a escuchar eventos
    juego = Game()

    juego.competir()



    input()

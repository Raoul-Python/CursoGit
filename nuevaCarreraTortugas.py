import pygame, sys

class Game:

    runners = []
    __startLine = 20
    __finishLine = 620


    def __init__(self):

        #Creación de la pantalla
        self.__screen = pygame.display.set_mode((640, 480))
        #Cargo imagen de fondo de pantalla
        self.__background = pygame.image.load("D:\pistadecarreras.jpg")
        #Título de la pantalla
        pygame.display.set_caption("En un país de la Mancha.....")

    def competir(self):

        gameOver = False

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True

            #Pintamos la pantalla
            self.__screen.blit(self.__background, (0,0))#La función blit me vuelca la imagen de la variable 
            #background en la pantalla en las coordenadas 0,0.

            #Ahora refrescamos la pantalla
            pygame.display.flip()

        pygame.quit()
        sys.exit()










if __name__ == "__main__":

    juego = Game()

    pygame.font.init()

    juego.competir()


    

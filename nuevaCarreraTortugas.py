import pygame, sys

class Game:

    runners = []
    __startLine = 20
    __finishLine = 620


    def __init__(self):

        #Creación de la pantalla
        self.__screen = pygame.display.set_mode((640, 480))
        #Cargo imagen de fondo de pantalla
        self.__background = pygame.image.load("D:\dragonlance.png")
        #Título de la pantalla
        pygame.display.set_caption("En un país de la Mancha.....")


if __name__ == "__main__":

    juego = Game()

    

    
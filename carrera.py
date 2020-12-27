import turtle
import random


class Circuito:

    corredores = []

    __posStartY = (-30, -10, 10, 30) #Lo meto en una tupla
    __colorTurtle = ("blue", "orange", "green", "red")

    def __init__(self, width , height):
        self.__screen = turtle.Screen() #Atributo de la Clase Circuito
        self.__screen.setup(width, height)
        self.__screen.bgcolor("lightgray")
        self.__startLine = -width / 2 + 20 #Punto inicial del recorrido en X. 
        self.__finishLine = width / 2 - 20 #Punto final del recorrido en  X
        
        self.__createRunners()



    def __createRunners(self):

        #Creamos las 4 tortugas corredoras
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.shape("turtle")
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, self.__posStartY[i])
            


            self.corredores.append(new_turtle)#Y me la añade a la lista corredores


    def competir(self):

        hayGanador = False

        while not hayGanador:

            for tortuga in self.corredores:

                avance = random.randint(1,6)

                tortuga.fd(avance)

                if tortuga.position()[0] >= self.__finishLine:

                    if tortuga.color()[0] == "blue":#Es una tupla (color de tortuga, color de línea)
                        tono = "AZUL"
                    
                    elif tortuga.color()[0] == "red":
                        tono = "ROJO"
                    
                    elif tortuga.color()[0] == "orange":
                        tono = "NARANJA"

                    elif tortuga.color()[0] == "green":
                        tono = "VERDE"

                    hayGanador = True

                    print("La tortuga de color {} ha ganado.".format(tono))

                    break








if __name__=="__main__":
    circuito = Circuito(640,480)

    circuito.competir()

    input()












        



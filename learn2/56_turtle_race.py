import turtle #performs 2d graphic operations
import time

#definiowanie rozmiaru okna
WIDTH,HEIGHT = 500, 500 # capital letters bo to wartości constant, nie zmienią się przez cały czas trwania programu
COLORS = ['red', 'blue', 'orange', 'yellow', 'green' , 'brown' , 'cyan']


def get_number_of_racers():
    racers = 0
    while True:
        racers=input("Enter the number of racers(2-10): ")
        if racers.isdigit():
            racers= int(racers)
            #break
        else:
            print("Input is not numeric. Try Again!")
            continue
        if 2<= racers <= 10:
            return racers
        else:
            print("Input in not from 2-10 range")
            # continue  #nie trzeba dawać tu continue bo po tym statemencie nic nie ma


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing!')


racers= get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
racer.speed(2)
racer.shape('turtle')
reacer.color('green')
racer.forward(100) #ilość pikseli o które obiekt ma się przesunać
racer.left(90) #przy skręcie w lewo i prawo podaje się kąt jako argument funkcji
racer.forward(100)
racer.left(90)
racer.backward(100)


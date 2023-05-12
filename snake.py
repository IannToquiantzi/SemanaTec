"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *
from freegames import square, vector
import random

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

#Funcion para cambiar la direccion de movimiento de la comida:
def change_food():
    #Lista de vectores que corresponde a la direccion
    food_list = [vector(0,10), vector(0,-10), vector(10,0), vector(-10,0)] 
    #Eleccion al azar de la direccion de la comida
    aim_food = random.choice(food_list)
    #Ciclo para elegir otra direccion en caso de que la anterior salga de los limites:
    while -200 > aim_food.x or  aim_food.x > 190 and -200 > aim_food.y or aim_food.y > 190: 
        aim_food = random.choice(food_list) 
    return aim_food   
        
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    #Funcion para mover la comida de posicion:
    food.move(change_food()) 

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
change_food()
move()
done()

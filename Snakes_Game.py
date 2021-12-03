from turtle import *
from random import randrange
from freegames import square, vector
import time
import matplotlib.pyplot as plt
import numpy as np


food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

#for recording the length of the snake
length = []
aim_x_list = []
aim_y_list = []
food_x_position =[]
food_y_position = []


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim_x_list.append(x)
    aim.y = y
    aim_y_list.append(y)

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        length.append(len(snake))
        food.x = randrange(-15, 15) * 10
        food_x_position.append(food.x)
        food.y = randrange(-15, 15) * 10
        food_y_position.append(food.y)
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

print(length)
print(aim_x_list)
print(aim_y_list)
print(food_x_position)
print(food_y_position)
xpoints = np.array(food_x_position)
ypoints = np.array(food_y_position)

plt.plot(xpoints, ypoints, marker = "*")
plt.title("Food position points summarization")
plt.show()

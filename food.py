from turtle import Turtle
from random import randint, randrange
FOOD_SIZE = 20


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("black")
        self.penup()
        self.make_move()

    def make_move(self):
        x = randrange(-280.00, 280.00, FOOD_SIZE)
        y = randrange(-280.00, 280.00, FOOD_SIZE)
        self.goto(x, y)




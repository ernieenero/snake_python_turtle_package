from turtle import Turtle
TURTLE_SIZE = 20
RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270
POSITION = [(0, 0), (-20, 0), (-40, 0)]
class Snake:
    def __init__(self):
        self.snake_object = []
        self.x_pos = 0
        self.add()
        self.head = self.snake_object[0]

    def add(self):
        for n in range(len(POSITION)):
            self.create(POSITION[n])

    def create(self, position):
        snake = Turtle()
        snake.shape("square")
        snake.penup()
        snake.speed("fastest")
        snake.color("black")
        snake.goto(position)
        self.snake_object.append(snake)

    def moves(self):
        for n in range(len(self.snake_object) - 1, 0, -1):
            temp = self.snake_object[n - 1].position()
            self.snake_object[n].setpos(temp)
        self.snake_object[0].forward(TURTLE_SIZE)

    def again(self):
        while len(self.snake_object) > 3:
            self.snake_object[-1].goto(400, 0)
            self.snake_object.pop(-1)
        for index in range(len(POSITION)):
            self.snake_object[index].goto(POSITION[index])
        self.snake_object[0].setheading(0)

    def ewan(self):
        self.create(self.snake_object[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
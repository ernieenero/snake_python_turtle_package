from turtle import Screen
import time
from food import Food
from snake import Snake
from scoring import Score
XCOR = 350
YCOR = -350
screen = Screen()
screen.tracer(0)
foods = Food()
scores = Score()
screen.setup(width=700, height=690)
screen.title("Snake 3310")
screen.bgcolor("goldenrod")
game = Snake()

screen.listen()


def game_start():
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)

        # Display the score
        scores.display()

        #Key for Movement
        screen.onkey(fun=game.up, key="w")
        screen.onkey(fun=game.down, key="s")
        screen.onkey(fun=game.right, key="d")
        screen.onkey(fun=game.left, key="a")

        #Keeps the Snake Moving
        game.moves()

        #Check Collision with Foods
        if game.head.distance(foods) < 10:
            foods.make_move()
            scores.add_score()
            game.ewan()

        #Wall Collision
        if game.head.xcor() >= XCOR or game.head.xcor() <= YCOR or game.head.ycor() >= XCOR or game.head.ycor() <= YCOR:
            scores.game_over()
            # game.again()
            game_on = False

        #Tale Collision
        for segment in game.snake_object[1:]:
            if game.head.distance(segment) < 15:
                game_on = False
                scores.game_over()
    game.again()
    scores.reset()

#Start of the Game
scores.enter()
screen.onkey(fun=game_start, key="space")

screen.exitonclick()

from turtle import Turtle
TURTLE_SIZE = 20
FONT = ("Courier", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        with open("scores.txt") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(x=0, y=265)

    def add_score(self):
        self.score += 10

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER\nPress Space to Play Again", move=False, align="center", font=FONT)

    def display(self):
        self.clear()
        self.goto(-265, 265)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=FONT)
        self.goto(100, 265)
        self.write(arg=f"High Score: {self.high_score}", move=False, align="center", font=FONT)

    def enter(self):
        self.write(arg=f'🐍 Enter Space To Play 🐍', move=False, align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("scores.txt", mode="w") as file:
            file.write(str(self.high_score))
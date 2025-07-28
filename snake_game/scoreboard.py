from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}   Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode="w") as update:
                update.write(f"{self.highest_score}")
        self.score = 0
        self.update_scoreboard()

    def increase(self):
        self.score += 1
        self.update_scoreboard()

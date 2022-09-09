FONT = ("Courier", 20, "normal")
from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.level = 0
        self.board = Turtle()
        self.board.color("black")
        self.board.penup()
        self.board.hideturtle()
        self.board.goto(-200, 250)
        self.board.write(f"Level: {self.level}", align="center", font=FONT)

    def refresh(self):
        self.board.clear()
        self.board.write(f"Leve: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.board.home()
        self.board.write("Game Over", align="center", font=FONT)

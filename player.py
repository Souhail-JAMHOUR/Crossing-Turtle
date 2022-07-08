from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        current_y = self.ycor()
        new_position = 0, current_y + MOVE_DISTANCE
        self.goto(new_position)

    def refresh(self):
        self.goto(STARTING_POSITION)


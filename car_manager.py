from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = list()
        self.freq = 6

    def creat_cars(self):
        space = random.randint(1, self.freq)
        if space == 1:
            new_car = Turtle("square")
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=2, stretch_len=1)
            y_position = random.randint(-200, 300)
            new_car.position = (350, y_position)
            new_car.goto(new_car.position)
            new_car.color(random.choice(COLORS))
            new_car.setheading(90)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - MOVE_INCREMENT
            car.goto(new_x, car.ycor())

    def level_up(self):
        if self.freq > 1:
            self.freq -= 1



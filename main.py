import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
new_player = Player()
new_car_manager = CarManager()
board = Scoreboard()
screen.listen()
screen.onkeypress(key="Up", fun=new_player.move)
game_speed = 0.1
game_is_on = True
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    new_car_manager.creat_cars()
    new_car_manager.move_cars()
    if new_player.ycor() >= 300:
        board.level_up()
        game_speed *= 0.9
        new_car_manager.level_up()
        new_player.refresh()
    for car in new_car_manager.cars:
        if new_player.distance(car) < 25:
            game_is_on = False
            board.game_over()
            print("bye")


screen.exitonclick()


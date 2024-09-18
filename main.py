from turtle import Screen
from avatar import Avatar
from scoreboard import Scoreboard
from cars import Cars
import time

turtle = Avatar()
scoreboard = Scoreboard()
cars = Cars()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Crossing')
screen.listen()

screen.onkey(turtle.move_up, 'Up')

is_game_on = True

game_speed = 0.1

while is_game_on:
    time.sleep(game_speed)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # detect hit finish line
    if turtle.ycor() > 280:
        scoreboard.increase_level()
        turtle.reset_position()
        game_speed *= 0.9

    '''
    detect if we are hit by a car, changing the distance based on the position of the turtle
    compared to the car
    '''
    for car in cars.cars:
        d = 30 if car.xcor() < -20 else 20

        if car.distance(turtle) < d:
            is_game_on = False
            scoreboard.game_over()



screen.exitonclick()
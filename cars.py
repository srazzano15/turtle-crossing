from turtle import Turtle
from random import randint

COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
DEFAULT_X_RANGE = (300, 350)
DEFAULT_Y_RANGE = (-250, 250)

class Cars:

    def __init__(self):
        self.cars = []

    def create_car(self, x_range=DEFAULT_X_RANGE, y_range=DEFAULT_Y_RANGE):
        dice_roll = randint(1, 6)
        if dice_roll == 1:
            car = Turtle(shape='square')
            car.penup()
            car.speed('fastest')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(COLORS[randint(0, 5)])
            # left side of screen is
            rand_x = randint(x_range[0], x_range[1])
            rand_y = randint(y_range[0], y_range[1])
            car.teleport(rand_x, rand_y)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(10)
            #if car.xcor() < -320:
               # self.reset_car_position(car)

    def reset_car_position(self, car):
        rand_x = randint(DEFAULT_X_RANGE[0], DEFAULT_X_RANGE[1])
        rand_y = randint(DEFAULT_Y_RANGE[0], DEFAULT_Y_RANGE[1])
        car.teleport(rand_x, rand_y)
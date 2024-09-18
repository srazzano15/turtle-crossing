from turtle import Turtle

class Avatar(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.speed('fastest')
        self.setheading(90)
        self.reset_position()

    def move_up(self):
        self.fd(20)

    def reset_position(self):
        self.teleport(0, -280)
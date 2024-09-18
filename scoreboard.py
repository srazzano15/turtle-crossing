from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.teleport(-210, 260)
        self.write(f'Level: {self.level}', align=ALIGNMENT, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.teleport(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.goto(0,250)
        self.color("white")
        
    
    def write_score(self):
        self.score+=1
        self.clear()
        self.write(arg=f"Score: {self.score}",align="center")

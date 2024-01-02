import random
from turtle import Turtle

class Food(Turtle):

    def __init__(self): 
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.relocate_food()
        
    def relocate_food(self):
        random_x,random_y = random.randint(-12,12)*20,random.randint(-12,12)*20
        self.goto(random_x,random_y)
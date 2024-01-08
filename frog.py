from turtle import Turtle
import random
DIRECTIONS = [0,90,180,270]

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed("fastest")
        
    def move(self):
        random_direction = random.choice(DIRECTIONS)
        self.left(random_direction)
        self.forward(20)
         
    def relocate_frog(self):
        random_x,random_y = random.randint(-12,12)*20,random.randint(-12,12)*20
        self.goto(random_x,random_y)

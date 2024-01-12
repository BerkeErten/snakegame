from turtle import Turtle
import random
DIRECTIONS = [0,90,180,270]

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed("slowest")
        
    def move(self,need_esc: bool, esc_heading: str =None):
        
        #Escaping walls
        if need_esc is True:
            if esc_heading == "n":
                print(f"Escaping from {esc_heading}")
                self.setheading(90)
                self.forward(40)
            elif esc_heading == "s":
                print(f"Escaping from {esc_heading}")
                self.setheading(270)
                self.forward(40)
            elif esc_heading == "e":
                print(f"Escaping from {esc_heading}")
                self.setheading(0)
                self.forward(40)
            elif esc_heading == "w":
                print(f"Escaping from {esc_heading}")
                self.setheading(180)
                self.forward(40)
        #Random movement
        
        random_direction = random.choice(DIRECTIONS)

        self.setheading(random_direction)
        self.forward(20)
    
             
    
    def relocate_frog(self):
        random_x,random_y = random.randint(-12,12)*20,random.randint(-12,12)*20
        self.goto(random_x,random_y)

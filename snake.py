from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]

class Snake:
    
    def __init__(self):
        self.segments = []
        self.createsnake()

    def createsnake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("circle")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    
    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)
    
    def grow_snake(self):
        new_butt= Turtle("circle")
        new_butt.goto(self.segments[-1].xcor(),self.segments[-1].ycor())
        new_butt.color("white")
        new_butt.penup()
        self.segments.append(new_butt)

    def turn_snake_left(self):  
        self.segments[0].left(90)


    def turn_snake_right(self):  
        self.segments[0].right(90)

    def get_snake_segments(self):
        return self.segments
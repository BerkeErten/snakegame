import time
from turtle import Screen
from snake import Snake
from food import Food
from frog import Frog
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


s1 = Snake()
snake_head = s1.get_snake_segments()[0]
food = Food()
frog_food = Frog()
score = Scoreboard()
score.write_score()
screen.listen()
screen.onkeypress(key='a',fun=s1.turn_snake_left)
screen.onkeypress(key='d',fun=s1.turn_snake_right)
screen.onkeypress(key='f',fun=s1.grow_snake)
game_in_on=True

while game_in_on:
    screen.update()
    s1.move_snake()
    frog_food.move()
    
    
    
    for i in range(1,len(s1.get_snake_segments())):
        if s1.get_snake_segments()[0].distance(s1.get_snake_segments()[i])<15:
            game_in_on = False
            print("GAME OVER")

        
    
    if food.distance(snake_head)<10:
        food.relocate_food()
        score.write_score()
        s1.grow_snake()
        
    if frog_food.distance(snake_head)<10:
        frog_food.relocate_frog()
        score.write_score()
        score.write_score()
        s1.grow_snake()
        s1.grow_snake()
    

    if snake_head.xcor() > 300 or snake_head.xcor() < -300:
        snake_head.goto(-snake_head.xcor(),snake_head.ycor())
    
    if snake_head.ycor() > 300 or snake_head.ycor() < -300:
        snake_head.goto(snake_head.xcor(),-snake_head.ycor())

    if frog_food.xcor() > 250 or frog_food.xcor() < -250:
        frog_food.goto(-frog_food.xcor(),frog_food.ycor())
    
    if frog_food.ycor() > 250 or frog_food.ycor() <-250:
        frog_food.goto(frog_food.xcor(),-frog_food.ycor())

    time.sleep(0.1)
    












screen.exitonclick()
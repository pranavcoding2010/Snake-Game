import turtle
import random
import time 
screen = turtle.Screen()
screen.title('Snake Game')
screen.setup(width=700,height=700)
screen.tracer(0)
turtle.bgcolor('red')
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-315,250)
turtle.pendown()
turtle.color('yellow')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.penup()
turtle.hideturtle()
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('black')
snake.penup()
snake.goto(0,0)
snake.direction='stop'
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('circle')
fruit.color('yellow')
fruit.penup()
fruit.goto(30,30)
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color('blue')
scoring.penup()
scoring.goto(0,300)
scoring.hideturtle()
scoring.write('score:',align = 'center',font = ('courier',24,'bold'))

def snake_game_up():
    if snake.direction != "down":
        snake.direction = "up"

def snake_game_down():
    if snake.direction != "up":
        snake.direction = "down"
    
def snake_game_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_game_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction=="up":
        y=snake.ycor()
        snake.sety(y+20)

    if snake.direction=="down":
        y=snake.ycor()
        snake.sety(y-20)

    if snake.direction=="left":
        x=snake.xcor()
        snake.setx(x-20)        

    if snake.direction=="right":
        x=snake.xcor()
        snake.setx(x+20)         

screen.listen()
screen.onkeypress(snake_game_up,'Up')
screen.onkeypress(snake_game_down,'Down')
screen.onkeypress(snake_game_left,'Left')
screen.onkeypress(snake_game_right,'Right')
old_fruit=[]

score=0
delay=0.1
while True :
    screen.update()
    if snake.distance(fruit)<20:
        x=random.randint(-290,270)
        y=random.randint(-240,240)
        fruit.goto(x,y)
        scoring.clear()
        score+=1
        scoring.write('score:{}'.format(score),align = 'center',font = ('courier',24,'bold'))
        delay-=0.001
        new_fruit=turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('circle')
        new_fruit.color('yellow')
        new_fruit.penup()
        old_fruit.append(new_fruit)
    for index in range (len(old_fruit)-1,0,-1):
         a = old_fruit[index-1].xcor()
         b = old_fruit[index-1].ycor()
         old_fruit[index].goto(a,b)
    if len(old_fruit)>0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a,b)

    snake_move()
    if snake.xcor()>280 or snake.xcor()<-300 or snake.ycor()>240 or snake.ycor()<-250:
        time.sleep(1)
        screen.clear()
        screen.bgcolor('orange')
        scoring.goto(0,0)
        scoring.write('Game over\n your score is {}'.format(score),align = 'center',font = ('courier',24,'bold'))
    for food in old_fruit:
        if food.distance(snake)<20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor('orange')
            scoring.goto(0,0)
            scoring.write('Game over\n your score is {}'.format(score),align = 'center',font = ('courier',24,'bold'))


    time.sleep(0.1)
turtle.Terminator()

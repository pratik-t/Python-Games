import turtle
import time
from snake_mechanics import Snake,Food,box, Scoreboard

sc= turtle.Screen()
sc.bgcolor("black")
sc.screensize()
sc.setup(width=1.0, height=1.0)
canvas= sc.getcanvas()
root= canvas.winfo_toplevel()
root.overrideredirect(1)

sc.title("SNAKE!")
sc.tracer(0)

box()
s= Snake()
f= Food()
score= Scoreboard()
game= True

paused= True

def pause():
    global paused
    if paused==True:
        sc.listen()
        sc.onkey(s.up, "Up")
        sc.onkey(s.down, "Down")
        sc.onkey(s.left, "Left")
        sc.onkey(s.right, "Right")
        paused= False
    else:
        paused=True

def exit():
    global game
    global sc
    sc.bye()

sc.listen()
sc.onkey(pause, "space")
sc.onkey(exit, "Escape")

speed= 0.13
level= 1

while game:

    if not paused:

        time.sleep(speed)
        sc.update()
        s.move()
        if s.head.distance(f)<15:
            f.refresh(s.snake)
            points= score.update_score()
            s.extend()

            if points%10==0 and level==1:
                speed=0.1
                level= 2
            elif points%20==0 and level==2:
                speed= 0.08
                level= 3
            elif points%30==0 and level==3:
                speed= 0.05

        if s.head.xcor()>310 or s.head.xcor()<-310or s.head.ycor()>310 or s.head.ycor()<-310:
            game= False
            score.endgame()

        for body in s.snake[1:]:
            if s.head.distance(body)<10:
                game= False
                score.endgame()

    else:

        sc.update()

sc.exitonclick()

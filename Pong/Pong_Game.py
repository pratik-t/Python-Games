import turtle
import time
from Pong_mechanics import Paddle,Ball,Score,box

sc= turtle.Screen()
sc.bgcolor('black')
sc.setup(height=600, width=800)
sc.title("Pong!")
sc.tracer(0)

p1= Paddle(-350,0)
ai= Paddle(350,0)
b= Ball()

sc.onkeypress(p1.up, "Up")
sc.onkeypress(p1.down, "Down")
sc.listen()
box()
sc.update()
game = True

speed= 0.01

s= Score()
while game:

    sc.update()
    time.sleep(speed)
    b.move()

    if b.ycor()>280 or b.ycor()<-280:
        b.wbounce()

    if (b.xcor()==330 and abs(b.ycor()-ai.ycor())<=50) or (b.xcor()==-330 and \
                        abs(b.ycor()-p1.ycor())<=50):
        b.pbounce()

    if (b.xcor()<-330 and b.xcor()>-360 and abs(b.ycor()-p1.ycor())==55)or(b.xcor()>330 \
                        and b.xcor()<360 and abs(b.ycor()-ai.ycor())==55):
        b.wbounce()

    if b.xcor()>380:
        b.miss()
        speed= 0.01
        s.update(1)
        ai.goto(350,0)
        time.sleep(1)

    if b.xcor()<-380:
        b.miss()
        speed= 0.01
        ai.goto(350,0)
        s.update(2)
        time.sleep(1)

    if b.xcor()>-50:
        ai.follow(b)
    else:
        ai.ai_move()


sc.exitonclick()

import turtle
import random

def box():
    t= turtle.Turtle(); t.color('white'); t.ht()
    t.penup(); t.goto(0,-300); t.setheading(90);
    t.pendown();t.speed('fastest');t.fd(600)

class Paddle(turtle.Turtle):

    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.color('white'); self.penup(); self.speed('fastest')
        self.shapesize(1,5);self.setheading(90)
        self.goto(x,y)
        self.y_iter= 5

    def up(self):
        if self.ycor()<250:
            self.fd(20)

    def down(self):
        if self.ycor()>-250:
            self.bk(20)

    def bounce(self):
        self.y_iter*=-1

    def ai_move(self):
        newy=self.ycor()+self.y_iter
        self.goto(350,newy)

        if self.ycor()>240 or self.ycor()<-240:
            self.bounce()

    def ai_up(self,rate):
        if self.ycor()<250:
            self.fd(rate)

    def ai_down(self,rate):
        if self.ycor()>-250:
            self.bk(rate)

    def follow(self,b):

        rate= random.choice([4.8,4.9,5])
        if b.y_iter>0:
            if b.ycor()>self.ycor():
                if self.distance(b)>50:
                    self.ai_up(rate)
            else:
                if self.distance(b)>50:
                    self.ai_down(rate)

        elif b.y_iter<0:
            if b.ycor()<self.ycor():
                if self.distance(b)>50:
                    self.ai_down(rate)
            else:
                if self.distance(b)>50:
                    self.ai_up(rate)


class Ball(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle'); self.color('white'); self.penup();
        self.speed('fastest')
        self.x_iter= 5
        self.y_iter= 5

    def move(self):
        newx=self.xcor()+self.x_iter
        newy=self.ycor()+self.y_iter
        self.goto(newx,newy)

    def wbounce(self):
        self.y_iter*=-1

    def pbounce(self):
        self.x_iter*=-1

    def miss(self):
        self.goto(0,0)
        self.pbounce()

class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score1=0
        self.score2=0
        self.penup(); self.color('white'); self.ht()
        self.write_score()

    def write_score(self):
        self.goto(-50,200);
        self.write(f"{self.score1}", font=('High Tower Text',40))
        self.goto(30,200)
        self.write(f"{self.score2}", font=('High Tower Text',40))

    def update(self,player):
        self.clear()
        if player==1:
            self.score1+=1
        elif player==2:
            self.score2+=1
        self.write_score()

import turtle
import time
import random

snake_col= ['green1','green2','green3','green4','LawnGreen','DarkGreen',
        'chartreuse1','chartreuse2','chartreuse3','chartreuse4',
        'LimeGreen','OliveDrab1','OliveDrab3','ForestGreen','PaleGreen3',
        'SeaGreen1','SeaGreen2','SeaGreen3','SeaGreen4','SpringGreen1','SpringGreen1',
        'SpringGreen2','SpringGreen3','SpringGreen4']

food_col=['DarkRed','red','DeepPink4','goldenrod2','OrangeRed1',
        'plum3','orange1','wheat2','salmon2','red2','maroon']

def box():

    sc= turtle.Screen()
    sc.tracer(0)
    t= turtle.Turtle()
    t.color("green2"); t.ht(); t.penup(); t.speed('fastest')
    t.goto(-500,150)
    t.write('Snake !', align= 'center', font=('Chiller', 40))
    t.goto(-500,60)
    t.write('Press "Space" to', align= 'center', font=('Chiller', 40))
    t.goto(-500,0)
    t.write('Pause/Play', align= 'center', font=('Chiller', 40))

    def square(n,c,size):
        x=turtle.Turtle(); x.color(c);x.pensize(size)
        x.ht();x.speed('fastest');x.penup()
        x.goto(-n,-n);x.setheading(90); x.pendown()
        for _ in range(4):
            x.fd(2*n)
            x.rt(90)
    square(310,'white',2)
    square(315,'dark slate gray',3)
    square(320,'white',5)

    sc.update()


class Snake:

    global snake_col

    def __init__(self):

        self.snake= []
        self.create_snake()
        self.head=self.snake[0]

    def create_snake(self):

        for i in range(3):
            t= turtle.Turtle("square"); t.penup()
            if i==0:
                t.color("yellow","turquoise4")
            else:
                t.color(random.choice(snake_col))
            t.goto(-20*i,0)
            self.snake.append(t)

    def extend(self):

        new_pos= self.snake[-1].pos()
        t= turtle.Turtle("square"); t.penup()
        t.color(random.choice(snake_col))
        t.goto(new_pos)
        self.snake.append(t)

    def move(self):

        for i in range(len(self.snake)-1, 0, -1):
            newpos= self.snake[i-1].pos()
            self.snake[i].goto(newpos)
        self.head.fd(20)
        self.snake[1].setheading(self.head.heading())

    def up(self):
        if self.snake[1].heading()== self.head.heading():
            if self.head.heading()!=270:
                self.head.setheading(90)

    def down(self):
        if self.snake[1].heading()== self.head.heading():
            if self.head.heading()!=90:
                self.head.setheading(270)

    def left(self):
        if self.snake[1].heading()== self.head.heading():
            if self.head.heading()!=0:
                self.head.setheading(180)

    def right(self):
        if self.snake[1].heading()== self.head.heading():
            if self.head.heading()!=180:
                self.head.setheading(0)

class Food(turtle.Turtle):

    global food_col

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.penup(); self.speed('fastest'); self.color(random.choice(food_col))
        self.goto(random.randint(20,300),random.randint(20,300))

    def refresh(self,snake):

        self.penup(); self.speed('fastest'); self.color(random.choice(food_col))
        next= (random.randint(-300,300),random.randint(-300,300))
        self.goto(next)
        for body in snake:
            if self.distance(body)<20:
                while self.distance(body)<20:
                    next= (random.randint(-300,300),random.randint(-300,300))
                    self.goto(next)


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score= 0
        self.color("green2"); self.ht(); self.penup(); self.speed('fastest')
        self.goto(450,150)
        self.write(f"Score : {self.score}", align= 'center', font=('Chiller', 48))

    def update_score(self):
        self.clear()
        self.score+=1
        self.goto(450,150)
        self.write(f"Score : {self.score}", align= 'center', font=('Chiller', 48))
        return self.score

    def endgame(self):
        self.clear()
        self.goto(480,150)
        self.write("Game Over", align= 'center', font=('Chiller', 48))
        self.goto(480, 0)
        self.write(f"\n\nYour Score \nis: {self.score}", align= 'center', font=('Chiller', 48))

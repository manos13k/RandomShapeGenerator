import turtle
import random

scn = turtle.Screen()
scn.bgcolor("white")
scn.colormode(255)
t = turtle.Turtle()
t.speed(8)
turtle.title("Shapes")

class Turtle():
    def __init__(self,color,size,sides,ran):
        self.color = color
        self.size = size
        self.sides = sides
        self.corner = 360/sides
        self.ran = ran
    def shape(self):
        if (self.ran <=4):
            t.pu()
            t.fillcolor(self.color)
            t.goto(random.randint(-350,350),random.randint(-350,350))
            t.pencolor(self.color)
            t.begin_fill()
            t.pd()
            for i in range (0,self.sides):
                t.rt(self.corner)
                t.fd(self.size)
            t.pu()
            t.end_fill()
        else:
            t.pu()
            t.fillcolor(self.color)
            t.goto(random.randint(-350,350),random.randint(-350,350))
            t.pencolor(self.color)
            t.begin_fill()
            t.pd()
            for i in range(5):
                t.forward(self.size)
                t.right(144)
                t.fd(self.size)
            t.pu()
            t.end_fill()

for i in range(0,50):
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    ts = Turtle(ran = int(random.randint(0,7)),color = (r, g, b),size = int(random.randint(10,150)),sides = int(random.randint(3,8))).shape()
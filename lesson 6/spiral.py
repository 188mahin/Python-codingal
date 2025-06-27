import turtle
my_wn=turtle.Screen()
my_wn.bgcolor("dark blue")
my_wn.title("spiral")
my_pen=turtle.Turtle()
my_pen.color("white")
size=0
while True:
    for i in range(4):
        my_pen.forward(size+1)
        my_pen.left(90)
        size=size-5
    size+=1
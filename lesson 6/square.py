import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
numside=4
length=80
angle=360.0/4
for i in range(numside):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()

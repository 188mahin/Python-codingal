import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(400,400)
polygon=turtle.Turtle()
numside=6
length=80
angle=360.0/6
for i in range(numside):
    polygon.forward(length)
    polygon.right(angle)
turtle.done()


import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon = turtle.Turtle()
n = 6
l = 90
for i in range(1,n+1):
    polygon.forward(l)
    polygon.right(60)
turtle.done()
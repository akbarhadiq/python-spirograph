import turtle
import random

kim = turtle.Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


kim.pensize(3)
kim.speed(0)
heading = 10

while heading < 360:
    kim.color(random_color())
    kim.circle(170)
    kim.seth(heading)
    heading = heading + 10

screen = turtle.Screen()
screen.exitonclick()

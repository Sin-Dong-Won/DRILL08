import turtle
import random
import math

r = 100
l = 80

def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]

    a = (y2 - y1)/(x2 - x1)
    b = y1 - x1 * a

    for x in range(x1, x2 + 1 ,10):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)

    pass


def draw_Kite_shaped(px, py):
    global r
    p = px, py
    draw_big_point(p)

    for t in range(0, 360 + 1, 2):
        math.radians(t)

        x = px + (math.cos(t) + 1.3 * (math.cos(t) ** 2) - 0.8) * r
        y = py + (1.5 * math.sin(t)) * r

        draw_point((x, y))

    pass

def draw_Peanut_shaped(px, py):
    global r
    p = px, py
    draw_big_point(p)

    for t in range(0, 360 + 1, 2):
        math.radians(t)

        m = (math.sqrt(math.cos(t) ** 2 + (math.sin(t) ** 2) * 0.25))

        x = px + m * r * math.cos(t)
        y = py + m * r * math.sin(t)

        draw_point((x, y))

    pass


def draw_Round_Triangle(px, py):
    global r
    p = px, py
    draw_big_point(p)

    for t in range(0, 360 + 1, 2):
        math.radians(t)

        m = (2 + 0.3 * math.cos(3 * t))
        x = px + m * r * math.cos(t)
        y = py + m * r * math.sin(t)
        draw_point((x, y))

    pass

def draw_Drop_shape(px, py):
    global r
    p = px, py
    draw_big_point(p)

    for t in range(0, 360 + 1, 2):
        math.radians(t)

        x = px + (-0.5 + 0.75 * math.sin( t / 2)) * r
        y = py + (-0.75 * math.sin(t)) * r
        draw_point((x, y))

    pass


prepare_turtle_canvas()

draw_Kite_shaped(100, -100)
draw_Peanut_shaped(100, 100)
draw_Round_Triangle(-100, -100)
draw_Drop_shape(-100, 100)

turtle.done()


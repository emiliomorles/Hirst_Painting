import turtle as t
import random

spot = t.Turtle()
spot.penup()
# spot.shape("square")
spot.hideturtle()
t.colormode(255)
spot.speed(0)
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


def dashed_spot():
    """It creates a dashed line"""
    spot.setx(-200)
    spot.sety(-200)
    line_length = 10  # Total length of the dashed line
    gap_length = 50  # Length of each gap
    for _ in range(5):
        for _ in range(line_length):
            spot.dot(20, random.choice(color_list))
            spot.penup()
            spot.forward(gap_length)
            spot.pendown()
        spot.penup()
        spot.left(90)
        spot.forward(50)
        spot.left(90)
        spot.forward(50)
        for _ in range(line_length):
            spot.dot(20, random.choice(color_list))
            spot.penup()
            spot.forward(gap_length)
            spot.pendown()
        spot.penup()
        spot.right(90)
        spot.forward(50)
        spot.right(90)
        spot.forward(50)


dashed_spot()

screen = t.Screen()
screen.exitonclick()

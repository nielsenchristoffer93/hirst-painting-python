import colorgram
from turtle import Turtle, Screen
import random

# Extract colors from image
# rgb_colors = []
# colors = colorgram.extract("hirst.jpg", 30)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     new_color = (red, green, blue)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

# 10x10 grid
# 20 in size and space between is 50

tim = Turtle()
tim.pensize(20)
tim.speed(0)
tim.hideturtle()
screen = Screen()
screen.colormode(255)

def set_starting_position(turtle, startin_pos_y):
    turtle.penup()
    turtle.goto(-440, startin_pos_y)

def move_and_draw_1_dot(turtle):
    turtle.dot()
    turtle.forward(96)

def move_to_new_row(turtle, y_pos):
    y_pos += 80  # 80
    turtle.goto(-440, y_pos)
    return y_pos

y_position = -360
set_starting_position(tim, y_position)

for _ in range(10): # 10 Rows
    for _ in range(10): # Draw 10 dots on each row
        tim.pencolor(random.choice(color_list))
        move_and_draw_1_dot(tim)

    y_position = move_to_new_row(tim, y_position)




screen.exitonclick()
import turtle as turtle_module
import random

turtle_module.colormode(255)
color_list = [(233, 227, 220), (203, 160, 110), (214, 228, 238),
              (239, 218, 228), (216, 235, 226), (125, 168, 192),
              (56, 105, 140), (189, 144, 164), (140, 68, 93),
              (132, 178, 157), (149, 86, 58), (222, 203, 126),
              (57, 122, 89), (171, 162, 49), (187, 89, 114),
              (130, 32, 52), (73, 161, 133), (207, 92, 68),
              (49, 163, 184), (224, 171, 188), (68, 30, 50),
              (68, 37, 24), (156, 211, 195), (233, 172, 160),
              (32, 43, 70), (39, 56, 109), (107, 119, 168),
              (148, 209, 220), (131, 35, 26), (180, 185, 217)]

raphael = turtle_module.Turtle()
raphael.speed("fastest")
raphael.penup()
raphael.hideturtle()
raphael.setheading(225)
raphael.forward(250)
raphael.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    raphael.dot(20, random.choice(color_list))
    raphael.forward(50)

    if dot_count % 10 == 0:
        raphael.setheading(90)
        raphael.forward(50)
        raphael.setheading(180)
        raphael.forward(500)
        raphael.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:


    def __init__(self):
        """Initializes our cars"""
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE
        

    def create_car(self):
        """Creates a new car"""
        random_chance = random.randint(1, 5)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.goto(300, random.randint(-250, 250))
            self.car_list.append(new_car)


    def move(self):
        """Moves the car"""
        for car in self.car_list:
            car.forward(self.move_distance)


    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

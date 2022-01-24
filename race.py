import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["green", "red", "yellow", "purple", "black"]
y_positions = [-80, -40, 0, 40, 80]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.goto(x=-240, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False;
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won!! The {winning_color} turtle is the winner!")

            else:
                print(f"you have Lost! The {winning_color} turtle is the winner!")
        rand_dist = random.randint(1, 10)
        turtle.forward(rand_dist)


screen.exitonclick()



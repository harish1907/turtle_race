from turtle import *
import random

screen = Screen()
race_on = False
screen.setup(500, 400)
user_bet = screen.textinput(title="Make a bet.", prompt="Which turtle win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
yaxis = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(-230, yaxis[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You'r won! The {winning_color} turtle is the winner.")
            else:
                print(f"You'r loose! The {winning_color} turtle is the winner.")

        random_step = random.randint(0, 10)
        turtle.forward(random_step)


screen.exitonclick()

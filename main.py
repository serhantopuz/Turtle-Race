from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a Bet", prompt="Who will win the race? Enter a colour:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -80

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    all_turtles.append(new_turtle)
    y += 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            winning_color = turtle.pencolor()
            is_race_on = False
        random_number = random.randint(0, 10)
        turtle.forward(random_number)

if winning_color == user_bet:
    print("You Won.")
else:
    print("You Lost.")

screen.exitonclick()

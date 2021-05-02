import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

count = 0
while count < 6:
    turtle = t.Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[count])
    val = -75 + count*25
    turtle.goto(x=-230, y=val)
    turtles.append(turtle)
    count += 1


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost. the {winning_color} turtle is the winner!")
            is_race_on = False
            break
        turtle.forward(random.randint(0,10))

screen.exitonclick()
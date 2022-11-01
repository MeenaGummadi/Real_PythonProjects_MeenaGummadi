from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Pick the color of the turtle which wins?: ")
colors = ["red", "purple", "green", "dark orange", "yellow", "blue"]
y_positions = [0, -25, 25, -50, 50, -75]
all_turtles = []

for index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[index])
    all_turtles.append(tim)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You've won the game. The winner is {winner} turtle.")
            else:
                print(f"You've lose the game. The winner is {winner} turtle.")
            is_race_on = False
        speed = random.randint(0, 10)
        turtle.forward(speed)


screen.exitonclick()

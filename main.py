import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

ans = screen.textinput(title="Guess the State", prompt="What's the another state's name?").title()

import pandas as pd

dt = pd.read_csv("50_states.csv")
states = dt["state"].to_list()



state_dt = dt[dt.state == states]

# row = state_dt.iloc[0]
# t.goto(int(row.x), int(row.y))
#
# t.write(ans)

guesses = []

while len(guesses) < 50:
    ans = screen.textinput(title=f"{len(guesses)}/50 States correct", prompt="What's another state's name?").title()
    ans = ans.title()
    if ans in states and ans not in guesses:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        guesses.append(ans)
        state_dt = dt[dt.state == ans]
        t.goto(int(state_dt.x.item()), int(state_dt.y.item()))
        t.write(ans)

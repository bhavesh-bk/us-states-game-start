import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

ans = screen.textinput(title="Guess the State", prompt="What's the another state's name?")


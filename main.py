import turtle
import pandas

screen = turtle.Screen()
screen.title("US State game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# read file
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

not_guessed = []
guessed_states = []
gameon = True

while len(guessed_states) < 50 and gameon == True:
    answer_state = turtle.textinput(f"{len(guessed_states)}/50 States Guesses", "What's another state name?").title()

    if answer_state in all_states and answer_state not in guessed_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        guessed_states.append(answer_state)

    elif answer_state == "Exit":
        for states in all_states:
            if states not in guessed_states:
                not_guessed.append(states)
        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("not-guesses.csv")
        print(not_guessed)
        gameon = False


# convert from csv to Python list
# create a new list
# get the cordinates

turtle.mainloop()

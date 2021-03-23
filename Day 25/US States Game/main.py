import turtle
import pandas
IMG_PATH = "blank_states_img.gif"

def print_name(turtle, state, x, y):
    turtle.goto(x,y)
    turtle.write(state)

screen = turtle.Screen()
screen.title("U.S. States Game")

data = pandas.read_csv("50_states.csv")
state_names = data.state.tolist()
prev_answers = []

screen.addshape(IMG_PATH)
turtle.shape(IMG_PATH)
writer = turtle.Turtle()
writer.up()
writer.hideturtle()


while (len(prev_answers) != len(state_names)):
    answer = screen.textinput(title = f"{len(prev_answers)} / {len(state_names)} states correct", prompt = "Enter the name of a state:").title()
    if answer == "Exit":
        break
    if answer in state_names and answer not in prev_answers:
        prev_answers.append(answer)
        dataline = data[data["state"] == answer]
        print_name(writer, answer, int(dataline.x), int(dataline.y))



missed_states = [x for x in state_names if x not in prev_answers]
df = pandas.DataFrame(missed_states)
df.to_csv("states_to_learn.csv")

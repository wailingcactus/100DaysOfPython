import turtle
import pandas as pd
from label import Label

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

# Set up screen and import US image
screen = turtle.Screen()
screen.title("U.S. States Game")
image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
states_guessed = 0
guessed_states=[]


while len(guessed_states)<50:
    answer_state = screen.textinput(title = f'{states_guessed}/50 States Correct', prompt='What is the state name?').title()
    if answer_state == 'Exit':
        states_missed = [state for state in all_states if state not in guessed_states ]
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_missed.append(state)
        new_data = pd.DataFrame(states_missed)
        new_data.to_csv('missed_states.csv')
        break
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        states_guessed += 1
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        Label(x,y, answer_state)




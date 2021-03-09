import pandas
import turtle
screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
loop = True
data = pandas.read_csv('./50_states.csv')
all_states = data.state.to_list()
# print(all_states)
count = 0
total = []

# print(all_states)
while len(total) < 50:
    answer_state = screen.textinput(title=f' {len(total)}/50 Guess the State', prompt="What's another state's name?")
    answer = answer_state.capitalize()

    if answer in all_states:
        print('YEs')
        total.append(answer)
        print(answer)
        tur = turtle.Turtle()
        tur.hideturtle()
        tur.penup()
        date_state = data[data.state == answer]
        tur.goto(int(date_state.x), int(date_state.y))
        tur.write(answer)
    elif answer == 'Exit':
        miss_state = [state for state in all_states if answer not in total]
        new_data = pandas.DataFrame(miss_state)
        new_data.to_csv('state to learn.csv')
        break



# import pandas
# weather = {
#     'day': ['monday', 'tuesday', 'wednesday'],
#     'temp': [30, 40, 34]
# }
#
# data = pandas.DataFrame(weather)
#
# for (index, row) in data.iterrows():
#     print(row.temp)
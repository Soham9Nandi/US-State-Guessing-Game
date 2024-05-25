import turtle
import pandas

screen = turtle.Screen()
screen.title = "U.S. States Game"
image = "day-25-us-states-game-start/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv('day-25-us-states-game-start/50_states.csv')
state_names = states['state'].to_list()
state_xcoor = states['x'].to_list()
state_ycoor = states['y'].to_list()

answered = []
answer_number = 0


#The turtle which writes the names of the states
name_writer = turtle.Turtle()
name_writer.penup()
name_writer.color('black')
name_writer.hideturtle()



game_is_on = True
while game_is_on:
    answer_state_input = screen.textinput(title=f'Guess the State {answer_number}/50',prompt="What's another state name?")
    answer_state = answer_state_input.title()
    print(answer_state)
    if (answer_state in state_names):
        print('Yo') 
    if (answer_state not in answered) and (answer_state in state_names):
        #increase answer_number
        answer_number+=1#This number is also showed on the title signifying how many states have been guessed
        
        #Find the x and y coor of the state
        xcoor = state_xcoor[state_names.index(answer_state)]
        ycoor = state_ycoor[state_names.index(answer_state)]
        
        #make the turtle write the name
        name_writer.goto(xcoor,ycoor)
        name_writer.write(answer_state,align='center',font=("Courier",10,"normal"))

    if answer_number == 50:
        game_is_on = False

turtle.mainloop()


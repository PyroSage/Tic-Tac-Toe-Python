## This is the GUI based version of the game
from tkinter import *
import random

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == ' ' and check_winner() is False:
        buttons[row][column]['text'] = player
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text = 'Player ' + player + '\'s turn')
            elif check_winner() is True:
                label.config(text = 'Player ' + player + ' wins!')
            elif check_winner() == 'Its a draw!':
                label.config(text = 'Its a draw!')
        else:
            buttons[row][column]['text'] = player
            if player == players[1]:
                buttons[row][column]['text'] = player
                if check_winner() is False:
                    player = players[0]
                    label.config(text = 'Player ' + player + '\'s turn')
                elif check_winner() is True:
                    label.config(text = 'Player ' + player + ' wins!')
                elif check_winner() == 'Its a draw!':
                    label.config(text = 'Its a draw!')
        

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != ' ':
            buttons[row][0].config(bg = 'green')
            buttons[row][1].config(bg = 'green')
            buttons[row][2].config(bg = 'green')
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != ' ':
            buttons[0][col].config(bg = 'green')
            buttons[1][col].config(bg = 'green')
            buttons[2][col].config(bg = 'green')
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != ' ':
        buttons[0][0].config(bg = 'green')
        buttons[1][1].config(bg = 'green')
        buttons[2][2].config(bg = 'green')
        return True
    elif buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != ' ':
        buttons[2][0].config(bg = 'green')
        buttons[1][1].config(bg = 'green')
        buttons[0][2].config(bg = 'green')
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config( bg = 'yellow')
        return "Its a draw!"
    else:
        return False

def check_draw():
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == ' ':
                return False
    return True

def empty_spaces():
    spaces = 9 
    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] != ' ':
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text = 'Player ' + player + '\'s turn')
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text = ' ', bg = 'white')

window = Tk()
window.title('Tic-Tac-Toe')
players = ['🐯', '🐶']
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
label = Label(text = 'Player ' + player + '\'s turn', font=('consolas', 40))
label.pack(side = 'top')

reset_button = Button(text = 'Reset',font=('consolas', 20), command = new_game)
reset_button.pack(side = 'top')

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        buttons[row][col] = Button(frame, text = ' ', bg = 'white', font=('consolas', 40), width = 5, height = 2, command = lambda row = row, column = col: next_turn(row, column))
        buttons[row][col].grid(row = row, column = col)
window.mainloop()
   
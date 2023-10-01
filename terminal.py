## This is the Terminal based version of the game

def printBoard(xstate, ostate):
    zero = 'X' if xstate[0] == 1 else ('O' if ostate[0] == 1 else '0')
    one = 'X' if xstate[1] == 1 else ('O' if ostate[1] == 1 else '1')
    two = 'X' if xstate[2] == 1 else ('O' if ostate[2] == 1 else '2')
    three = 'X' if xstate[3] == 1 else ('O' if ostate[3] == 1 else '3')
    four = 'X' if xstate[4] == 1 else ('O' if ostate[4] == 1 else '4')
    five = 'X' if xstate[5] == 1 else ('O' if ostate[5] == 1 else '5')
    six = 'X' if xstate[6] == 1 else ('O' if ostate[6] == 1 else '6')
    seven = 'X' if xstate[7] == 1 else ('O' if ostate[7] == 1 else '7')
    eight = 'X' if xstate[8] == 1 else ('O' if ostate[8] == 1 else '8')
    print(f' {zero} | {one} | {two} ')
    print(f'---|---|---')
    print(f' {three} | {four} | {five} ')
    print(f'---|---|---')
    print(f' {six} | {seven} | {eight} ')
    print(f'---|---|---')

def checkwin(xstate, ostate):
    xwins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [0, 3, 6], [2, 5, 8]]
    owins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [0, 3, 6], [2, 5, 8]]
    for i in xwins:
        if(xstate[i[0]] == 1 and xstate[i[1]] == 1 and xstate[i[2]] == 1):
            return 3
    for i in owins:
        if(ostate[i[0]] == 1 and ostate[i[1]] == 1 and ostate[i[2]] == 1):
            return 4

if __name__ == '__main__':
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ostate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1 # 1 for x, 0 for o
    print('Konichiwa world, to the tic-tac-toe game!')
    printBoard(xState, ostate)
    while(True):
        if(turn == 1):
            print("X's turn")
            value = int(input('Enter the position: '))
            if(value > 8):
                print('Invalid position')
                continue
            if(xState[value] == 1 or ostate[value] == 1):
                print('Position already occupied')
                continue
            xState[value] = 1
            turn = 0
            printBoard(xState, ostate)
        else:
            print("O's turn")
            value = int(input('Enter the position: '))
            if(value > 8):
                print('Invalid position')
                continue
            if(xState[value] == 1 or ostate[value] == 1):
                print('Position already occupied')
                continue
            ostate[value] = 1
            turn = 1
            printBoard(xState, ostate)
        
        if(checkwin(xState, ostate) == 3):
            print('X wins!')
            break
        elif(checkwin(xState, ostate) == 4):
            print('O wins!')
            break
        else:
            continue
import time
import random

board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}


def init() -> None:
    print('Welcome to Tic Tac Toe! Type "Help" to learn how to play.')
    time.sleep(1)
    get_board()
    get_command()


def get_board() -> None:
    print('Current Board:')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def help_board() -> None:
    print('Choose where to place according to the numbers: ')
    print('7, 8, 9 \n4, 5, 6 \n1, 2, 3')


def help_commands() -> None:
    print('Type Quit or Exit to quit.')


def check_place(key:str) -> bool:
    if board[key] != ' ':
        return False
    else:
        return True


def computer_play() -> None:
    num = random.randint(1, 9)
    if check_place(str(num)):
        board[str(num)] = "O"
    else:
        computer_play()


def declare_winner(winner: str) -> None:
    if winner == "X":
        get_board()
        print('\nYou Won!\n')
    else:
        get_board()
        print("\nYou Lost!\n")


def check_win() -> bool:
    if board['7'] == board['8'] == board['9'] != ' ': #Across The Top
        declare_winner(board['7'])
        return True
    elif board['4'] == board['5'] == board['6'] != ' ': #Across The Middle
        declare_winner(board['4'])
        return True
    elif board['1'] == board['2'] == board['3'] != ' ': #Across The Bottom
        declare_winner(board['1'])
        return True
    elif board['7'] == board['4'] == board['1'] != ' ': #Down Left
        declare_winner(board['7'])
        return True
    elif board['8'] == board['5'] == board['2'] != ' ': #Down Middle
        declare_winner(board['8'])
        return True
    elif board['9'] == board['6'] == board['3'] != ' ': #Down Right
        declare_winner(board['9'])
        return True
    elif board['7'] == board['5'] == board['3'] != ' ': #Diagonal
        declare_winner(board['7'])
        return True
    elif board['1'] == board['5'] == board['9'] != ' ': #Diagonal
        declare_winner(board['1'])
        return True

    for x in board:
        if board[x] == ' ':
            return False
    print("Game Over It's A Tie!")
    get_board()
    return True


def get_command() -> None:
    key = input('Command: ')
    if key.lower() == 'help':
        help_board()
        help_commands()
        time.sleep(3)
        get_command()
    elif key.lower() == "quit" or key.lower() == "exit":
        print("Goodbye")
        return
    else:
        check_win()
        try:
            int(key)
            valid = check_place(key)
            if not valid:
                print('There is already a Key there!')
            else:
                board[key] = 'X'
                if check_win():
                    return
                computer_play()
                if check_win():
                    return
                get_board()
            get_command()
        except:
            print("Uknown Command Try Inputting Another Command")
            get_command()


if __name__ == "__main__":
    init()
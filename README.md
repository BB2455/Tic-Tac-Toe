# Tic-Tac-Toe CLI

Simple tic-tac-toe game using python that is run in the terminal.

## How it works

On being called the function init will run and welcome the user, give a tip to learn how to play, then will show the board and ask the user to type a command.

- The get_board function will show the current board in it's current state by accessing the board dictionary declared at the top of the file.
- The get_command function will wait for the user input and check the input against the defined keywords (help, quit, exit, 1, 2, etc..)
- After every valid move the check_win function will run before and after the computer_play function which will pick a random position to play.
- The check_win function will run everytime a command is input and will declare a winner if there is a winning move or no more moves remaining and will break out of the loop.

## Installation

Download the repository and place it in desired file location.

## Usage

Call the tictactoe.py file in the terminal with python.

```
python tictactoe.py
```

When run it show you the current board and ask you where to place your turn (1-9):

```
Welcome to Tic Tac Toe! Type "Help" to learn how to play.
Current Board:
 | |
-+-+-
 | |
-+-+-
 | |
Command:
```

Invalid commands will warn you and tell you to try again.

```
Uknown Command Try Inputting Another Command
```

Typing 'help' will bring up the help menu and show you the placement of each number and how to quit.

```
Choose where to place according to the numbers:
7, 8, 9
4, 5, 6
1, 2, 3
Type Quit or Exit to quit.
Command:
```

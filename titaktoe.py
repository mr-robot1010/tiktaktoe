def read_me():
    # In this project - I create a tik-tak-toe game
    # Sunday November 20 2021
    # rev - A.01.05
    return    
#-------------Global Variablles -----
global board, game_still_going, winner, player
board = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]
# Game Still active?
game_still_going = True
winner = None
current_player = 'X'
#-------------------------------------

def display_board():
    # Build out board layout
    print()
    print("\t *WELCOME*")
    print("\t___________\n")
    print(f"\t {board[0]} | {board[1]} | {board[2]}")
    print(f"\t {board[3]} | {board[4]} | {board[5]}")
    print(f"\t {board[6]} | {board[7]} | {board[8]}")
    print("\t___________")

def play_game():    
    display_board()
    
    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    # Game has ended
    if winner == 'X' or winner == 'O':
        print(f'Player "{winner}" won!')


def handle_turn(current_player):
    global game_still_going 
    
    print(f'\n\t{current_player}\'s turn.\n')
    position = input("Please Enter Position 1-9: ")

    while position not in ['1','2','3','4','5','6','7','8','9']:
        position = input("ERROR: invalid input. Please Enter Position 1-9: ")

        
    
    position = int(position) - 1 
    board[position] = current_player
    display_board()


def check_if_game_over():
    check_for_win()
    check_if_tie()


def check_for_win():
    global winner 
    # check rows
    row_winner = check_rows()

    # check Columns
    column_winner = check_columns()

    # check diag
    diagnol_winner = check_diagnols()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagnol_winner:
        winner = diagnol_winner
    return
    

def check_rows():
    # Set up global variable
    global game_still_going
    # Check for Row winner
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Set up global variable
    global game_still_going
    # Check for columns winner
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagnols():
    # Set up global variable
    global game_still_going
    # Check for daig winner
    daig_1 = board[0] == board[4] == board[8] != '-'
    daig_2 = board[2] == board[4] == board[6] != '-'

    if daig_1 or daig_2:
        game_still_going = False
        return board[4]
    return


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

def check_if_tie():
    global game_still_going
    if '-' not in board:
        game_still_going = False

    return 

play_game()

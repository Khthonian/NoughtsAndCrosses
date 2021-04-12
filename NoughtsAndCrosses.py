# This function will control the layout of the board
board = ["#", "#", "#",
         "#", "#", "#",
         "#", "#", "#"]

# This function will draw the board
def draw_board():
    print(board[0] + "|" + board [1] + "|" + board[2])
    print(board[3] + "|" + board [4] + "|" + board[5])
    print(board[6] + "|" + board [7] + "|" + board[8])

# This function will handle turn placements
def turn_control(current_symbol):
    # Determine where the player would like to position their next icon
    position = input('Where would ' + current_symbol + ' like to place their icon from 1-9: ')
    # Ensure that the user's input is valid and that the chosen space is available to be taken
    valid = False
    while not valid:
        # Check to make sure the input is a valid character
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Where would ' + current_symbol + ' like to place their icon from 1-9: ')
        # Check the index of the board
        position = int(position)-1
        # Check position is available
        if board[position] == '#':
            valid = True
        else:
            print('This move is invalid. Please choose another position.')
    # The game will now place the icon on the board
    board[position] = current_symbol
    draw_board()

# This function will check if the game has finished, by either being won or tied
def game_finished():
    game_won()
    game_tied()

# This function will check for a win
def game_won():
    # Allow for the global variable for the winner
    global victor
    row_win = row_check()
    column_win = column_check()
    diagonal_win = diagonal_check()
    if row_win:
        victor = row_win
    elif column_win:
        victor = column_win
    elif diagonal_win:
        victor = diagonal_win
    else:
        victor = None

    return

# This function will check for a tie
def game_tied():
    # Allow for the global variable to check for the continued play of the game
    global game_in_play
    if '#' not in board:
        game_in_play = False
    return

# This function will check the rows
def row_check():
    # Allow for the global variable to check for the continued play of the game
    global game_in_play
    # Determine whether the rows contain any winning combinations as a result of having the same output
    first_row = board[0] == board[1] == board[2] != '#'
    second_row = board[3] == board[4] == board[5] != '#'
    third_row = board[6] == board[7] == board[8] != '#'
    # If a row has a winning combination, the game will be stopped
    if first_row or second_row or third_row:
        game_in_play = False
    # Now return a value for the game winner, the values being those of Players 1 or 2
    if first_row:
        return board[0]
    if second_row:
        return board[3]
    if third_row:
        return board[6]
    return

# This function will check the columns
def column_check():
    # Allow for the global variable to check for the continued play of the game
    global game_in_play
    # Determine whether the columns contain any winning combinations as a result of having the same output
    first_column = board[0] == board[3] == board[6] != '#'
    second_column = board[1] == board[4] == board[7] != '#'
    third_column = board[2] == board[5] == board[8] != '#'
    # If a column has a winning combination, the game will be stopped
    if first_column or second_column or third_column:
        game_in_play = False
    # Now return a value for the game winner, the values being those of Players 1 or 2
    if first_column:
        return board[0]
    if second_column:
        return board[1]
    if third_column:
        return board[2]
    return

# This function will check the diagonals
def diagonal_check():
    # Allow for the global variable to check for the continued play of the game
    global game_in_play
    # Determine whether the diagonals contain any winning combinations as a result of having the same output
    first_diagonal = board[0] == board[4] == board[8] != '#'
    second_diagonal = board[2] == board[4] == board[6] != '#'    
    # If a diagonal has a winning combination, the game will be stopped
    if first_diagonal or second_diagonal:
        game_in_play = False
    # Now return a value for the game winner, the values being those of Players 1 or 2
    if first_diagonal:
        return board[0]
    if second_diagonal:
        return board[2]
    return

# This function will swap between the players during the game
def player_switch():
  # Global variables we need
  global current_symbol
  # If the current player was X, make it O
  if current_symbol == "X":
    current_symbol = "O"
  # Or if the current player was O, make it X
  elif current_symbol == "O":
    current_symbol = "X"
    
# This function will control if the game is still in play
game_in_play = True

# This function will control the winner
victor = None

# This function will determine whose turn it is to play
current_symbol = 'X'

# This function will control the game vs a human
def begin_game_human():
    print("Welcome to Tic Tac Toe. Player 1 shall be X and Player 2 shall be O.")
    # Draw out the initial board
    draw_board()
    while game_in_play:
        turn_control(current_symbol)
        game_finished()
        player_switch()
    # This will determine post-game results
    if victor == 'X' or victor == 'O':
        print(victor + ' has won.')
    elif victor == None:
        print('Nobody has won, the game is a draw.')

#--------------------------------CPU Game------------------------------

import random
# This function shall control the placements by the player and the CPU
def turn_control_cpu(current_symbol):
    # Determine where the player would like to position their next icon
    position = input('Where would X like to place their icon from 1-9: ')
    # Ensure that the user's input is valid and that the chosen space is available to be taken
    valid = False
    while not valid:
        # Check to make sure the input is a valid character
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input('Where would ' + current_symbol + ' like to place their icon from 1-9: ')
        # Check the index of the board
        position = int(position)-1
        # Check position is available
        if board[position] == '#':
            valid = True
        else:
            print('This move is invalid. Please choose another position.')
    # The game will now place the icon on the board
    board[position] = current_symbol
    

# This function shall control the randomised moves performed by the CPU
def cpu_decision():
    # This function will generate a random number in order to place an icon for the CPU
    position_cpu = random.randint(0,8)
    valid_cpu = False
    while not valid_cpu:
        if board[position_cpu] == '#':
            valid_cpu = True
        else:
            position_cpu = random.randint(0,8)
    board[position_cpu] = 'O'
    draw_board()

# This function will control the game vs the computer
def begin_game_cpu():
    print("Welcome to Tic Tac Toe. You shall be X and the CPU shall be O.")
    # Draw out the initial board
    draw_board()
    while game_in_play:
        turn_control_cpu(current_symbol)
        cpu_decision()
        game_finished()
    # This will determine post-game results
    if victor == 'X' or victor == 'O':
        print(victor + ' has won.')
    elif victor == None:
        print('Nobody has won, the game is a draw.')    


#-----------------------Main Menu---------------------

# This section of code will function as the opening gamemode selection for the game
player_count = input('How many players are there (1 or 2): ')
player_count = int(player_count)
if player_count == 1:
    begin_game_cpu()
elif player_count == 2:
    begin_game_human()
else:
    player_count = input('How many players are there (1 or 2): ')
player_count = int(player_count)


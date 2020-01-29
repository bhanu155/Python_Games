#   CHANDRA BHANU
#   https://www.bhanu155.github.io

import random

def display_board(board):
    '''
        Function to print current board status
        input : board
    '''
    print('\n')
    print('\t ' + board[1] + ' | ' + board[2] + ' | '+ board[3])
    print('\t' + '-'*11)
    print('\t ' + board[4] + ' | ' + board[5] + ' | '+ board[6])
    print('\t'+'-'*11)
    print('\t ' + board[7] + ' | ' + board[8] + ' | '+ board[9])
    print('\n')
    
def player_input():
    '''
        Function to take input from player 
        Returns player marker symbol
    '''
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    '''
        Funcftion to place the marker on board 
        input: board, marker, position
    '''
    board[position] = marker

def win_check(board,mark):
    '''
        Function to check whether current mark has won or not
        input: board, mark to be checked
        Returns True if player has won, else returns False
    '''
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    '''
        Function to choose random first player
        Returns a random player who should move first
    '''
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    '''
        Function to check whether a postion is available or not
        input: board, position to be checked
        Returns True if position is empty
    '''
    return board[position] == ' '

def full_board_check(board):
    '''
        Function to check if board is completely filled or not
        input:board
        Returns True if any space is empty, else returns False
    '''
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    '''
        Function to choose a position by player
        input:board
        Returns selected valid position
    '''
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    '''
        Function to ask for rematch
        returns yes / no
    '''
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break

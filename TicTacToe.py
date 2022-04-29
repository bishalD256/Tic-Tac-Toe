import random

def display_board(board):
    #print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    #print('   |   |')
    print('-----------')
    #print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    #print('   |   |')
    print('-----------')
    #print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    #print('   |   |')


def player_input():
    marker = ''

    #KEEP ASKING PLAYER 1 TO CHOOSE X OR O
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, choose X or O: ")

    player1 = marker

    #ASSIGN PLAYER 2, THE OPPOSITE MARKER
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker
    #return board


def win_check(board, mark):
    #ALL ROWS, and check to see if they all share the same marker
    if ((board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark)):
        return True
    # ALL COLUMNS, and check to see if they all share the same marker
    elif ((board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark)):
        return True
    #2 diagonals, check to see match
    elif ((board[3] == mark and board[5] == mark and board[7] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark)):
        return True
    else:
        return False


def choose_first():
    flip = random.randint(1, 2)

    if flip == 1:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    if board[position] == ' ':
        return True
    else:
        print("Position has been taken already")
        return False


def full_board_check(board):
    for item in board:
        if item == ' ':
            return False
    return True


def player_choice(board):
    pos = 0

    while pos not in list(range(1, 10)) or not space_check(board, pos):
        pos = int(input("Choose a position between 1 to 9 : "))

    return pos


def replay():
    choice = input("Do you want to play again? Y or N : ")

    return choice == 'Y'



print('Welcome to Tic Tac Toe!')

#WHILE LOOP TO KEEP RUNNING THE GAME
while True:
    #PLAY THE GAME

    ##SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKER X, O)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n? : ')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False


    ##GAME PLAY
    while game_on:
        ###PLAYER 1 TURN
        if turn == 'Player 1':
            #Display the board
            display_board(the_board)

            #Choose a position
            position = player_choice(the_board)

            #Place the marker on the postion
            place_marker(the_board, player1_marker, position)

            #Check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player 1 has won!!")
                game_on = False
            else:   #or if There is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE!!")
                    game_on = False
                else:   #No tie and No win? the next player turn
                    turn = 'Player 2'
        else:   ###PLAYER 2 TURN
            # Display the board
            display_board(the_board)

            # Choose a position
            position = player_choice(the_board)

            # Place the marker on the postion
            place_marker(the_board, player2_marker, position)

            # Check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player 2 has won!!")
                game_on = False
            else:  # or if There is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE!!")
                    game_on = False
                else:  # No tie and No win? the next player turn
                    turn = 'Player 1'

    #BREAK OUT OF THE WHILE LOOP ON repley()
    if not replay():
        break
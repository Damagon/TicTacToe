#Tic Tac Toe Game
# -------------Global Variables  ---------------
#if game is still going
game_not_ended = True;

#Who won or tie?
winner = None
#Whose turn is it?
current_player = "X"
# -------------Global Variables  ---------------



board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#handle a turn of one of the two player
def handle_turn(current_player):
    print(current_player + "'s turn.")
    while True:
        try:
            position = input("Choose a position from 1-9: ") #position is a variable
            if int(position) < 1 or int(position) > 9:
                raise ValueError #this will send it to the print message and back to the input option
            break
        except ValueError:
            print("Please enter a different number")

    position = int(position)-1 #Lists start at zero indexing
    if board[position] == "-":
        board[position] = current_player  # put in X in that position of the list
    else:
        print("Cannot overwrite previously written symbol")
    display_board()


def play_game():
    display_board()  # display the tic tac toe board
    while game_not_ended:

        #call the function to handle a turn of one of the two players
        handle_turn(current_player)
        #check if game has ended
        check_game_over()
    #Flip to other player
        flip_player()
    #will skip to this section if game_not_ended is False
    if winner == "X" or winner == "O":
        print("Whoever was playing as " + winner + " has won the game!")
    elif winner == None:
        print("The game is a tie.")


def check_game_over ():
    check_if_win()
    check_if_tie()

def check_if_win():
    #Set up global variables
    global winner

    #check rows
    row_winner = check_rows()

    #check columns
    column_winner = check_columns()

    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    global game_not_ended
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    #If any row has a match flag that there is a win
    if row_1 or row_2 or row_3:
        game_not_ended = False
        # Return whether its X or O that won
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    global game_not_ended
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any row has a match flag that there is a win
    if column_1 or column_2 or column_3:
        game_not_ended = False
        # Return whether its X or O that won
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return


def check_diagonals():
    global game_not_ended
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # If any row has a match flag that there is a win
    if diagonal_1 or diagonal_2:
        game_not_ended = False

     # Return whether its X or O that won
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[1]

    return



def check_if_tie():
    global game_not_ended
    if "-" not in board:
        game_not_ended = False
    return

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game() #function to be able to play the game




#board
    #make a list, not a tuple - we want mutability
#display board
#play game
    #check win
        #check rows
        #check diagonals
    #check tie
#flip player
#proceed until game over
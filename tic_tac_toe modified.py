
import random
#make the board
#player moves
#computer moves
#check rows, columns, diagonals
    #win or tie?
#if not win or tie, keep playing

#variables that are defined outside

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
Playing_with_AI = False
center = 4
corners = [0, 2, 6, 8]
edges = [1,3,5,7]
all = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_board():
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print("                                                            ")


def ask_ai():
    still_asking = True
    while still_asking:
        answer = input("Will you be playing with the computer? Select Y/N: ")
        if answer == 'Y' or answer == 'N':
            still_asking = False
            return answer
        else:
            print("Invalid response. Try again.")






def ask_char(): # ask if they will use X or O
    asking_4_character = True
    while asking_4_character:
        character = input("Who do you want to play as? X or O? ")
        if character == 'X' or character == 'O':
            asking_4_character = False
        else:
            print("Invalid character. Try again.")
    return character


def get_pos(char): #get what position on board that program will write to
    asking_4_num = True
    while asking_4_num:
        position = input("Choose a position from 1-9: ")
        if int(position) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Invalid number. Try again.")
        elif board[int(position)-1] != "-":
            print("Cannot overwrite other player's symbol")

        else:
            asking_4_num = False

    board[int(position)-1] = char



def handle_first_turn():
    global Playing_with_AI #allow write access to global variable
    character = ask_char()
    will_computer_play = ask_ai()
    if will_computer_play == 'Y':
        Playing_with_AI = True
        computer_first_turn(character)
        character = flip_char(character)
        return character
    else:
        get_pos(character)
        print_board()
        return character


def computer_first_turn(character): #makes move based on if its moving first or second
    if character == "X": # computer will move second
        get_pos(character) #let the player move first, computer is O
        computer_char = flip_char(character) #get the computers character
        if board[4] == "X":
            corner_select = random.choice(corners)
            board[corner_select] = computer_char
            print_board()
            return
        else:
            board[center] = computer_char
            print_board()
    else:  # computer moves first, player chose O, computer is X
        computer_char = flip_char(character)
        board[4] = computer_char  # mark the center
        print_board()
        return


def human_v_computer(current_char):
    #first working with player's character
    still_playing = True
    while still_playing:
        current_char = flip_char(current_char)
        get_pos(current_char) #human turn
        print_board()
        finished = check_victory_cond(current_char)
        if finished:
            still_playing = False
        current_char = flip_char(current_char)
        computer_turn(current_char)
        print_board()
        finished = check_victory_cond(current_char)
        if finished:
            still_playing = False

def computer_turn(computer_char):
    if computer_char == "X":
        second_turn = True
        while second_turn:
            #if the opponent selects an edge piece
            if board[4] =="X" and board[1] == "O": #if opponent marks an edge
                corner_select_1 = random.choice([6,8])
                board[corner_select_1] = computer_char
                second_turn = False
                return
            elif board[4] == "X" and board[3] =="O":
                corner_select_2 = random.choice([2, 8])
                board[corner_select_2] = computer_char
                second_turn = False
                return
            elif board[4] == "X" and board[5] =="O":
                corner_select_3 = random.choice([0, 6])
                board[corner_select_3] = computer_char
                second_turn = False
                return
            elif board[4] == "X" and board[7] =="O":
                corner_select_4 = random.choice([0, 6])
                board[corner_select_4] = computer_char
                #if the opponent select a corner piece
                second_turn = False
                return
            elif board[4] == "X" and board[0] =="O":
                board[8] = computer_char
                second_turn = False
                return
            elif board[4] == "X" and board[2] == "O":
                board[6] = computer_char
                second_turn = False
                return
            elif board[4] == "X" and board[6] == "O":
                board[2] = computer_char
                second_turn = False
                return
            elif board[4] == "X" and board[8] == "O":
                board[0] = computer_char
                second_turn = False
                return
        if not second_turn:
            continue_turn = True
            while continue_turn:
                rand_select = random.choice(all)
                if board[rand_select] == "-":
                    continue_turn = False
            board[rand_select] = computer_char
            return


    else:  #if computer is O
        second_o_turn = True
        while second_o_turn:
            if board[center] == "X":
                corner_select = random.choice(corners)
                board[corner_select] = False
                second_o_turn = False
                return
            else:
                board[center] = computer_char
                second_o_turn = False
                return
        if not second_o_turn:
            continue_o_turn = True
            while continue_o_turn:
                rand_select = random.choice(all)
                if board[rand_select] == "-":
                    continue_o_turn = False
            board[rand_select] = computer_char




def check_victory_cond(current_char):
    global Playing_with_AI
    row_return = row_check()
    column_return = column_check()
    diagonal_return = diagonal_check()
    tie_return = tie_check()
    if row_return == 1 or column_return == 1 or diagonal_return == 1:
        print("The game has been won by " + current_char)
        Playing_with_AI = False
        return True
    elif tie_return == 1:
        print("The game is a tie.")
        Playing_with_AI = False
        return True

def handle_turn(current_char):
    still_playing = True
    while still_playing:
        if Playing_with_AI:
            human_v_computer(current_char)
            still_playing = False
        else:
            current_char = flip_char(current_char)
            get_pos(current_char)
            print_board()
            row_return = row_check()
            column_return = column_check()
            diagonal_return  = diagonal_check()
            tie_return = tie_check()
            if row_return == 1 or column_return == 1 or diagonal_return == 1:
                print("The game has been won by " + current_char)
                still_playing = False
            elif tie_return == 1:
                print("The game is a tie.")
                still_playing = False


def row_check():
    have_won = 0;
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        have_won = 1;
    return have_won


def column_check():
    have_won = 0;
    column_1 = board[0] == board[3] == board [6] != "-"
    column_2 = board[1] == board[4] == board [7] != "-"
    column_3 =  board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        have_won = 1
    return have_won

def diagonal_check():
    have_won = 0;
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    if diagonal_1 or diagonal_2:
        have_won = 1
    return have_won


def tie_check():
    have_won = 0
    if "-" not in board:
        have_won = 1
    return have_won

def flip_char(current_char):
    if current_char == "X":
        current_char = "O"
    else:
        current_char = "X"
    return  current_char



def play_game():
    print_board()
    character = handle_first_turn()
    handle_turn(character)


play_game()

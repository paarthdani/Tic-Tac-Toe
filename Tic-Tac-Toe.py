# Created By Parth Dani
# Date : 15/10/2017

import random

def main():
    while True:
        the_board = [' '] * 10
        player_letter, computer_letter = input_player_letters()
        turn = who_goes_first()
        print('The ' + turn + ' will go first.')
        game_is_playing = True
        while game_is_playing:
            if turn == 'player':
                gui(the_board)
                move = get_player_move(the_board)
                make_move(the_board, player_letter, move)
                if is_winner(the_board, player_letter):
                    gui(the_board)
                    print('Hooray! You have won the game!')
                    game_is_playing = False
                else:
                    if is_board_full(the_board):
                        gui(the_board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'computer'
            else:
                move = get_computer_move(the_board, computer_letter)
                make_move(the_board, computer_letter, move)
                if is_winner(the_board, computer_letter):
                    gui(the_board)
                    print('The computer has beaten you! You lose.')
                    game_is_playing = False
                else:
                    if is_board_full(the_board):
                        gui(the_board)
                        print('The game is a tie!')
                        break
                    else:
                        turn = 'player'
        if not play_again():
            break


def input_player_letters():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def play_again():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def make_move(board, letter, move):
    board[move] = letter


def is_winner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))


def get_board_copy(board):
    dupe_board = []
    for i in board:
        dupe_board.append(i)
    return dupe_board


def is_space_free(board, move):
    return board[move] == ' '


def get_player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def choose_random_move_from_list(board, movesList):
    possibleMoves = []
    for i in movesList:
        if is_space_free(board, i):
            possibleMoves.append(i)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def get_computer_move(board, computer_letter):
    if computer_letter == 'X':
        player_letter = 'O'
    else:
        player_letter = 'X'

    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, computer_letter, i)
            if is_winner(copy, computer_letter):
                return i

    for i in range(1, 10):
        copy = get_board_copy(board)
        if is_space_free(copy, i):
            make_move(copy, player_letter, i)
            if is_winner(copy, player_letter):
                return i

    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move is not None:
        return move
    
    if is_space_free(board, 5):
        return 5

    return choose_random_move_from_list(board, [2, 4, 6, 8])


def is_board_full(board):
    for i in range(1, 10):
        if is_space_free(board, i):
            return False
    return True


def gui(board):
    print('     |     |')
    print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
    print('     |     |')
    print('-----------------')
    print('     |     |')
    print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
    print('     |     |')


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    main()

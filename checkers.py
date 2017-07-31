#!/usr/bin/python

import json

class ShellUI(object):
    def write(self, text):
        print text

def print_board(board, ui):
    zero = ' '.join(board[0])
    one = ' '.join(board[1])
    two = ' '.join(board[2])
    three = ' '.join(board[3])
    four = ' '.join(board[4])
    five = ' '.join(board[5])
    six = ' '.join(board[6])
    seven = ' '.join(board[7])
    output = '\n'.join([zero, one, two, three, four, five, six, seven])
    ui.write(output)

def pretty_board(board, ui):
    print_board(board, ui)
    ui.write('\n')

def move_piece(y_src, x_src, y_dest, x_dest, board):
    board[y_dest][x_dest] = board[y_src][x_src]
    board[y_src][x_src] = '_'

def remove_piece(y_remove, x_remove, board):
    board[y_remove][x_remove] = '_'

def king_piece(y_king, x_king, board):
    if board[y_king][x_king] == 'r':
        board[y_king][x_king] = 'R'
    if board[y_king][x_king] == 'w':
        board[y_king][x_king] = 'W'

def valid_jump(y_src, x_scr, y_dest, x_dest):
    pass

def load_state(state_file):
    state = json.load(state_file)
    return state

def demo():
    # initialize state by calling function
    f = open('checkers_demo_state.json')
    state = load_state(f)
    f.close()

    ui = ShellUI()

    pretty_board(state['board'], ui)
    # regular move
    move_piece(6, 2, 5, 1, state['board'])
    pretty_board(state['board'], ui)
    # jump move
    move_piece(4, 0, 6, 2, state['board'])
    remove_piece(5, 1, state['board'])
    pretty_board(state['board'], ui)
    # king move
    move_piece(6, 2, 7, 3, state['board'])
    king_piece(7, 3, state['board'])
    pretty_board(state['board'], ui)

def main():
    state = {
        'board': [
            ['_', 'W'] * 4,
            ['W', '_'] * 4,
            ['_', 'W'] * 4,
            ['_'] * 8,
            ['_'] * 8,
            ['R', '_'] * 4,
            ['_', 'R'] * 4,
            ['R', '_'] * 4,
        ]
    }
    ui = ShellUI()

    print_board(board, ui)

if __name__ == '__main__':
    demo()


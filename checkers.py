#!/usr/bin/python

import json

class ShellUI(object):
    def write(self, text):
        print text
    def read(self):
        return raw_input('->')

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

def load_state(state_file):
    state = json.load(state_file)
    return state

def interpret_move_action(user_input, board):
    y_src, x_src, y_des, x_des = user_input.split(' ')
    move_piece(int(y_src), int(x_src), int(y_des), int(x_des), board)

def interpret_king_action(user_input, board):
    y_king, x_king = user_input.split(' ')
    king_piece(int(y_king), int(x_king), board)

def interpret_remove_action(user_input, board):
    y_remove, x_remove = user_input.split(' ')
    remove_piece(int(y_remove), int(x_remove), board)

def interpret_action(user_input, board):
    action, user = user_input.split(None, 1)
    if action == 'move':
        interpret_move_action(user, board)
    if action == 'remove':
        interpret_remove_action(user, board)
    if action == 'king':
        interpret_king_action(user, board)

class CheckersGame(object):
    def turn(self):
        user_input = self.ui.read()
        interpret_action(user_input, self.state['board'])
        pretty_board(self.state['board'], self.ui)
        return False

def main():
    state = {
        'board': [
            ['_', 'w'] * 4,
            ['w', '_'] * 4,
            ['_', 'w'] * 4,
            ['_'] * 8,
            ['_'] * 8,
            ['r', '_'] * 4,
            ['_', 'r'] * 4,
            ['r', '_'] * 4,
        ]
    }
    game = CheckersGame()
    game.ui = ShellUI()
    game.state = state

    pretty_board(state['board'], game.ui)

    for i in range(9999):
        if game.turn():
            break

if __name__ == '__main__':
    main()


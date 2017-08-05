#!/usr/bin/python

import checkers
import json

def main():
    # initialize state by calling function
    f = open('checkers_demo_state.json')
    state = checkers.load_state(f)
    f.close()

    ui = checkers.ShellUI()

    checkers.pretty_board(state['board'], ui)
    # regular move
    checkers.move_piece(6, 2, 5, 1, state['board'])
    checkers.pretty_board(state['board'], ui)
    # jump move
    checkers.move_piece(4, 0, 6, 2, state['board'])
    checkers.remove_piece(5, 1, state['board'])
    checkers.pretty_board(state['board'], ui)
    # king move
    checkers.move_piece(6, 2, 7, 3, state['board'])
    checkers.king_piece(7, 3, state['board'])
    checkers.pretty_board(state['board'], ui)

if __name__ == '__main__':
    main()

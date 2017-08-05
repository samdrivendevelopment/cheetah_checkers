#!/usr/bin/python

import json
import checkers

def main():
    # initialize state by calling function
    f = open('checkers_demo_state.json')
    state = checkers.load_state(f)
    f.close()

    ui = checkers.ShellUI()

    checkers.pretty_board(state['board'], ui)
    # regular move
    checkers.interpret_action('move 6 2 5 1', state['board'])
    checkers.pretty_board(state['board'], ui)
    # jump move
    checkers.interpret_action('move 4 0 6 2', state['board'])
    checkers.interpret_action('remove 5 1', state['board'])
    checkers.pretty_board(state['board'], ui)
    # king move
    checkers.interpret_action('move 6 2 7 3', state['board'])
    checkers.interpret_action('king 7 3', state['board'])
    checkers.pretty_board(state['board'], ui)

if __name__ == '__main__':
    main()

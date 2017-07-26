
from checkers import print_board, move_piece

class TestUI(object):
    def write(self, text):
        self.written = text

def test_print_board():
    ui = TestUI()
    ui.written = None
    board = [['_'] * 8] * 8
    print_board(board, ui)
    checker_board = '\n'.join([' '.join('_' * 8)] * 8)
    return ui.written == checker_board

def test_move_piece():
    y_src = 2
    x_src = 1
    y_dest = 3
    x_dest = 0
    board = [
        ['_', 'w'] * 4,
        ['w', '_'] * 4,
        ['_', 'w'] * 4,
        ['_'] * 8,
        ['_'] * 8,
        ['r', '_'] * 4,
        ['_', 'r'] * 4,
        ['r', '_'] * 4,
    ]
    move_piece(y_src, x_src, y_dest, x_dest, board)
    good_board = [
        ['_', 'w'] * 4,
        ['w', '_'] * 4,
        ['_', '_', '_', 'w', '_', 'w', '_', 'w'],
        ['w', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['r', '_'] * 4,
        ['_', 'r'] * 4,
        ['r', '_'] * 4,
    ]
    return good_board == board

def main():
    print 'start test'

    if not test_print_board():
        print 'print_board failed'

    if not test_move_piece():
        print 'move_piece failed'

    print 'end test'

if __name__ == '__main__':
    main()


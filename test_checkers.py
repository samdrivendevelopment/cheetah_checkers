
from checkers import print_board, move_piece, remove_piece, valid_jump, king_piece, interpret_move_action, interpret_king_action, interpret_remove_action, interpret_action

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

def test_remove_piece():
    y_remove = 4
    x_remove = 3
    board = [
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_', '_', '_', 'r', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]   
    remove_piece(y_remove, x_remove, board)
    good_board = [['_'] * 8] * 8
    return good_board == board

def test_king_move_w():
    board = [
        ['w', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]   
    king_piece(0, 0, board)
    good_board = [
        ['W', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]   
    return good_board == board

def test_king_move_r():
    board = [
        ['r', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    king_piece(0, 0, board)
    good_board = [
        ['R', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    return good_board == board

def test_interpret_move_action():
    board = [
        ['r', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    user_input = '0 0 1 1'
    interpret_move_action(user_input, board)
    good_board = [
        ['_'] * 8,
        ['_', 'r', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    return good_board == board

def test_interpret_king_action():
    board = [
        ['r', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    user_input = '0 0'
    interpret_king_action(user_input, board)
    good_board = [
        ['R', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    return good_board == board

def test_interpret_remove_action():
    board = [
        ['r', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    user_input = '0 0'
    interpret_remove_action(user_input, board)
    good_board = [
        ['_', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    return good_board == board

def test_move_interpret_action():
    board = [
        ['r', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    interpret_action('move 0 0 1 1', board)
    good_board = [
        ['_'] * 8,
        ['_', 'r', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    return good_board == board

def test_remove_interpret_action():
    board = [
        ['r', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    interpret_action('remove 0 0', board)
    good_board = [
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    return good_board == board

def test_king_interpret_action():
    board = [
        ['r', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    interpret_action('king 0 0', board)
    good_board = [
        ['R', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
    ]
    return good_board == board

def main():
    print 'start test'

    if not test_print_board():
        print 'print_board failed'

    if not test_move_piece():
        print 'move_piece failed'

    if not test_remove_piece():
        print 'remove_piece failed'

    if not test_king_move_w():
        print 'king_move failed for w'

    if not test_king_move_r():
        print 'king_move failed for r'

    if not test_interpret_move_action():
        print 'interpret_move_action failed'

    if not test_interpret_king_action():
        print 'interpret_king_action failed'

    if not test_interpret_remove_action():
        print 'interpret_remove_action failed'

    if not test_move_interpret_action():
        print 'move_interpret_action failed'

    if not test_remove_interpret_action():
        print 'remove_interpret_action failed'

    if not test_king_interpret_action():
        print 'king_interpret_action failed'

    print 'end test'

if __name__ == '__main__':
    main()


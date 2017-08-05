
from checkers import print_board, move_piece, remove_piece, king_piece, interpret_move_action, interpret_king_action, interpret_remove_action, interpret_action

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

def make_empty_board():
    return [['_'] * 8] * 8

def make_one_piece_board(y, x, piece):
    board = make_empty_board()
    board[y][x] = piece
    return board

def test_move_piece():
    board = make_one_piece_board(2, 1, 'r')
    move_piece(2, 1, 3, 0, board)
    good_board = make_one_piece_board(3, 0, 'r')
    return good_board == board

def test_remove_piece():
    board = make_one_piece_board(4, 3, 'r') 
    remove_piece(4, 3, board)
    good_board = make_empty_board()
    return good_board == board

def test_king_move_w():
    board = make_one_piece_board(0, 0, 'w') 
    king_piece(0, 0, board)
    good_board = make_one_piece_board(0, 0, 'W')
    return good_board == board

def test_king_move_r():
    board = make_one_piece_board(0, 0, 'r')
    king_piece(0, 0, board)
    good_board = make_one_piece_board(0, 0, 'R')
    return good_board == board

def test_interpret_move_action():
    board = make_one_piece_board(0, 0, 'r')
    user_input = '0 0 1 1'
    interpret_move_action(user_input, board)
    good_board = make_one_piece_board(1, 1, 'r')
    return good_board == board

def test_interpret_king_action():
    board = make_one_piece_board(0, 0, 'r')
    user_input = '0 0'
    interpret_king_action(user_input, board)
    good_board = make_one_piece_board(0, 0, 'R')
    return good_board == board

def test_interpret_remove_action():
    board = make_one_piece_board(0, 0, 'r')
    user_input = '0 0'
    interpret_remove_action(user_input, board)
    good_board = make_empty_board()
    return good_board == board

def test_move_interpret_action():
    board = make_one_piece_board(0, 0, 'r')
    interpret_action('move 0 0 1 1', board)
    good_board = make_one_piece_board(1, 1, 'r')
    return good_board == board

def test_remove_interpret_action():
    board = make_one_piece_board(0, 0, 'r')
    interpret_action('remove 0 0', board)
    good_board = make_empty_board()
    return good_board == board

def test_king_interpret_action():
    board = make_one_piece_board(0, 0, 'r')
    interpret_action('king 0 0', board)
    good_board = make_one_piece_board(0, 0, 'R')
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



from checkers import CheckersGame

class TestUI(object):
    def write(self, text):
        self.written = text
    def read(self):
        fake_user_input = self.user_input
        return fake_user_input

def test_turn_move():
    board = [
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['r', '_', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
        ['_'] * 8,
    ]
    state = {
        'board': board
    }
    game = CheckersGame()
    game.ui = TestUI()
    game.state = state
    game.ui.user_input = 'move 5 0 6 1'
    result = game.turn()
    good_board = [
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_'] * 8,
        ['_', 'r', '_', '_', '_', '_', '_', '_'],
        ['_'] * 8,
    ]
    return result == False and good_board == board

def main():
    print 'start test'

    if not test_turn_move():
        print 'turn failed'

    print 'end test'

if __name__ == '__main__':
    main()

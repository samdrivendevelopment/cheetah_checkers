
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

def move_piece(y_src, x_src, y_dest, x_dest, board):
    board[y_dest][x_dest] = board[y_src][x_src]
    board[y_src][x_src] = '_'

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
    main()


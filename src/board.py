#file with the mathematics logic of Connect four
def create_board() -> list :
    return [[0 for _ in range(7)] for _ in range (6)]

def column_full(board, column):
    pass

def place_token(board, column, player):
    pass

def has_win(board, player):
    pass

def board_full(board):
    pass



# tests

if __name__ == "__main__":
    board = create_board()

    def display_board(board):
        for line in board:
            print(line)

    display_board(board)

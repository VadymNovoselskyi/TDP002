def create_board(height, width):
    board = []
    for h in range(height):
        board.append([])
        for w in range(width):
            board[h].append([])
    return board


def is_empty(board, x, y):
    return not len(board[y][x]) > 0


def add_piece(board, piece, x, y):
    if is_empty(board, x, y):
        board[y][x] = [piece]
    else:
        board[y][x].append(piece)


def remove_piece(board, piece, x, y):
    board[y][x].remove(piece)


def move_piece(board, piece, old_x, old_y, new_x, new_y):
    if is_empty(board, old_x, old_y):
        return
    remove_piece(board, piece, old_x, old_y)
    add_piece(board, piece, new_x, new_y)


def get_pieces(board, x, y):
    return board[y][x]


def print_board(board):
    max_width = 1
    for row in board:
        for cell in row:
            if cell:
                cell_str = ",".join(cell)
                max_width = max(max_width, len(cell_str))

    for row_i in range(len(board)):
        for col_i in range(len(board[row_i])):
            if is_empty(board, col_i, row_i):
                print("■".center(max_width), end=" ")
            else:
                cell_str = ",".join(board[row_i][col_i])
                print(cell_str.center(max_width), end=" ")
        print()


if __name__ == "__main__":
    height = int(input("Height: "))
    width = int(input("Width: "))
    board = create_board(height, width)

    print("Initial board:")
    print_board(board)

    add_piece(board, "X", 0, 0)
    add_piece(board, "Y", 1, 0)
    add_piece(board, "Z1", 2, 0)
    add_piece(board, "Z2", 2, 0)

    print("Board after adding pieces:")
    print_board(board)
    move_piece(board, "X", 0, 0, 0, 1)
    print("Board after moving piece X:")
    print_board(board)
    move_piece(board, "Y", 1, 0, 1, 1)
    print("Board after moving piece Y:")
    print_board(board)
    move_piece(board, "Z1", 2, 0, 1, 2)
    print("Board after moving piece Z:")
    print_board(board)

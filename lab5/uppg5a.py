def is_player(board, x, y):
    return (x, y) in board and "player" in board[(x, y)]

def is_box(board, x, y):
    return (x, y) in board and "box" in board[(x, y)]

def is_wall(board, x, y):
    return (x, y) in board and "wall" in board[(x, y)]

def is_goal(board, x, y):
    return (x, y) in board and "goal" in board[(x, y)]
def is_empty_goal(board, x, y):
    return is_goal(board, x, y) and not (is_player(board, x, y) or is_box(board, x, y))

def get_player_position(board):
    for (x, y) in board.keys():
        if is_player(board, x, y):
            return x, y

def create_board():
    return {}

def create_player(board, x, y):
    if (x, y) in board and not is_empty_goal(board, x, y):
        raise Exception(f"Adding a player onto entity: x: {x}; y: {y}; {board[(x, y)]}, {board}")

    if is_goal(board, x, y):
        board[(x, y)] = ["goal", "player"]
        return
    board[(x, y)] = "player"

def add_box(board, x, y):
    if (x, y) in board and not is_empty_goal(board, x, y):
        raise Exception(f"Adding a box onto entity: x: {x}; y: {y}; {board[(x, y)]}, {board}")

    if is_goal(board, x, y):
        board[(x, y)] = ["goal", "box"]
        return
    board[(x, y)] = "box"

def add_goal(board, x, y):
    if (x, y) in board and not (is_player(board, x, y) or is_box(board, x, y)):
        raise Exception(f"Adding a goal onto entity: x: {x}; y: {y}; {board[(x, y)]}, {board}")

    if is_player(board, x, y):
        board[(x, y)] = ["goal", "player"]
    elif is_box(board, x, y):
        board[(x, y)] = ["goal", "box"]
    else: board[(x, y)] = ["goal"]

def add_wall(board, x, y):
    if (x, y) in board:
        raise Exception(f"Adding a wall onto existing entity: x: {x}; y: {y}; {board[(x, y)]}, {board}")

    board[(x, y)] = "wall"

def get_max_coords(board):
    max_x = 0
    max_y = 0
    for (x, y) in board.keys():
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    return max_x, max_y

def get_symbol(board, x, y):
    if not (x, y) in board:
        return " "
    entity_type = board[(x, y)]
    match entity_type:
        case "player": return "@"
        case "box": return "o"
        case "wall": return "#"
        case ["goal"]: return "."
        case ["goal", "player"]: return "+"
        case ["goal", "box"]: return "*"
        case e: raise Exception(f"Unknown entity_type: {e}")

def sokoban_display(board):
    max_x, max_y = get_max_coords(board)
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            print(get_symbol(board, x, y), end="")
        print()
    return

if __name__ == "__main__":
    board = create_board()
    create_player(board, 0, 0)
    add_box(board, 1, 1)
    add_wall(board, 2, 2)
    add_goal(board, 3, 3)

    add_box(board, 6, 6)
    add_goal(board, 6, 6)
    create_player(board, 7, 7)
    add_goal(board, 7, 7)
    sokoban_display(board)
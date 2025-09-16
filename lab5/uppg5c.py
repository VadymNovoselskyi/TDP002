import uppg5a as uppgA


def is_outside_bounds(board, x, y):
    max_x, max_y = uppgA.get_max_coords(board)
    return x < 0 or x > max_x or y < 0 or y > max_y


def player_can_move(board, x, y, dx, dy):
    next_x, next_y = x + dx, y + dy
    if uppgA.is_box(board, next_x, next_y):
        return box_can_move(board, next_x, next_y, dx, dy)
    return not (
        is_outside_bounds(board, next_x, next_y) or uppgA.is_wall(board, next_x, next_y)
    )


def box_can_move(board, x, y, dx, dy):
    next_x, next_y = x + dx, y + dy
    return not (
        is_outside_bounds(board, next_x, next_y)
        or uppgA.is_wall(board, next_x, next_y)
        or uppgA.is_box(board, next_x, next_y)
    )

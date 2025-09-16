import os
import subprocess
import uppg5a as uppgA
import uppg5b as uppgB
import uppg5c as uppgC


def make_a_move(board, x, y, dx, dy):
    if not uppgC.player_can_move(board, x, y, dx, dy):
        # print("Cant move because of an obstacle") # Doesn't display but idrk atp
        return False, False

    next_x, next_y = x + dx, y + dy
    if uppgA.is_box(board, next_x, next_y):
        uppgA.move_entity(board, "box", next_x, next_y, dx, dy)
        uppgA.move_entity(board, "player", x, y, dx, dy)
        return True, True
    uppgA.move_entity(board, "player", x, y, dx, dy)
    return True, False


def has_won(boxes_coords, goals_coords):
    for box_coord in boxes_coords.keys():
        if not box_coord in goals_coords.keys():
            return False
    return True


if __name__ == "__main__":
    result = subprocess.run(
        ["find", "levels/", "-name", "*.txt"], capture_output=True, text=True
    )
    levels = result.stdout.split("\n")

    print("Welcome to Sokoban, please choose a level:")
    for i in range(len(levels) - 1):
        print(f"{i+1}. {levels[i][7:len(levels[i]) - 4]}")
    level_index = int(input("Choose: ")) - 1

    board = uppgB.sokoban_load(levels[level_index])
    x, y = uppgA.get_player_position(board)
    goals_coords = uppgA.get_goals_coords(board)
    while True:
        os.system("clear")
        uppgA.sokoban_display(board)
        move = input(" \nMake your move (a)left, (d)right, (w)up, (s)down:")
        match move:
            case "a":
                moved_player, moved_box = make_a_move(board, x, y, 0, -1)
                if moved_player:
                    y -= 1
                if moved_box and has_won(uppgA.get_boxes_coords(board), goals_coords):
                    break
            case "d":
                moved_player, moved_box = make_a_move(board, x, y, 0, 1)
                if moved_player:
                    y += 1
                if moved_box and has_won(uppgA.get_boxes_coords(board), goals_coords):
                    break
            case "s":
                moved_player, moved_box = make_a_move(board, x, y, 1, 0)
                if moved_player:
                    x += 1
                if moved_box and has_won(uppgA.get_boxes_coords(board), goals_coords):
                    break
            case "w":
                moved_player, moved_box = make_a_move(board, x, y, -1, 0)
                if moved_player:
                    x -= 1
                if moved_box and has_won(uppgA.get_boxes_coords(board), goals_coords):
                    break
            # case _:
            # print("Please choose either (a)left, (d)right, (w)up, (s)down") # Doesn't display but idrk atp

    os.system("clear")
    uppgA.sokoban_display(board)
    print(
        f"\n\nYou comleted level '{levels[level_index][7:len(levels[level_index]) - 4]}'"
    )

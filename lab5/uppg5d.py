import os
import subprocess
import uppg5a as uppgA
import uppg5b as uppgB
import uppg5c as uppgC

def move_player(board, x, y, dx, dy):
    if not uppgC.player_can_move(board, x, y, dx, dy):
        print("Cant move because of an obstacle") # Doesn't display but idrk atp
        return
    
    next_x, next_y = x + dx, y + dy
    if uppgA.is_box(board, next_x, next_y):
        uppgA.move_entity(board, "box", next_x, next_y, dx, dy)
    uppgA.move_entity(board, "player", x, y, dx, dy)
    
    
if __name__ == "__main__":
    result = subprocess.run(["find", "levels/", "-name", "*.txt"], capture_output=True, text=True)
    levels = result.stdout.split("\n")

    print("Welcome to Sokoban, please choose a level:")
    for i in range(len(levels) - 1):
        print(f"{i+1}. {levels[i][7:len(levels[i]) - 4]}")
    level_index = int(input("Choose: ")) - 1

    board = uppgB.sokoban_load(levels[level_index])
    while True:
        os.system('clear')
        uppgA.sokoban_display(board)
        x, y = uppgA.get_player_position(board)
        move = input(" \nMake your move (a)left, (d)right, (w)up, (s)down:")
        match move:
            case "a":
                move_player(board, x, y, 0, -1)
            case "d":
                move_player(board, x, y, 0, 1)
            case "s":
                move_player(board, x, y, 1, 0)
            case "w":
                move_player(board, x, y, -1, 0)
            case _:
                print("Please choose either (a)left, (d)right, (w)up, (s)down") # Doesn't display but idrk atp
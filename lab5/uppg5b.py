import uppg5a as uppgA

    #####
    #   #
    #o  #
  ###  o##
  #  o o #
### # ## #   ######
#   # ## #####  ..#
# o  o          ..#
##### ### #@##  ..#
    #     #########
    #######


def sokoban_load(file_name):
    board = uppgA.create_board()
    with open(file_name, "r") as file:
        x = 0
        for line in file.readlines():
            y = 0
            for char in line:
                if char == "@":
                    uppgA.create_player(board, x, y)
                elif char == "o":
                    uppgA.add_box(board, x, y)
                elif char == "#":
                    uppgA.add_wall(board, x, y)
                elif char == ".":
                    uppgA.add_goal(board, x, y)
                elif char == "+":
                    uppgA.create_player(board, x, y)
                    uppgA.add_goal(board, x, y)
                elif char == "*":
                    uppgA.add_box(board, x, y)
                    uppgA.add_goal(board, x, y)
                y += 1
            x += 1
    return board

if __name__ == "__main__":
    board = sokoban_load("first_lvl.txt")
    uppgA.sokoban_display(board)
    print("\n\n")

    board = sokoban_load("second_lvl.txt")
    uppgA.sokoban_display(board)
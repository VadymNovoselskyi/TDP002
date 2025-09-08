import os
from uppg2b import *


def main():
    slist = create_shopping_list()

    print("Welcome to the shoppingList, choose one of the following: ")
    while True:
        option = int(
            input(
                """
1. Skriv ut en existerande lista
2. Lägg till ett föremål i listan
3. Ta bort ett föremål ur listan
4. Ändra ett föremål i listan
5. Avsluta
"""
            )
        )
        os.system("clear")

        match option:
            case 1:
                shopping_list(slist)
            case 2:
                shopping_add(slist)
            case 3:
                shopping_remove(slist)
            case 4:
                shopping_edit(slist)
            case 5:
                print("Hejdå!")
                break
            case _:
                print("Invalid input")
        print("\n")


if __name__ == "__main__":
    main()

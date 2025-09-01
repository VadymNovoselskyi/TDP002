def create_shopping_list():
    return ["Kurslitteratur", "Anteckningsblock", "Penna"]


def shopping_list(slist):
    for i in range(0, len(slist)):
        print(f"{i + 1}. {slist[i]}")


def shopping_add(slist):
    new_item = input("What shall be added: ")
    slist.append(new_item)


def shopping_remove(slist):
    remove_index = int(input("which index to remove: ")) - 1
    slist.pop(remove_index)


def shopping_edit(slist):
    edit_index = int(input("Which index to edit: ")) - 1
    edit_value = input(f"What should be in place of \"{slist[edit_index]}\": ")
    slist[edit_index] = edit_value

from pprint import pprint


def link_characters(characters: dict[str, dict[str, int]], char1, char2):
    potions1 = characters[char1]
    potions2 = characters[char2]
    linked_potions = {}
    for potion, amount in potions1.items():
        if potion not in linked_potions:
            linked_potions[potion] = 0
        linked_potions[potion] += amount
    for potion, amount in potions2.items():
        if potion not in linked_potions:
            linked_potions[potion] = 0
        linked_potions[potion] += amount
    characters[char1] = linked_potions
    characters[char2] = linked_potions


def add_item(characters: dict[str, dict[str, int]], name, item, amount):
    potions = characters[name]
    if not potions[item]:
        potions[item] = 0
    potions[item] += amount


def use_item(characters: dict[str, dict[str, int]], name, item, amount):
    potions = characters[name]
    potions[item] -= amount


def unlink_characters(characters: dict[str, dict[str, int]], char1, char2):
    linked_potions = characters[char1]
    potions1 = {}
    potions2 = {}
    for potion, amount in linked_potions.items():
        middle = int(amount / 2)
        potions1[potion] = middle
        potions2[potion] = amount - middle
    characters[char1] = potions1
    characters[char2] = potions2


def print_inventories(characters: dict[str, dict[str, int]]):
    # Get all character names and potion types
    char_names = list(characters.keys())
    potion_types = []
    for inventory in characters.values():
        for potion in inventory.keys():
            if potion not in potion_types:
                potion_types.append(potion)

    # Calculate column widths
    label_width = max(len("Character"), max(len(p) for p in potion_types))
    char_widths = {name: max(len(name), 5) for name in char_names}

    # Print header
    print(f"{'Character':<{label_width}} | ", end="")
    for name in char_names:
        print(f"{name:>{char_widths[name]}}| ", end="")
    print()

    # Print separator
    print(f"{'-' * label_width}-|-", end="")
    for name in char_names:
        print(f"{'-' * char_widths[name]}|-", end="")
    print()

    # Print each potion type
    for potion in potion_types:
        print(f"{potion:<{label_width}} | ", end="")
        for name in char_names:
            value = characters[name].get(potion, 0)
            print(f"{value:>{char_widths[name]}}| ", end="")
        print()

    # Print bottom separator
    print(f"{'-' * label_width}-|-", end="")
    for name in char_names:
        print(f"{'-' * char_widths[name]}|-", end="")
    print()


if __name__ == "__main__":
    # startinventarier
    characters = {
        "Alice": {"HealthPotion": 3, "SpeedPotion": 2, "ShieldPotion": 0},
        "Bob": {"HealthPotion": 1, "SpeedPotion": 0, "ShieldPotion": 0},
        "Clara": {"HealthPotion": 5, "SpeedPotion": 2, "ShieldPotion": 1},
    }

    print("Ursprungligt lÃ¤ge:")
    print_inventories(characters)

    # exempeloperationer
    link_characters(characters, "Alice", "Bob")
    use_item(characters, "Alice", "SpeedPotion", 2)
    add_item(characters, "Bob", "HealthPotion", 1)
    unlink_characters(characters, "Alice", "Bob")
    use_item(characters, "Bob", "HealthPotion", 1)

    print("\nEfter operationer:")
    print_inventories(characters)

from pprint import pprint
import random

suits = ["hearts", "spades"]
values = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
}


def create_deck():
    deck = []
    for suit in suits:
        for key, value in values.items():
            card = {
                "name": f"{key} of {suit}",
                "suit": suit,
                "value": key,
                "numerical_value": value,
            }
            deck.append(card)

    deck.append(
        {"name": "Joker A", "suit": "A", "value": "Joker", "numerical_value": 9999}
    )
    deck.append(
        {"name": "Joker B", "suit": "B", "value": "Joker", "numerical_value": 9999}
    )
    return deck


def count_cards(deck):
    return len(deck)


def shuffle_deck(deck):
    for i in range(len(deck)):
        random_index = random.randint(0, len(deck) - 1)
        temp = deck[i]
        deck[i] = deck[random_index]
        deck[random_index] = temp
    # return deck


def copy_deck(deck):
    return deck.copy()


def get_card_info(card):
    return card.get("suit"), card.get("value"), card.get("numerical_value")


def get_card_at(deck, index):
    return deck[index]


def get_card_index(deck, card_name):
    for i in range(len(deck)):
        if deck[i].get("name") == card_name:
            return i


def remove_index(deck, index):
    if index < len(deck):
        deck.pop(index)


def cut_deck(deck, index):
    return [deck[: index + 1], deck[index + 1 :]]


def compose_deck(_deck1, deck2):
    deck1 = copy_deck(_deck1)
    deck1.extend(deck2)
    return deck1


if __name__ == "__main__":

    # Create deck
    deck = create_deck()
    # pprint(deck)

    # Count deck
    # pprint(count_deck(deck))

    # Randomize deck
    # randomize_deck(deck)
    # pprint(deck)

    # Copy deck
    # new_deck = copy_deck(deck)
    # pprint(new_deck)

    # Getting card by index and card info
    # card_info = get_card_info(get_card_at(deck, 2))
    # pprint(card_info)

    # Getting card info
    # card_index = get_card(deck, "Joker A")
    # pprint(card_index)

    # Removing a card
    # remove_index(deck, 2)
    # remove_index(deck, 40)
    # card_info = get_card_info(get_card_at(deck, 2))
    # pprint(card_info)

    # Cutting deck
    # deck1, deck2 = cut_deck(deck, 10)
    # deck1, deck2 = cut_deck(deck, 27)
    # deck1, deck2 = cut_deck(deck, 40)
    # deck1, deck2 = cut_deck(deck, 0)
    # pprint(len(deck1))
    # pprint(len(deck2))

    # Composing deck
    # composed_deck = compose_deck(deck2, deck1)
    # pprint(composed_deck)

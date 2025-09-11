import random

suits = ["hearts", 'spades']
values = {
    "Jack": 11, 
    "Queen": 12, 
    "King": 13, 
    "Ace": 1, 
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10
}

def create_cards():
    cards = []
    for suit in suits:
        for key, value in values.items():
            card = {"name": f"{key} of {suit}", "suit": suit, "value_name": key, "value": value }
            cards.append(card)

    cards.append({"name": "Joker A", "suit": "A", "value_name": "Joker", "value": 9999})
    cards.append({"name": "Joker B", "suit": "B", "value_name": "Joker", "value": 9999})
    return cards

def count_cards(cards): 
    return len(cards)

def randomize_cards(cards):
    for i in range(len(cards)):
        random_index = random.randint(0, len(cards) - 1)
        temp = cards[i]
        cards[i] = cards[random_index]
        cards[random_index] = temp
    # return cards

def copy_cards(cards):
    return cards.copy()

def get_card_info(card):
    return {"suit": card.get("suit"), "value_name": card.get("value_name")}

def get_card_at(cards, index):
    return cards[index]

def get_card(cards, card_info): 
    for i in range(len(cards)):
        if cards[i].get("suit") == card_info.get("suit") and cards[i].get("value_name") == card_info.get("value_name"):
            return i

def remove_index(cards, index):
    if index < len(cards):
        cards.pop(index)
        
def cut_cards(cards, index):
    return [cards[:index+1], cards[index+1:]]

def compose_cards(cards1, cards2):
    cards1.extend(cards2)
    return cards1

if __name__ == "__main__":

    # Create cards
    cards = create_cards()
    # print(cards)

    # Count cards
    # print(count_cards(cards))

    # Randomize cards
    # randomize_cards(cards)
    # print(cards)

    # Copy cards
    # new_cards = copy_cards(cards)
    # print(new_cards)

    # Getting card by index and card info
    # card_info = get_card_info(get_card_at(cards, 2))
    # print(card_info)

    # Getting card info
    # card_index = get_card(cards, card_info)
    # print(card_index)

    # Removing a card
    # remove_index(cards, 2)
    # remove_index(cards, 40)
    # card_info = get_card_info(get_card_at(cards, 2))
    # print(card_info)

    # Cutting cards
    cards1, cards2 = cut_cards(cards, 10)
    # cards1, cards2 = cut_cards(cards, 27)
    # cards1, cards2 = cut_cards(cards, 40)
    # cards1, cards2 = cut_cards(cards, 0)
    # print(len(cards1))
    # print(len(cards2))

    # Composing cards
    composed_cards = compose_cards(cards2, cards1)
    print(composed_cards)

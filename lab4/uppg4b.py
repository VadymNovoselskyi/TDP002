from email import message
from pprint import pprint
import uppg4a as adt


def card_to_number(card): 
    return card["numerical_value"] + (13 if card["suit"] == "spades" else 0)

def num_to_char(number):
    return chr(number + 64)

def char_to_num(char):
    return ord(char) - 64

def move_card(deck, card_index, move_distance):
    """move_distance > 0 means move go from index 7 to 8 for example"""
    if card_index + move_distance < 0 or card_index + move_distance > adt.count_cards(deck):
        raise Exception(f"Trying to move {card_index} up/down {move_distance} (len is {adt.count_cards(deck)})")

    deck_w_target, deck_after_target = adt.cut_deck(deck, card_index)
    deck_before_target, target = adt.cut_deck(deck_w_target, card_index - 1)

    if move_distance > 0:
        deck_before_target_index, deck_after_target_index = adt.cut_deck(deck_after_target, move_distance - 1)
        deck1 = adt.compose_deck(deck_before_target, deck_before_target_index)
        deck2 = adt.compose_deck(deck1, target)
        deck = adt.compose_deck(deck2, deck_after_target_index)
        return deck
    elif move_distance < 0:
        deck_before_target_index, deck_after_target_index = adt.cut_deck(deck_before_target, adt.count_cards(deck_before_target) + move_distance - 1)
        deck1 = adt.compose_deck(deck_before_target_index, target)
        deck2 = adt.compose_deck(deck1, deck_after_target_index)
        deck = adt.compose_deck(deck2, deck_after_target)
        return deck


def generate_key_letter(deck):
    deck_count = adt.count_cards(deck)

    # Step 2
    jokerA_index = adt.get_card_index(deck, "Joker A")
    if (jokerA_index != deck_count - 1):
        deck = move_card(deck, jokerA_index, 1)
    else:
        deck = move_card(deck, jokerA_index, -(deck_count - 2))
    # pprint(deck)
        
    # Step 3
    jokerB_index = adt.get_card_index(deck, "Joker B")
    if (jokerB_index < deck_count - 2):
        deck = move_card(deck, jokerB_index, 2)
    else:
        deck = move_card(deck, jokerB_index, -(deck_count - 3))
    # pprint(deck)

    # Step 4
    jokerA_index = adt.get_card_index(deck, "Joker A")
    jokerB_index = adt.get_card_index(deck, "Joker B")
    first_joker_index = min(jokerA_index, jokerB_index)
    last_joker_index = max(jokerA_index, jokerB_index)

    deck_A, deck_BC = adt.cut_deck(deck, first_joker_index - 1)
    deck_B, deck_C = adt.cut_deck(deck_BC, last_joker_index - first_joker_index)
    deck_CB = adt.compose_deck(deck_C, deck_B)
    deck = adt.compose_deck(deck_CB, deck_A)
    # pprint(deck)

    # Step 5
    last_card_value = card_to_number(adt.get_card_at(deck, deck_count - 1))
    top_deck, bottom_deck = adt.cut_deck(deck, last_card_value - 1)
    bottom_deck, bottom_card = adt.cut_deck(bottom_deck, adt.count_cards(bottom_deck) - 2)
    deck_but_bottom = adt.compose_deck(bottom_deck, top_deck)
    deck = adt.compose_deck(deck_but_bottom, bottom_card)

    # Step 6
    first_card_value = card_to_number(adt.get_card_at(deck, 0))
    if first_card_value > deck_count:
        return deck, ''
    key_value = card_to_number(adt.get_card_at(deck, first_card_value))
    if key_value > deck_count:
        return deck, ''
    return deck, num_to_char(key_value)

def solitaire_keystream(length, deck):
    key = ""
    while len(key) < length:
        deck, letter = generate_key_letter(deck)
        key += letter
    return key

def encrypt_message(message, deck):
    key = solitaire_keystream(len(message), deck)
    numerical_key = [char_to_num(c) for c in key]
    numerical_message = [char_to_num(c) for c in message]
    numerical_enc_message = []
    for i in range(len(numerical_key)):
        value = numerical_key[i] + numerical_message[i]
        numerical_enc_message.append(value if value < 27 else value % 26)
    enc_message_list = [num_to_char(n) for n in numerical_enc_message]

    return "".join(enc_message_list)

def decrypt_message(enc_message, deck):
    key = solitaire_keystream(len(enc_message), deck)
    numerical_key = [char_to_num(c) for c in key]
    numerical_enc_message = [char_to_num(c) for c in enc_message]
    numerical_decrypted_message = []
    for i in range(len(numerical_key)):
        value =  numerical_enc_message[i] - numerical_key[i]
        numerical_decrypted_message.append(value if value > 0 else value % 26)
    decrypted_message_list = [num_to_char(n) for n in numerical_decrypted_message]

    return "".join(decrypted_message_list)


if __name__ == "__main__":
    message_utf = input("Input your message: ")
    message = ""
    for char in message_utf:
        if (ord(char) > ord("A") and ord(char) < ord("Z")) or (ord(char) > ord("a") and ord(char) < ord("z")):
            message += char

    deck = adt.create_deck()
    adt.shuffle_deck(deck)

    # Encrypt
    enc_message = encrypt_message(message.upper(), adt.copy_deck(deck))
    print(enc_message)

    # Decrypt
    decrypted_message = decrypt_message(enc_message, adt.copy_deck(deck))
    print(decrypted_message)

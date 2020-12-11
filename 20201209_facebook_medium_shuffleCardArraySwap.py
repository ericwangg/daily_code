# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a function that generates perfectly random numbers between 1 and k (inclusive), where k is an input,
# write a function that shuffles a deck of cards represented as an array using only swaps.
#
# It should run in O(N) time.
#
# Hint: Make sure each one of the 52! permutations of the deck is equally likely.

import random

CARDS_NUM = 52
SUITS = ["Spades", "Hearts", "Diamonds", "Clubs"]

def card_index():
    CARDS_INDEX = {}
    for i in range(CARDS_NUM):
        if ((i+1)/13) <= 1:
            CARDS_INDEX[i] = "{} {}".format(SUITS[0], i % 13 + 1)
        if 1 < ((i+1)/13) <= 2:
            CARDS_INDEX[i] = "{} {}".format(SUITS[1], i % 13 + 1)
        if 2 < ((i+1)/13) <= 3:
            CARDS_INDEX[i] = "{} {}".format(SUITS[2], i % 13 + 1)
        if 3 < ((i+1)/13) <= 4:
            CARDS_INDEX[i] = "{} {}".format(SUITS[3], i % 13 + 1)
    return CARDS_INDEX

def random_number(k):
    return random.randint(0,k)

def shuffle_cards():
    cards = [x for x in range(CARDS_NUM)]
    for pos_cur in cards:
        pos_next = pos_cur + random_number(CARDS_NUM - pos_cur - 1)
        swap = cards[pos_next]
        cards[pos_next] = cards[pos_cur]
        cards[pos_cur] = swap
    return cards

def shuffled_card_names():
    SHUFFLED_DECK = [x for x in range(CARDS_NUM)]
    for i, card_val in enumerate(shuffle_cards()):
        SHUFFLED_DECK[i] = card_index().get(card_val)
    return SHUFFLED_DECK


# Got fancy by creating a card index that maps a card number to card name, say 24 is "Queen of Hearts" or "Hearts 12"
if __name__ == '__main__':
    print(card_index())
    # print(shuffle_cards())
    print(shuffled_card_names())

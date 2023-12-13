import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

deck = []

for suit in suits:
    for number in numbers:
        deck.append(f"{numbers} of {suits}")

random.shuffle(deck)

def deal_cards(deck, hand):
    card = deck.pop()
    hand.append(card)






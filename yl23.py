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


def hand_value(hand):
    value = 0
    has_ace = False

    for card in hand:
        rank = card.split()[0]

        if rank.isdigit():
            value += int(rank)
        elif rank in ["Jack", "Queen", "King"]:
            value += 10
        elif rank == "Ace":
            has_ace = True
            value += 11
    
    if has_ace and value > 21:
        value -= 10
    
    return value

player_hand = []
dealer_hand = []

deal_cards(deck, player_hand)
deal_cards(deck, player_hand)
deal_cards(deck, dealer_hand)
deal_cards(deck, dealer_hand)

while True:
    print(f'Player hand: {player_hand}({hand_value(player_hand)})')
    print(f'Dealer hand: [{dealer_hand[0]}, <face down>]')

    if hand_value(player_hand) > 21:
        print("Player busts")
        break

    action = input("Hit or stand? ")

    if action.lower() == "hit":
        deal_cards(deck, player_hand)
    else:
        break

    print(f'Player hand: {player_hand}({hand_value(player_hand)})')
    print(f'Dealer hand: {dealer_hand}({hand_value(dealer_hand)})')

    if hand_value(player_hand) > 21:
        print("Player busts")
    elif hand_value(dealer_hand) > 21:
        print("Dealer busts, you win")
    elif hand_value(player_hand) > hand_value(dealer_hand):
        print("Player wins")
    elif hand_value(player_hand) < hand_value(dealer_hand):
        print("Dealer wins")
    else:
        print("Push")




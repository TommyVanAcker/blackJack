import art
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player_cards = []
dealer_cards = []

def add_card(total, deck, cards):
    for i in range(total):
        card= random.choice(cards)
        deck.append(card)


def blackjack():
    print(f'your cards: {player_cards}, current score: {sum(player_cards)}')
    print(f"Computer's first card: {dealer_cards[0]}")
    deal = input("Type 'y' to get another card, type 'n' to pass:")
    if deal == "y":
        add_card(1, player_cards, cards)


print(art.logo)
game = input("Do you want to play a game of Blackjack? (y/n): ").lower()
if game == "y":
    add_card(2, player_cards, cards)
    add_card(1, dealer_cards, cards)
    while True:
        blackjack()

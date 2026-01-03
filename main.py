import art
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

player_cards = []
dealer_cards = []

def deal_2_cards(deck):
    for i in range(2):
        card = random.choice(deck)
        player_cards.append(card)

def deal_computer_cards(deck):
    card = random.choice(deck)
    dealer_cards.append(card)

def blackjack():
    pass


print(art.logo)
game = input("Do you want to play a game of Blackjack? (y/n): ").lower()
if game == "y":
    deal_2_cards(cards)
    deal_computer_cards(cards)

print(f'your cards: {player_cards}, current score: {sum(player_cards)}')
print(f"Computer's first card: {dealer_cards[0]}")
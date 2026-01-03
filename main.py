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
    game_over = False
    while game_over != True:
        deal = input("Type 'y' to get another card, type 'n' to pass:")
        if deal == "y":
            add_card(1, player_cards, cards)
            if sum(player_cards) > 21:
                for card in player_cards:
                    if card == 11:
                        player_cards.remove(11)
                        player_cards.append(1)
            print(f'your cards: {player_cards}, current score: {sum(player_cards)}')
            print(f"Computer's first card: {dealer_cards[0]}")
            if sum(player_cards) >= 21:
                game_over = True
                decide_winner()
        elif deal == "n":
            while sum(dealer_cards) < 17:
                add_card(1, dealer_cards, cards)
            game_over = True
            decide_winner()

def decide_winner():
    total_player = sum(player_cards)
    total_dealer = sum(dealer_cards)
    print(f'your final hand: {player_cards}, final score: {total_player}')
    print(f"Computer's final hand: {dealer_cards}, final score: {total_dealer}")
    if total_player > 21:
        print("You went over. You lose")
    elif total_dealer > 21:
        print("Dealer went over, you win")
    elif total_player > total_dealer:
        print("you win")
    elif total_player == total_dealer:
        print("It's a draw")
    else:
        print("Dealer wins, you lose")
    start_game()


print(art.logo)
def start_game():
    global player_cards
    global dealer_cards
    player_cards = []
    dealer_cards = []
    game = input("Do you want to play a game of Blackjack? (y/n): ").lower()
    if game == "y":
        add_card(2, player_cards, cards)
        add_card(1, dealer_cards, cards)
        blackjack()

start_game()
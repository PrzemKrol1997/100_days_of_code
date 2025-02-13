# game deals us 2 cards
# game deals opponent 1 card
# We decide if we draw another or pass
# If computer has less than as it draws cards
# The winner is a person ho has the highest hand, but going over 21 loses a game
# If player or computer has any ace(11) and goes over 21 ace is converted to 1

import random
from art import logo


list_of_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
def get_card():
    return list_of_cards.pop(random.randint(0, len(list_of_cards)-1))


def draw_player(hand, ace):
    hand_sum = sum(hand)
    print(f"Your hand: {hand}, your summ ={hand_sum}")
    if hand_sum >= 21:
        if ace > 1:
            hand[hand.index(11)] = 1
            hand_sum -= 10
            ace -=1
            print("You had over 21, ace changed from 11 to 1")
    do_you_draw =input(f'Do you wont to draw "y" or not "n"?: ')
    if do_you_draw == "y":
        card =get_card()
        hand.append(card)
        hand_sum = sum(hand)
        if card == 11:
            ace += 1
        if hand_sum < 21:
            draw_player(hand, ace)
        elif hand_sum >= 21:
            if ace > 1:
                hand[hand.index(11)] = 1
                hand_sum -= 10
                ace -=1
                print("You had over 21, ace change to 1")
                draw_player(hand, ace)
        else:
            return hand
    return hand

def draw_opponent(hand, ace):
    hand_sum = sum(hand)
    if hand_sum < 17:
        card = get_card()
        if card == 11:
            ace += 1
        hand.append(card)
        draw_opponent(hand, ace)
    elif hand_sum > 21:
        if ace > 1:
            hand[hand.index(11)] = 1
            hand_sum -= 10
            ace -= 1
            draw_opponent(hand, ace)
        return hand
    return hand


def blackjack():
    print (logo + "\n")
    player_hand =[get_card(),get_card()]
    player_hand_sum = sum(player_hand)
    ace_player =0
    for card in player_hand:
        if card == 11:
            ace_player += 1
    opponent_hand =[get_card(), get_card()]
    if player_hand_sum == 21 and len(player_hand) ==2:
        print("\n****Blackjack, You win!****\n")
        print(f"Opponent had: {opponent_hand}\n")
        exit()
    ace_opponent=0
    for card in opponent_hand:
        if card == 11:
            ace_opponent += 1
    print(f"Opponent first card: {opponent_hand[0]} \n")
    player_hand=draw_player(player_hand, ace_player)
    player_hand_sum = sum(player_hand)
    if len(player_hand) > 2:
        print(f"Your hand: {player_hand}, your summ ={player_hand_sum}")
    if player_hand_sum >21:
        print("\n****Bust, You lose****\n")
        print(f"Opponent had: {opponent_hand}\n")
    else:
        opponent_hand = draw_opponent(opponent_hand,ace_opponent)
        opponent_hand_sum = sum(opponent_hand)
        print(f"Opponent hand: {opponent_hand}, opponent summ = {opponent_hand_sum}")
        if opponent_hand_sum == 21 and len(opponent_hand) == 2:
            print("\n****opponent had blackjack, You lose****\n")
            print(f"Opponent had: {opponent_hand}\n")
        elif opponent_hand_sum > 21:
            print("\n****Opponent busted, You win!****\n")
        elif player_hand_sum == opponent_hand_sum:
            print("\n****It is a draw****\n")
        elif player_hand_sum > opponent_hand_sum:
            print("\n****You win!****\n")
        else:
            print("\n****You lose****\n")

play_agin ="y"
while play_agin == "y":
    blackjack()
    play_agin=input('\nDo you want to play agin "y" or "n"?: ').lower()
    if play_agin == "y":
        print("\n" * 40)
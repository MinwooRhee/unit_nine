# Minwoo Rhee
# 2018 11 30
# assignment_nine
# card game compare, 5 rounds, 2 players

import deck


def deal_cards(deck1):
    """
    make lists for each players, draws five cards for each and append cards to the list
    :param deck1: deck to draw card from
    :return: cards drawn for player 1, cards drawn for player 2
    """

    player1_cards = []
    player2_cards = []

    for x in range(5):
        player1_cards.append(deck1.draw_a_card())
        player2_cards.append(deck1.draw_a_card())

    return player1_cards, player2_cards


def compare_cards(card1, card2):
    """
    compare two cards to determine who wins
    :param card1: player 1 card
    :param card2: player 2 card
    :return: if player 1 wins, "Player One". if player 2 wins, "Player Two"
    """

    if card1.compared_to(card2) == card1:
        return "Player One"
    else:
        return "Player Two"


def main():
    """
    draw cards, compare them and determine which player wins by comparing score variables
    :return: None
    """

    deck1 = deck.Deck()

    deck1.shuffle()

    player1_score = 0
    player2_score = 0

    player1_cards, player2_cards = deal_cards(deck1)

    for x in range(0, 5):

        print("Player one has", player1_cards[x])
        print("Player two has", player2_cards[x])

        if compare_cards(player1_cards[x], player2_cards[x]) == "Player One":
            player1_score += 1
            print("Player One wins this round!")
        else:
            player2_score += 1
            print("Player Two wins this round!")

        print(" ")

    if player1_score > player2_score:
        print("Player One wins the game!")
    else:
        print("Player Two wins the game!")


main()


import deck


def main():

    deck1 = deck.Deck()

    for card in deck1.deck_of_cards:

        print(card)

    deck1.shuffle()
    print(" ")

    for card in deck1.deck_of_cards:

        print(card)

    playerCards = []
    dealerCards = []

    for x in range(5):
        playerCards.append(deck1.draw_a_card())
        dealerCards.append(deck1.draw_a_card())

    print(playerCards)
    print(dealerCards)


main()

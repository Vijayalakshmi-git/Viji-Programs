# importing random
import random

# creating a class for a new card with attributes self,suite,value																																																																																					`
class Cards:
    def __init__(self, suite, value,):
        self.suite = suite
        self.value = value

# function to print the card
    def show(self):
        print("{} of {}".format(self.value, self.suite))

# creating a Deck class for 4 suits of cards
class Deck:
    def __init__(self):
        self.cards = []
        self.build()

# creating functions to build and show the cards
    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Cards(s, v))

    def show(self):
        for c in self.cards:
            c.show()

# function for shuffling cards
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

# function to draw a card random
    def drawCard(self):
        return self.cards.pop()

    def draw(self, deck):
        self.hand.append(deck.drawcard())
        return self

# creating a class for players
class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

# function to draw the hand
    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

deck = Deck()
deck.shuffle()

player_1 = Player('Viji')
player_1.draw(deck)
print('Viji: ')
player_1.showHand()

player_2 = Player('Lakshmi')
player_2.draw(deck)
print('Lakshmi: ')
player_2.showHand()


import random


class Card:
    suit_names = ["Spades", "Hearts", "Diamonds", "Clubs"]
    rank_names = ['None', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{} of {}'.format(Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return ",".join(res)

    def pop_card(self):
        return self.cards.pop()

    def add_card(self, card):
        self.cards.append(card)

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    def __init__(self, label=''):
        super().__init__()
        self.cards = []
        self.label = label

    def find_defining_class(obj, method_name):
        for ty in type(obj).mro():
            print(ty)


class PokerHand(Hand):
    def suit_hist(self):
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False


queen_of_diamonds = Card(2,12)
print(queen_of_diamonds)

card1 = Card(2,11)
print(card1)
print("------------------------------------")

deck = Deck()
deck.pop_card()
deck.add_card(card1)
deck.shuffle_cards()
print(deck)
print("------------------------------------")

hand = Hand('new hand')
print(hand.cards)
print(hand.label)
card2 = deck.pop_card()
hand.add_card(card2)
print(hand)
print("------------------------------")

pokerhand = PokerHand()
pokerhand.
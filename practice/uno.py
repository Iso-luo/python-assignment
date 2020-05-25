import random


class Card:
    Colors = ["None", "red", "yellow", "blue", "green"]
    Ranks01 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "skip", "reverse", "draw_two"]
    Ranks02 = ["Wild", "Wild draw four"]

    def __init__(self, color=0, rank1=0, rank2=0):
        self.color = color
        self.rank1 = rank1
        self.rank2 = rank2

    def __str__(self):
        if self.color != 0:
            res = "{} with {}".format(Card.Ranks01[self.rank1], Card.Colors[self.color])
        else:
            res = "{}".format(Card.Ranks02[self.rank2])
        return res


class Deck:
    def __init__(self):
        self.cards = []
        for color in range(1, 5):
            card = Card(color, rank1=0, rank2=0)
            self.cards.append(card)
            for rank1 in range(1, 13):
                card = Card(color, rank1, rank2=0)
                self.cards.append(card)
                self.cards.append(card)
        for rank2 in range(2):
            for i in range(4):
                card = Card(0, 0, rank2)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return ",\n".join(res)

    def get_list(self):
        r = self.__str__().split(",")
        return r


c = Card(0, 12, 0)
print(c)
deck = Deck()
print(deck)
r1 = deck.get_list()
print(len(r1))

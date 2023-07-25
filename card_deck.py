import collections

Card = collections.namedtuple('Card', ('rank', 'suit'))

class Deck:
    ranks = [str(a) for a in range(2,11)] + list("JQKA")
    suits = ['spades', 'diamonds', 'hearts', 'clubs']

    def __init__(self):
        self._cards = [Card(rank, suite) for suite in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, idx):
        return self._cards[idx]


my_deck = Deck()

print(my_deck[:5])
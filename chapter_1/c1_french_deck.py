# Use collections for your project it is the Pythonic-way.
import collections


# It is use for creating the class include only attributes without methods.
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    # [need know] There are 'dunder-methods' of the class:
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

"""
===================
=== My comments ===
===================

Try: 
    >>> from c1_french_deck import *
    >>> beer_card = Card(rank='7', suit='diamonds')
    >>> beer_card
    Card(rank='7', suit='diamonds')
    
    >>> deck = FrenchDeck()
    >>> len(deck)
    52
    
    >>> from random import choice                                   # [need know] maybe useful
    >>> choice(deck)
    Card(rank='9', suit='spades')
    
    >>> Card('Q', 'hearts') in deck
    True
    >>> Card('Q', 'beasts') in deck
    False



"""

# -*- coding: utf-8 -*-

cards = {'cards': '23456789TJQKA', 'suite': 'SHCD'}


class Card(object):

    def __init__(self, card):
        if len(card) != 2 or card[0] not in cards.get('cards') or card[1] not in cards.get('suite'):
            raise ValueError
        self.card = (card[0], card[1])

    def __repr__(self):
        return '<Card: {{ value: {}, suit: {} }}>'.format(self.card[0], self.card[1])



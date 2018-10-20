# -*- coding: utf-8 -*-
from poker.exceptions import DuplicatedCardError
from poker.card import Card


class Hand(object):
    # import pdb;
    # pdb.set_trace()

    def __init__(self, hand):
        result = set(list(hand.split(' ')))
        if len(result) < 5:
            raise DuplicatedCardError

    def rank(self):
        pass


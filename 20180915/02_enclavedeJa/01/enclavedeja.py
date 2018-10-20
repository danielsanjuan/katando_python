#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_price(seasons):
    if len(seasons) > 4:
        return 5 * len(seasons) * 0.8
    elif len(seasons) > 2:
        return 5 * len(seasons) * 0.9
    else:
        return 5 * len(seasons)

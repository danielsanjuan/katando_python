#!/usr/bin/env python
# -*- coding: utf-8 -*-

def get_price(seasons):
    season_price = {'prices': {'0': 2.5, '1': 3, '2': 3.5, '3': 4, '4': 4.5, '5': 5}, 'discounts': {'3': 0.9, '4': 0.8, '5': 0.7}}
    return round(divide_list_by_season(seasons, season_price), 2)

def divide_list_by_season(seasons, season_price):
    aux = []
    collection = []
    for season in seasons:
        if season == 5:
            collection.append([season])
        elif season in aux:
            collection.append(aux)
            aux = [season]
        else:
            aux.append(season)
    collection.append(aux)
    return get_total_price(collection, season_price)

def get_total_price(collection, season_price):
    return sum(get_season_price(seasons, season_price) * get_discount(seasons, season_price) for seasons in collection)

def get_season_price(seasons, season_price):
    return sum(season_price['prices'][str(season)] for season in seasons)

def get_discount(seasons, season_price):
    return season_price['discounts'][str(len(seasons))] if str(len(seasons)) in season_price['discounts'] else 1

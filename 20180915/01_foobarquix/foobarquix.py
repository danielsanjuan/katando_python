#!/usr/bin/env python
# -*- coding: utf-8 -*-

def foobarquix(number):
    dividers = {3:'Foo', 5:'Bar', 7:'Quix'}
    res = divisible(number, dividers)
    return is_digit(res, dividers) if res.isdigit() else is_digit(number, dividers, res)

def divisible(number, dividers):
    res = ''
    for key,value in dividers.items():
        if number % key == 0:
            res = res + value
    return res if res else str(number)
    
def is_digit(number, dividers, res=None):
    result = res if res else ''
    for key, value in dividers.items():
        for x in str(number):
            if x == str(key):
                result += value
    return result if result else str(number)

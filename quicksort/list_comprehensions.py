#!/usr/bin/env python
# -*- coding: utf-8 -*

from random import randint


def qsort1(list):
    """Quicksort using list comprehensions"""
    if list == []:
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater


l = [randint(0, 100) for i in range(0, 10)]

r = qsort1(l)

print(r)

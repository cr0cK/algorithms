#!/usr/bin/env python
# -*- coding: utf-8 -*-

# http://en.wikipedia.org/wiki/Insertion_sort

from random import randint


def sort(alist):
    for i in xrange(0, len(alist)):
        if i > 0 and alist[i] < alist[i - 1]:
            j = i
            while j > 0 and alist[j - 1] > alist[i]:
                j -= 1

            alist.insert(j, alist.pop(i))

mylist = [randint(1, 50) for i in range(0, 20)]
print(mylist)

sort(mylist)

print(mylist)

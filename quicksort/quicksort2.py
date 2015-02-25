#!/bin/python
#*-* encoding: utf-8 *-*


def printInt(l):
    print(' '.join([str(i) for i in l]))


def quickSort(ar):
    if not len(ar):
        return []

    p = ar[0]

    sublist_left = []
    sublist_right = []

    for i in ar:
        if i < p:
            sublist_left.append(i)

        elif i > p:
            sublist_right.append(i)

    r = quickSort(sublist_left) + [p] + quickSort(sublist_right)

    if len(r) > 1:
        printInt(r)

    return r

# ar = [int(i) for i in raw_input().strip().split()]
ar = [5, 8, 1, 3, 7, 9, 2]
m = len(ar)
quickSort(ar)

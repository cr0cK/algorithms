#!/bin/python
#*-* encoding: utf-8 *-*


def partition(ar):
    if not len(ar):
        return []

    p = ar[0]

    sublist_left = []
    sublist_right = []

    for i in ar:
        if i < p:
            sublist_left.append(i)
        else:
            sublist_right.append(i)

    return sublist_left + sublist_right

# ar = [int(i) for i in raw_input().strip().split()]
ar = [4, 5, 3, 7, 2]
m = len(ar)
r = partition(ar)

print(' '.join([str(i) for i in r]))

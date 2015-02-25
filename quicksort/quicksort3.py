#!/bin/python
#*-* encoding: utf-8 *-*
#
# Quicksort inplace.


import random


def quickSort(aList):
    _quicksort(aList, 0, len(aList) - 1)


def _quicksort(aList, first, last):
    if first < last:
        pivot = partition(aList, first, last)
        _quicksort(aList, first, pivot - 1)
        _quicksort(aList, pivot + 1, last)


def partition(aList, first, last):
    for i in range(first, last):
        if aList[i] <= aList[last]:
            if i != first:
                swap(aList, i, first)
            first += 1

    swap(aList, first, last)
    return first


def swap(A, x, y):
    A[x], A[y] = A[y], A[x]


# ar = [int(i) for i in raw_input().strip().split()]
ar = [1, 3, 9, 8, 2, 7, 5]
# ar = []
# for i in range(0, 100):
#     ar.append(random.randint(1, 50))

print(ar)

# ar = [1, 3, 2]
quickSort(ar)
print(ar)

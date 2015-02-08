#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.hackerrank.com/challenges/lonely-integer


def lonelyinteger(ints):
    counts = {}
    for i in range(0, len(ints)):
        value = ints[i]
        counts.setdefault(value, 0)
        counts[value] += 1

    return ([value for (value, count)
            in counts.iteritems() if count < 2] or [None])[0]


def lonelyinteger2(a):
    answer = 0
    for x in a:
        answer = answer ^ x
    return answer

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print(lonelyinteger(b))
    print(lonelyinteger2(b))

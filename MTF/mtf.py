#!/bin/env python

# move to front
# http://en.wikipedia.org/wiki/Move-to-front_transform


def mtf(word):
    letters = []
    indexes = []

    for c in word:
        if c not in letters:
            letters.append(c)

    letters.sort()

    for c in word:
        i = letters.index(c)
        indexes.append(i)
        letters.insert(0, letters.pop(i))

    letters.sort()
    return (indexes, letters)


def reverse_mtf(tuple_):
    indexes, letters = tuple_
    word = []

    for i in indexes:
        word.append(letters[i])
        letters.insert(0, letters.pop(i))

    return ''.join(word)

r = mtf('bananaaa')
s = reverse_mtf(r)

print(r)
# ([1, 1, 2, 1, 1, 1, 0, 0], ['a', 'n', 'b'])

print(s)
# bananaaa

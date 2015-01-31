#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division

from pprint import pprint


class SimpleHashTable(object):
    def __init__(self, size):
        self._size = size
        self._table = [[]]

    def add(self, index, value):
        h = self._hash(index)
        self._table[h].append((index, value))

    def remove(self, index):
        h = self._hash(index)
        values = self._table[h]

        for i in range(len(values) - 1):
            value = values[i]
            if value[0] == index:
                values.pop(i)

    def get(self, index):
        h = self._hash(index)
        values = self._table[h]

        for value in values:
            if value[0] == index:
                return value[1]

    def get_lf(self):
        nb_values = sum([len(list_) for list_ in self._table])
        return nb_values / self._size

    def _hash(self, index):
        if isinstance(index, str):
            index = sum([ord(c) for c in index])

        return index % len(self._table)


table = SimpleHashTable(10)
table.add('key1', 'foo')
table.add('key2', 'bar')
table.add('azeaze', 'bar2')
table.add(50, 42)
table.add(60, 422)

print(table.get('key1'))
print(table.get('key2'))
print(table.get('azeaze'))
print(table.get(50))
print(table.get(60))
print(table.get_lf())

table.remove(50)
print(table.get_lf())

print('---')
pprint(table._table)

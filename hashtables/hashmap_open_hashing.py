#!/usr/bin/env python
# -*- coding: utf-8 -*-

# hashmap open hashing
# Use a linked list in each bucket.

# TODO: resize when LF > 0.75

from random import randint


class Value(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap(object):
    MIN_BUCKETS = 5

    def __init__(self):
        self._list = [None] * self.MIN_BUCKETS

    def add(self, key, value):
        index = self._hash(key)

        value_obj = Value(key, value)

        if self._list[index] is None:
            self._list[index] = value_obj
        else:
            # chain the value object
            current_value_obj = self._list[index]
            while current_value_obj.next is not None:
                current_value_obj = current_value_obj.next

            current_value_obj.next = value_obj

    def get(self, key):
        ret = None

        index = self._hash(key)

        try:
            if self._list[index] is not None:
                value_obj = self._list[index]

                if value_obj.next is None:
                    ret = value_obj.value
                else:
                    while True:
                        if key == value_obj.key:
                            ret = value_obj.value
                            break

                        if value_obj.next is None:
                            break

                        value_obj = value_obj.next

        except KeyError:
            pass

        return ret

    def remove(self, key):
        index = self._hash(key)

        if self._list[index] is not None:
            previous_search_obj = None
            value_obj = self._list[index]

            while True:
                if key == value_obj.key:
                    if previous_search_obj is not None:
                        previous_search_obj.next = value_obj.next
                    else:
                        self._list[index] = value_obj.next

                    del value_obj
                    break

                if value_obj.next is None:
                    break

                previous_search_obj = value_obj
                value_obj = value_obj.next

        else:
            pass

    def _hash(self, key):
        if not isinstance(key, str):
            raise Exception('The key should be a string.')

        index = sum([ord(c) for c in key])

        return index % (self.MIN_BUCKETS - 1)


# create hashmap
h = HashMap()


# insert values in the hashmap
values = [
    ('one', 'un'),
    ('two', 'deux'),
    ('three', 'trois'),
    ('four', 'quatre'),
    ('five', 'cinq'),
    ('six', 'six')
]

for words in values:
    h.add(words[0], words[1])

print(h.get('five'))

# # retrieve values
# result = h.get('three')
# print(result)

# result = h.get('five')
# print(result)

# # remove a value
# h.remove('three')
# result = h.get('three')
# print(result)

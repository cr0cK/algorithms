#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Given a linked list, swap every two adjacent nodes and return its head.

# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.

# Your algorithm should use only constant space. You may not modify the values
# in the list, only nodes itself can be changed.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def deserialize(self):
        values = []
        node = self
        while node:
            values.append(node.val)
            node = node.next

        return values


class Solution(object):
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        root = ListNode(0)
        root.next = head
        prev = root

        while True:
            # 2 > 1 > 3 > 4

            # next_ => 3
            next_ = head.next.next

            # newhead => 2
            newhead = head.next

            # newhead.next => 1
            newhead.next = head

            # prev.next => 2
            prev.next = newhead

            # head.next => 3
            head.next = next_

            # set new pairs for the next loop
            head = next_
            prev = newhead.next

            if not head or not head.next:
                break

        return root.next


def createList(l):
    head = None
    prevNode = None

    for value in l:
        node = ListNode(value)

        if not head:
            head = node

        if prevNode:
            prevNode.next = node

        prevNode = node

    return head


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
chain = createList(l)

print(chain.deserialize())

s = Solution()
chain = s.swapPairs(chain)

print('--')

print(chain.deserialize())

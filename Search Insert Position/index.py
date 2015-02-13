#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.

# You may assume no duplicates in the array.

# Here are few examples.
# [1,3,5,6], 5 → 2
# [1,3,5,6], 2 → 1
# [1,3,5,6], 7 → 4
# [1,3,5,6], 0 → 0

from profilehooks import profile


class Solution(object):
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    @profile
    def searchInsert(self, A, target):
        """
        Binary seach.
        O(log(n))
        """

        A = A[:]

        if target not in A:
            A.append(target)
            A.sort()

        left, right = 0, len(A) - 1
        found = False

        if len(A) <= 2:
            if A[0] == target:
                return 0
            if A[1] == target:
                return 1
            return None

        while left <= right and not found:
            middle = (left + right) / 2

            # because the result of the division is floored
            if left and middle == left:
                middle += 1

            value = A[middle]

            if value == target:
                found = True
                break
            else:
                if target < value:
                    right = middle
                elif target > value:
                    left = middle

        if not found:
            return None

        return middle

    @profile
    def searchInsert2(self, A, target):
        """
        Full scan.
        O(n)
        """

        for i in range(len(A)):
            if A[i] >= target:
                return i
        return i+1


s = Solution()

A_ = range(0, 1000000)
print(s.searchInsert(A_, 999999))

# A_ = [1, 3, 5, 6]

# for i in range(0, 8):
#     print(i, s.searchInsert(A_, i))

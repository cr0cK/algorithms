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

        n = len(A)
        if not target:
            return -1
        if target > A[n - 1]:
            return A[-1]

        left, right = 0, n - 1
        while (left < right):
            mid = left + (right - left) / 2
            if A[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

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

A_ = range(1, 999)
print(s.searchInsert(A_, 999 / 2))

A_ = [1, 3, 5, 6]

for i in range(0, 8):
    print(i, s.searchInsert(A_, i))

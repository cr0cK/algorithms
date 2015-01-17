#!/usr/bin/env python


class Solution:
    # @param num, a list of integer
    # @return an integer
    def findPeakElement(self, num):
        maxEl = None
        idx = 0
        foundIdx = 0

        for i in num:
            if not maxEl or i > maxEl:
                maxEl = i
                foundIdx = idx

            idx += 1

        return foundIdx

s = Solution()
print s.findPeakElement([1, 2, 3, 1])
print s.findPeakElement([1, 2, 3, 3, 6, 2, 9, 1])


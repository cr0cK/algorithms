#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://oj.leetcode.com/problems/permutation-sequence
#
# The set [1,2,3,…,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order,
# We get the following sequence (ie, for n = 3):

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note: Given n will be between 1 and 9 inclusive.


class Solution(object):
    # @return a string
    def getPermutation(self, n, k):
        ret = None
        try:
            permutations = list(self.permute(range(1, n + 1)))
            kth_permut = permutations[k + 1]
            ret = ''.join([str(i) for i in kth_permut])
        except IndexError:
            pass

        return ret

    def permute(self, nums):
        if len(nums) == 2:
            # get the permutations of the last 2 numbers by swapping them
            yield nums
            nums[0], nums[1] = nums[1], nums[0]
            yield nums
        else:
            for i in range(0, len(nums)):
                # fix the first number and get the permutations of the rest of
                # numbers
                for perm in self.permute(nums[0:i] + nums[i+1:len(nums)]):
                    yield [nums[i]] + perm

s = Solution()
r = s.getPermutation(9, 1)
print(r)

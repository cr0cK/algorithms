#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# # https://oj.leetcode.com/problems/symmetric-tree

# Given a binary tree, check whether it is a mirror of itself
# (ie, symmetric around its center).

# For example, this binary tree is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# But the following is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        def isSym(L, R):
            if not L and not R:
                return True
            if L and R and L.val == R.val:
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            return False

        return isSym(root, root)


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


tree = \
    TreeNode(1,
        TreeNode(2,
            TreeNode(3),
            TreeNode(4)  \
        ),
        TreeNode(2,
            TreeNode(4),
            TreeNode(3)
        )
    )

s = Solution()
r = s.isSymmetric(tree)

print(r)

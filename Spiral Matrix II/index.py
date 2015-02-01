#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# https://oj.leetcode.com/problems/spiral-matrix-ii/

# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        self.n = n
        return self.fill_matrix()

    def fill_matrix(self):
        matrix = [[0 for i in range(0, self.n)] for i in range(0, self.n)]

        if self.n == 1:
            return [[1]]

        coords = self.get_coords()

        for i in range(0, len(coords)):
            coord = coords[i]
            matrix[coord[1]][coord[0]] = i + 1

        return matrix

    def get_coords(self):
        x = y = 0

        coords = []
        offset = 0

        while len(coords) < pow(self.n, 2):
            x = offset
            y = offset

            if len(coords) == pow(self.n, 2) - 1:
                coords.append((offset, offset))
                break

            while x < self.n - 1 - offset:
                coords.append((x, y))
                x += 1

            while y < self.n - 1 - offset:
                coords.append((x, y))
                y += 1

            while x > offset:
                coords.append((x, y))
                x -= 1

            while y > offset:
                coords.append((x, y))
                y -= 1

            offset += 1

        return coords[0:pow(self.n, 2)]

s = Solution()
# r = s.generateMatrix(4)
r = s.generateMatrix(1)
print(r)

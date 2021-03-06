#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Writing interview questions hasn't made me rich. Maybe trading Apple stocks
# will.
# I have an array stock_prices_yesterday where:

# The indices are the time, as a number of minutes past trade opening time,
# which was 9:30am local time.
# The values are the price of Apple stock at that time, in dollars.
# For example, the stock cost $500 at 10:30am,
# so stock_prices_yesterday[60] = 500.

# Write an efficient algorithm for computing the best profit I could have made
# from 1 purchase and 1 sale of 1 Apple stock yesterday. For this problem, we
# won't allow "shorting"—you must buy before you sell.

# Gotchas
# It is not sufficient to simply take the difference between the highest price
# and the lowest price, because the highest price may come before the lowest
# price. You must buy before you sell.

# You can do this in O(n) time.

# Breakdown
#
# The brute force ↴
# A brute force algorithm simply enumerates all possible answers to the
# question and checks them for correctness.

# It's seldom the most efficient approach, but it can be helpful to consider
# the time cost of the brute force approach when building an optimized
# solution. If your solution isn't faster than the brute force approach,
# it may not be optimal.
#
# approach would be to try every pair of times (treating the earlier time as
# the buy time and the later time as the sell time) and see which one is best.
# There are n2 such combinations, so this will take O(n2) time. We can do
# better.

# If we're going to do better than O(n2), we're probably going to do it in
# either O(nlg(n)) or O(n). O(nlg(n)) comes up in sorting and searching
# algorithms where we're recursively cutting the set in half. It's not obvious
# that we can save time by cutting the set in half here. Let's first see how
# well we can do by looping through the set only once (this costs only O(n)
# time).

# Since we're going to loop through the set only once, let's use a greedy ↴
# A greedy algorithm iterates through the problem space taking the optimal
# solution "so far," until it reaches the end.

# The greedy approach is only optimal if the problem has "optimal
# substructure," which means stitching together optimal solutions to
# subproblems yields an optimal solution.
# approach, where we keep a running max_profit until we reach the end. We'll
# start our max profit at $0. As we're iterating, how do we know if we've found
# a new max profit?

# At each iteration, our max_profit is either:

# the same as the max_profit at the last time step, or
# the best profit we can get by selling at the current_price
# How do we know when we have case (2)?

# The best profit we can get by selling at the current_price is simply the
# difference between the current_price and the min_price to the left of it.
# If this difference is greater than the current max_profit, we have a new
# max_profit.


from random import randint


class Solution(object):
    def __init__(self):
        self.init_stock()

    def init_stock(self):
        self.stock_prices_yesterday = []
        minutes = 8 * 60

        for m in range(0, minutes):
            self.stock_prices_yesterday.append(randint(200, 1000))

    def get_best_profit(self):
        min_price = self.stock_prices_yesterday[0]

        max_profit = 0
        for current_price in self.stock_prices_yesterday:
            min_price = min(min_price, current_price)
            max_profit = max(max_profit, current_price - min_price)
        return max_profit


s = Solution()
print(s.get_best_profit())

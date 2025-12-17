# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/


class Solution:
    """3573. Best Time to Buy and Sell Stock V

    You are given an integer array `prices` where `prices[i]` is the price of a stock in
    dollars on the `ith` day, and an integer `k`.

    You are allowed to make at most `k` transactions, where each transaction can be
    either of the following:

    * **Normal transaction**: Buy on day `i`, then sell on a later day `j` where `i <
    j`. You profit `prices[j] - prices[i]`.

    * **Short selling transaction**: Sell on day `i`, then buy back on a later day `j`
    where `i < j`. You profit `prices[i] - prices[j]`.

    **Note** that you must complete each transaction before starting another.
    Additionally, you can't buy or sell on the same day you are selling or buying back
    as part of a previous transaction.

    Return the **maximum** total profit you can earn by making **at most** `k`
    transactions."""

    def maximum_profit(self, prices: list[int], k: int) -> int: ...

    maximumProfit = maximum_profit

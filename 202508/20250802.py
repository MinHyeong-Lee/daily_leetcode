# https://leetcode.com/problems/rearranging-fruits/


class Solution:
    """2561. Rearranging Fruits

    You have two fruit baskets containing `n` fruits each. You are given two
    **0-indexed** integer arrays `basket1` and `basket2` representing the cost of fruit
    in each basket. You want to make both baskets **equal**. To do so, you can use the
    following operation as many times as you want:

    * Chose two indices `i` and `j`, and swap the `ith`fruit of `basket1` with the `jth`
    fruit of `basket2`.

    * The cost of the swap is `min(basket1[i],basket2[j])`.

    Two baskets are considered equal if sorting them according to the fruit cost makes
    them exactly the same baskets.

    Return *the minimum cost to make both the baskets equal or* `-1` *if impossible.*"""

    def min_cost(self, basket1: list[int], basket2: list[int]) -> int: ...

    minCost = min_cost

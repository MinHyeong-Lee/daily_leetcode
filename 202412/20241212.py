# https://leetcode.com/problems/take-gifts-from-the-richest-pile/


class Solution:
    """2558. Take Gifts From the Richest Pile

    You are given an integer array `gifts` denoting the number of gifts in various
    piles. Every second, you do the following:

    * Choose the pile with the maximum number of gifts.

    * If there is more than one pile with the maximum number of gifts, choose any.

    * Leave behind the floor of the square root of the number of gifts in the pile. Take
    the rest of the gifts.

    Return *the number of gifts remaining after* `k` *seconds.*"""

    def pick_gifts(self, gifts: list[int], k: int) -> int: ...

    pickGifts = pick_gifts

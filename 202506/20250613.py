# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/


class Solution:
    """2616. Minimize the Maximum Difference of Pairs

    You are given a **0-indexed** integer array `nums` and an integer `p`. Find `p`
    pairs of indices of `nums` such that the **maximum** difference amongst all the
    pairs is **minimized**. Also, ensure no index appears more than once amongst the `p`
    pairs.

    Note that for a pair of elements at the index `i` and `j`, the difference of this
    pair is `|nums[i] - nums[j]|`, where `|x|` represents the **absolute** **value** of
    `x`.

    Return *the **minimum** **maximum** difference among all* `p` *pairs.* We define the
    maximum of an empty set to be zero."""

    def minimize_max(self, nums: list[int], p: int) -> int: ...

    minimizeMax = minimize_max

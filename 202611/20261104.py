# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/


class Solution:
    """3505. Minimum Operations to Make Elements Within K Subarrays Equal

    You are given an integer array `nums` and two integers, `x` and `k`. You can perform
    the following operation any number of times (**including zero**):

    * Increase or decrease any element of `nums` by 1.

    Return the **minimum** number of operations needed to have **at least** `k` *non-
    overlapping subarrays* of size **exactly** `x` in `nums`, where all elements within
    each subarray are equal."""

    def min_operations(self, nums: list[int], x: int, k: int) -> int: ...

    minOperations = min_operations

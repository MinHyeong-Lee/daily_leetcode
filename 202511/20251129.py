# https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/


class Solution:
    """3512. Minimum Operations to Make Array Sum Divisible by K

    You are given an integer array `nums` and an integer `k`. You can perform the
    following operation any number of times:

    * Select an index `i` and replace `nums[i]` with `nums[i] - 1`.

    Return the **minimum** number of operations required to make the sum of the array
    divisible by `k`."""

    def min_operations(self, nums: list[int], k: int) -> int: ...

    minOperations = min_operations

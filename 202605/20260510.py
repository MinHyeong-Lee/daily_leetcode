# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/


class Solution:
    """2770. Maximum Number of Jumps to Reach the Last Index

    You are given a **0-indexed** array `nums` of `n` integers and an integer `target`.

    You are initially positioned at index `0`. In one step, you can jump from index `i`
    to any index `j` such that:

    * `0 <= i < j < n`

    * `-target <= nums[j] - nums[i] <= target`

    Return *the **maximum number of jumps** you can make to reach index* `n - 1`.

    If there is no way to reach index `n - 1`, return `-1`."""

    def maximum_jumps(self, nums: list[int], target: int) -> int: ...

    maximumJumps = maximum_jumps

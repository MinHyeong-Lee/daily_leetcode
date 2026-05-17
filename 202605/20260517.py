# https://leetcode.com/problems/jump-game-iii/


class Solution:
    """1306. Jump Game III

    Given an array of non-negative integers `arr`, you are initially positioned at
    `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]`
    or `i - arr[i]`, check if you can reach **any** index with value 0.

    Notice that you can not jump outside of the array at any time."""

    def can_reach(self, arr: list[int], start: int) -> bool: ...

    canReach = can_reach

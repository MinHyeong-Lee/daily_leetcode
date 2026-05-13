# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/


class Solution:
    """1674. Minimum Moves to Make Array Complementary

    You are given an integer array `nums` of **even** length `n` and an integer `limit`.
    In one move, you can replace any integer from `nums` with another integer between
    `1` and `limit`, inclusive.

    The array `nums` is **complementary** if for all indices `i` (**0-indexed**),
    `nums[i] + nums[n - 1 - i]` equals the same number. For example, the array
    `[1,2,3,4]` is complementary because for all indices `i`, `nums[i] + nums[n - 1 - i]
    = 5`.

    Return the ***minimum** number of moves required to make* `nums`
    ***complementary***."""

    def min_moves(self, nums: list[int], limit: int) -> int: ...

    minMoves = min_moves

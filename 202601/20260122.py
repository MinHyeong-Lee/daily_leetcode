# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/


class Solution:
    """3507. Minimum Pair Removal to Sort Array I

    Given an array `nums`, you can perform the following operation any number of times:

    * Select the **adjacent** pair with the **minimum** sum in `nums`. If multiple such
    pairs exist, choose the leftmost one.

    * Replace the pair with their sum.

    Return the **minimum number of operations** needed to make the array **non-
    decreasing**.

    An array is said to be **non-decreasing** if each element is greater than or equal
    to its previous element (if it exists)."""

    def minimum_pair_removal(self, nums: list[int]) -> int: ...

    minimumPairRemoval = minimum_pair_removal

# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/


class Solution:
    """1671. Minimum Number of Removals to Make Mountain Array

    You may recall that an array `arr` is a **mountain array** if and only if:

    * `arr.length >= 3`

    * There exists some index `i` (**0\\-indexed**) with `0 < i < arr.length - 1` such
    that:

            + `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`

            + `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

    Given an integer array `nums`\u200b\u200b\u200b, return *the **minimum** number of elements to
    remove to make* `nums\u200b\u200b\u200b`*a **mountain array**.*

    """

    def minimum_mountain_removals(self, nums: list[int]) -> int: ...

    minimumMountainRemovals = minimum_mountain_removals

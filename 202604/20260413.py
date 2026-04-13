# https://leetcode.com/problems/minimum-distance-to-the-target-element/


class Solution:
    """1848. Minimum Distance to the Target Element

    Given an integer array `nums` **(0-indexed)** and two integers `target` and `start`,
    find an index `i` such that `nums[i] == target` and `abs(i - start)` is
    **minimized**. Note that `abs(x)` is the absolute value of `x`.

    Return `abs(i - start)`.

    It is **guaranteed** that `target` exists in `nums`."""

    def get_min_distance(self, nums: list[int], target: int, start: int) -> int: ...

    getMinDistance = get_min_distance

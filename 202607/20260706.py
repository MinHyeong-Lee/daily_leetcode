# https://leetcode.com/problems/remove-covered-intervals/


class Solution:
    """1288. Remove Covered Intervals

    Given an array `intervals` where `intervals[i] = [li, ri]` represent the interval
    `[li, ri)`, remove all intervals that are covered by another interval in the list.

    The interval `[a, b)` is covered by the interval `[c, d)` if and only if `c <= a`
    and `b <= d`.

    Return *the number of remaining intervals*."""

    def remove_covered_intervals(self, intervals: list[list[int]]) -> int: ...

    removeCoveredIntervals = remove_covered_intervals

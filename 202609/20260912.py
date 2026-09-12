# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/


class Solution:
    """3414. Maximum Score of Non-overlapping Intervals

    You are given a 2D integer array `intervals`, where `intervals[i] = [li, ri,
    weighti]`. Interval `i` starts at position `li` and ends at `ri`, and has a weight
    of `weighti`. You can choose *up to* 4 **non-overlapping** intervals. The **score**
    of the chosen intervals is defined as the total sum of their weights.

    Return the lexicographically smallest array of at most 4 indices from `intervals`
    with **maximum** score, representing your choice of non-overlapping intervals.

    Two intervals are said to be **non-overlapping** if they do not share any points. In
    particular, intervals sharing a left or right boundary are considered overlapping.
    """

    def maximum_weight(self, intervals: list[list[int]]) -> list[int]: ...

    maximumWeight = maximum_weight

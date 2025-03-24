# https://leetcode.com/problems/count-days-without-meetings/


class Solution:
    """3169. Count Days Without Meetings

    You are given a positive integer `days` representing the total number of days an
    employee is available for work (starting from day 1). You are also given a 2D array
    `meetings` of size `n` where, `meetings[i] = [start_i, end_i]` represents the
    starting and ending days of meeting `i` (inclusive).

    Return the count of days when the employee is available for work but no meetings are
    scheduled.

    **Note:** The meetings may overlap."""

    def count_days(self, days: int, meetings: list[list[int]]) -> int: ...

    countDays = count_days

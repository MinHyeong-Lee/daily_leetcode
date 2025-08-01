# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/


class Solution:
    """1751. Maximum Number of Events That Can Be Attended II

    You are given an array of `events` where `events[i] = [startDayi, endDayi, valuei]`.
    The `ith` event starts at `startDayi`and ends at `endDayi`, and if you attend this
    event, you will receive a value of `valuei`. You are also given an integer `k` which
    represents the maximum number of events you can attend.

    You can only attend one event at a time. If you choose to attend an event, you must
    attend the **entire** event. Note that the end day is **inclusive**: that is, you
    cannot attend two events where one of them starts and the other ends on the same
    day.

    Return *the **maximum sum** of values that you can receive by attending events.*"""

    def max_value(self, events: list[list[int]], k: int) -> int: ...

    maxValue = max_value

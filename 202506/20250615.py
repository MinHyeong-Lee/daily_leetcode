# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/


class Solution:
    """1432. Max Difference You Can Get From Changing an Integer

    You are given an integer `num`. You will apply the following steps to `num` **two**
    separate times:

    * Pick a digit `x (0 <= x <= 9)`.

    * Pick another digit `y (0 <= y <= 9)`. Note `y` can be equal to `x`.

    * Replace all the occurrences of `x` in the decimal representation of `num` by `y`.

    Let `a` and `b` be the two results from applying the operation to `num`
    *independently*.

    Return *the max difference* between `a` and `b`.

    Note that neither `a` nor `b` may have any leading zeros, and **must not** be 0."""

    def max_diff(self, num: int) -> int: ...

    maxDiff = max_diff

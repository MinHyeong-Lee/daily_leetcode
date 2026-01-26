# https://leetcode.com/problems/minimum-absolute-difference/


class Solution:
    """1200. Minimum Absolute Difference

    Given an array of **distinct** integers `arr`, find all pairs of elements with the
    minimum absolute difference of any two elements.

    Return a list of pairs in ascending order(with respect to pairs), each pair `[a, b]`
    follows

    * `a, b` are from `arr`

    * `a < b`

    * `b - a` equals to the minimum absolute difference of any two elements in `arr`"""

    def minimum_abs_difference(self, arr: list[int]) -> list[list[int]]: ...

    minimumAbsDifference = minimum_abs_difference

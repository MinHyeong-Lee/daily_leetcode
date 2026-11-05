# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/


class Solution:
    """1385. Find the Distance Value Between Two Arrays

    Given two integer arrays `arr1` and `arr2`, and the integer `d`, *return the
    distance value between the two arrays*.

    The distance value is defined as the number of elements `arr1[i]` such that there is
    not any element `arr2[j]` where `|arr1[i]-arr2[j]| <= d`."""

    def find_the_distance_value(
        self, arr1: list[int], arr2: list[int], d: int
    ) -> int: ...

    findTheDistanceValue = find_the_distance_value

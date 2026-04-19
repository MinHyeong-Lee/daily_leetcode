# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/


class Solution:
    """1855. Maximum Distance Between a Pair of Values

    You are given two **non-increasing 0-indexed** integer arrays `nums1`\u200b\u200b\u200b\u200b\u200b\u200b and
    `nums2`\u200b\u200b\u200b\u200b\u200b\u200b.

    A pair of indices `(i, j)`, where `0 <= i < nums1.length` and `0 <= j <
    nums2.length`, is **valid** if both `i <= j` and `nums1[i] <= nums2[j]`. The
    **distance** of the pair is `j - i`\u200b\u200b\u200b\u200b.

    Return *the **maximum distance** of any **valid** pair* `(i, j)`*. If there are no
    valid pairs, return* `0`.

    An array `arr` is **non-increasing** if `arr[i-1] >= arr[i]` for every `1 <= i <
    arr.length`."""

    def max_distance(self, nums1: list[int], nums2: list[int]) -> int: ...

    maxDistance = max_distance

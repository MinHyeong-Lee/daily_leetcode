# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/


class Solution:
    """3337. Total Characters in String After Transformations II

    You are given a string `s` consisting of lowercase English letters, an integer `t`
    representing the number of **transformations** to perform, and an array `nums` of
    size 26. In one **transformation**, every character in `s` is replaced according to
    the following rules:

    * Replace `s[i]` with the **next** `nums[s[i] - 'a']` consecutive characters in the
    alphabet. For example, if `s[i] = 'a'` and `nums[0] = 3`, the character `'a'`
    transforms into the next 3 consecutive characters ahead of it, which results in
    `"bcd"`.

    * The transformation **wraps** around the alphabet if it exceeds `'z'`. For example,
    if `s[i] = 'y'` and `nums[24] = 3`, the character `'y'` transforms into the next 3
    consecutive characters ahead of it, which results in `"zab"`.

    Return the length of the resulting string after **exactly** `t` transformations.

    Since the answer may be very large, return it **modulo** `109 + 7`."""

    def length_after_transformations(self, s: str, t: int, nums: list[int]) -> int: ...

    lengthAfterTransformations = length_after_transformations

# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/


class Solution:
    """2839. Check if Strings Can be Made Equal With Operations I

    You are given two strings `s1` and `s2`, both of length `4`, consisting of
    **lowercase** English letters.

    You can apply the following operation on any of the two strings **any** number of
    times:

    * Choose any two indices `i` and `j` such that `j - i = 2`, then **swap** the two
    characters at those indices in the string.

    Return `true` *if you can make the strings* `s1` *and* `s2` *equal, and* `false`
    *otherwise*."""

    def can_be_equal(self, s1: str, s2: str) -> bool: ...

    canBeEqual = can_be_equal

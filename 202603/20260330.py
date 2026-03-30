# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/


class Solution:
    """2840. Check if Strings Can be Made Equal With Operations II

    You are given two strings `s1` and `s2`, both of length `n`, consisting of
    **lowercase** English letters.

    You can apply the following operation on **any** of the two strings **any** number
    of times:

    * Choose any two indices `i` and `j` such that `i < j` and the difference `j - i` is
    **even**, then **swap** the two characters at those indices in the string.

    Return `true` *if you can make the strings* `s1` *and* `s2` *equal, and*`false`
    *otherwise*."""

    def check_strings(self, s1: str, s2: str) -> bool: ...

    checkStrings = check_strings

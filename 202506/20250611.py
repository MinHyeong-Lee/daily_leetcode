# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/


class Solution:
    """3445. Maximum Difference Between Even and Odd Frequency II

    You are given a string `s` and an integer `k`. Your task is to find the **maximum**
    difference between the frequency of **two** characters, `freq[a] - freq[b]`, in a
    substring `subs` of `s`, such that:

    * `subs` has a size of **at least** `k`.

    * Character `a` has an *odd frequency* in `subs`.

    * Character `b` has an *even frequency* in `subs`.

    Return the **maximum** difference.

    **Note** that `subs` can contain more than 2 **distinct** characters."""

    def max_difference(self, s: str, k: int) -> int: ...

    maxDifference = max_difference

# https://leetcode.com/problems/longest-subsequence-repeated-k-times/


class Solution:
    """2014. Longest Subsequence Repeated k Times

    You are given a string `s` of length `n`, and an integer `k`. You are tasked to find
    the **longest subsequence repeated** `k` times in string `s`.

    A **subsequence** is a string that can be derived from another string by deleting
    some or no characters without changing the order of the remaining characters.

    A subsequence `seq` is **repeated** `k` times in the string `s` if `seq * k` is a
    subsequence of `s`, where `seq * k` represents a string constructed by concatenating
    `seq` `k` times.

    * For example, `"bba"` is repeated `2` times in the string `"bababcba"`, because the
    string `"bbabba"`, constructed by concatenating `"bba"` `2` times, is a subsequence
    of the string `"bababcba"`.

    Return *the **longest subsequence repeated*** `k` *times in string* `s`*. If
    multiple such subsequences are found, return the **lexicographically largest** one.
    If there is no such subsequence, return an **empty** string*."""

    def longest_subsequence_repeated_k(self, s: str, k: int) -> str: ...

    longestSubsequenceRepeatedK = longest_subsequence_repeated_k

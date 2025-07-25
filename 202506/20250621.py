# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/


class Solution:
    """3085. Minimum Deletions to Make String K-Special

    You are given a string `word` and an integer `k`.

    We consider `word` to be **k-special** if `|freq(word[i]) - freq(word[j])| <= k` for
    all indices `i` and `j` in the string.

    Here, `freq(x)` denotes the frequency of the character `x` in `word`, and `|y|`
    denotes the absolute value of `y`.

    Return *the **minimum** number of characters you need to delete to make* `word`
    ***k-special***."""

    def minimum_deletions(self, word: str, k: int) -> int: ...

    minimumDeletions = minimum_deletions

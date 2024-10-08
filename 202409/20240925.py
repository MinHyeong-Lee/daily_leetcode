# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/


class Solution:
    """2416. Sum of Prefix Scores of Strings

    You are given an array `words` of size `n` consisting of **non\\-empty** strings.

    We define the **score** of a string `word` as the **number** of strings `words[i]`
    such that `word` is a **prefix** of `words[i]`.

    * For example, if `words = ["a", "ab", "abc", "cab"]`, then the score of `"ab"` is
    `2`, since `"ab"` is a prefix of both `"ab"` and `"abc"`.

    Return *an array* `answer` *of size* `n` *where* `answer[i]` *is the **sum** of
    scores of every **non\\-empty** prefix of* `words[i]`.

    **Note** that a string is considered as a prefix of itself.

    """

    def sum_prefix_scores(self, words: list[str]) -> list[int]: ...

    sumPrefixScores = sum_prefix_scores

# https://leetcode.com/problems/score-of-parentheses/


class Solution:
    """856. Score of Parentheses

    Given a balanced parentheses string `s`, return *the **score** of the string*.

    The **score** of a balanced parentheses string is based on the following rule:

    * `"()"` has score `1`.

    * `AB` has score `A + B`, where `A` and `B` are balanced parentheses strings.

    * `(A)` has score `2 * A`, where `A` is a balanced parentheses string."""

    def score_of_parentheses(self, s: str) -> int: ...

    scoreOfParentheses = score_of_parentheses

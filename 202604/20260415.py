# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/


class Solution:
    """2515. Shortest Distance to Target String in a Circular Array

    You are given a **0-indexed** **circular** string array `words` and a string
    `target`. A **circular array** means that the array's end connects to the array's
    beginning.

    * Formally, the next element of `words[i]` is `words[(i + 1) % n]` and the previous
    element of `words[i]` is `words[(i - 1 + n) % n]`, where `n` is the length of
    `words`.

    Starting from `start_index`, you can move to either the next word or the previous
    word with `1` step at a time.

    Return *the **shortest** distance needed to reach the string* `target`. If the
    string `target` does not exist in `words`, return `-1`."""

    def closest_target(
        self, words: list[str], target: str, start_index: int
    ) -> int: ...

    closestTarget = closest_target

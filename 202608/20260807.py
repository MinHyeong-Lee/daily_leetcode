# https://leetcode.com/problems/smallest-divisible-digit-product-ii/


class Solution:
    """3348. Smallest Divisible Digit Product II

    You are given a string `num` which represents a **positive** integer, and an integer
    `t`.

    A number is called **zero-free** if *none* of its digits are 0.

    Return a string representing the **smallest** **zero-free** number greater than or
    equal to `num` such that the **product of its digits** is divisible by `t`. If no
    such number exists, return `"-1"`."""

    def smallest_number(self, num: str, t: int) -> str: ...

    smallestNumber = smallest_number

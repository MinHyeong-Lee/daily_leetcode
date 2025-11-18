# https://leetcode.com/problems/1-bit-and-2-bit-characters/


class Solution:
    """717. 1-bit and 2-bit Characters

    We have two special characters:

    * The first character can be represented by one bit `0`.

    * The second character can be represented by two bits (`10` or `11`).

    Given a binary array `bits` that ends with `0`, return `true` if the last character
    must be a one-bit character."""

    def is_one_bit_character(self, bits: list[int]) -> bool: ...

    isOneBitCharacter = is_one_bit_character

# https://leetcode.com/problems/string-compression-iii/


class Solution:
    """3163. String Compression III

    Given a string `word`, compress it using the following algorithm:

    * Begin with an empty string `comp`. While `word` is **not** empty, use the
    following operation:

            + Remove a maximum length prefix of `word` made of a *single character* `c`
    repeating **at most** 9 times.

            + Append the length of the prefix followed by `c` to `comp`.

    Return the string `comp`.

    """

    def compressed_string(self, word: str) -> str: ...

    compressedString = compressed_string
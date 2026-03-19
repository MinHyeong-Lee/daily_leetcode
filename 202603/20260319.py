# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/


class Solution:
    """3212. Count Submatrices With Equal Frequency of X and Y

    Given a 2D character matrix `grid`, where `grid[i][j]` is either `'X'`, `'Y'`, or
    `'.'`, return the number of submatrices that contain:

    * `grid[0][0]`

    * an **equal** frequency of `'X'` and `'Y'`.

    * **at least** one `'X'`."""

    def number_of_submatrices(self, grid: list[list[str]]) -> int: ...

    numberOfSubmatrices = number_of_submatrices

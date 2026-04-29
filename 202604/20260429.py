# https://leetcode.com/problems/maximum-score-from-grid-operations/


class Solution:
    """3225. Maximum Score From Grid Operations

    You are given a 2D matrix `grid` of size `n x n`. Initially, all cells of the grid
    are colored white. In one operation, you can select any cell of indices `(i, j)`,
    and color black all the cells of the `jth` column starting from the top row down to
    the `ith` row.

    The grid score is the sum of all `grid[i][j]` such that cell `(i, j)` is white and
    it has a horizontally adjacent black cell.

    Return the **maximum** score that can be achieved after some number of operations.
    """

    def maximum_score(self, grid: list[list[int]]) -> int: ...

    maximumScore = maximum_score

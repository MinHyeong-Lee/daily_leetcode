# https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/


class Solution:
    """2946. Matrix Similarity After Cyclic Shifts

    You are given an `m x n` integer matrix `mat` and an integer `k`. The matrix rows
    are 0-indexed.

    The following proccess happens `k` times:

    * **Even-indexed** rows (0, 2, 4, ...) are cyclically shifted to the left.

    ![](https://assets.leetcode.com/uploads/2024/05/19/lshift.jpg)

    * **Odd-indexed** rows (1, 3, 5, ...) are cyclically shifted to the right.

    ![](https://assets.leetcode.com/uploads/2024/05/19/rshift-stlone.jpg)

    Return `true` if the final modified matrix after `k` steps is identical to the
    original matrix, and `false` otherwise."""

    def are_similar(self, mat: list[list[int]], k: int) -> bool: ...

    areSimilar = are_similar
